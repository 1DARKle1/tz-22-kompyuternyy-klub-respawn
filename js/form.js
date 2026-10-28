(function () {
  var form = document.querySelector("#lead-form");
  if (!form) return;

  var leadType = form.querySelector("#lead_type");
  var nameInput = form.querySelector("#name");
  var nameLabel = form.querySelector("label[for='name']");
  var phone = form.querySelector("#phone");
  var email = form.querySelector("#email");
  var zone = form.querySelector("#zone");
  var slotWrap = document.querySelector("#slot-wrap");
  var slot = form.querySelector("#slot");
  var seats = form.querySelector("#seats");
  var seatsWrap = document.querySelector("#seats-wrap");
  var consent = form.querySelector("#consent");
  var summary = document.querySelector("#quote-summary");
  var status = document.querySelector("#form-status");
  var submit = form.querySelector("#submit-lead");
  var requestId = form.querySelector("#request_id");
  var quote = readQuote();
  var quoteTouched = false;

  function readQuote() {
    try {
      return JSON.parse(sessionStorage.getItem("respawn_quote") || "null");
    } catch (error) {
      return null;
    }
  }

  function utm(key, fallback) {
    return (sessionStorage.getItem(key) || "").trim() || fallback;
  }

  function setError(id, text) {
    var field = form.querySelector("#" + id);
    var box = document.querySelector("#error-" + id);
    if (field) field.setAttribute("aria-invalid", text ? "true" : "false");
    if (box) box.textContent = text || "";
  }

  function clearErrors() {
    ["name", "phone", "email", "zone", "slot", "seats", "consent", "lead_type"].forEach(function (id) {
      setError(id, "");
    });
  }

  function normalizePhone(value) {
    var digits = String(value).replace(/\D/g, "");
    if (digits.length === 11 && (digits.charAt(0) === "7" || digits.charAt(0) === "8")) {
      return "+7" + digits.slice(1);
    }
    if (digits.length === 10) return "+7" + digits;
    return "";
  }

  function syncSeats() {
    var tournament = leadType.value === "tournament";
    var min = tournament || zone.value === "bootcamp" ? 5 : 1;
    var max = zone.value === "ps5" ? 4 : 5;
    Array.prototype.forEach.call(seats.options, function (option) {
      var n = Number(option.value);
      option.hidden = n < min || n > max;
    });
    if (Number(seats.value) < min || Number(seats.value) > max) seats.value = String(min);
  }

  function applyMode() {
    var tournament = leadType.value === "tournament";
    nameLabel.textContent = tournament ? "Название команды" : "Имя";
    slotWrap.hidden = tournament;
    seatsWrap.hidden = tournament;
    if (!tournament && quote) {
      if (!zone.value && quote.zone) zone.value = quote.zone;
      if (!zone.value || zone.value === quote.zone) {
        if (quote.seats) seats.value = String(quote.seats);
        if (quote.slot && !slot.value) slot.value = quote.slot;
      }
    }
    syncSeats();
    renderSummary();
  }

  function freshQuote() {
    if (!quote || !window.RespawnPricing || !slot.value || !zone.value) return null;
    return window.RespawnPricing.quote({
      zone: zone.value,
      seats: Number(seats.value || quote.seats || 1),
      hours: quote.hours || 1,
      start: new Date(slot.value),
      packageName: quoteTouched ? "" : (quote.packageName || "")
    });
  }

  function currentTotal() {
    if (leadType.value === "tournament") return 2500;
    if (!quote) return null;
    var fresh = freshQuote();
    return fresh ? fresh.total : quote.total;
  }

  function renderSummary() {
    if (leadType.value === "tournament") {
      summary.textContent = "Взнос «Зимнего кубка» — 2 500 ₽ с команды. Время брони для турнира не нужно.";
      return;
    }
    if (!quote) {
      summary.textContent = "Если посчитать стоимость на странице «Цены», сумма подставится сюда.";
      return;
    }
    var fresh = freshQuote();
    var total = fresh ? fresh.total : quote.total;
    var text = fresh && quoteTouched ? fresh.formula : (quote.formula || "");
    summary.textContent = text + (total ? " К отправке: " + total + " ₽." : "");
  }

  function firstProblem(payload) {
    if (payload.name.length < 2 || payload.name.length > 60) {
      return { field: "name", type: payload.name ? "format" : "required", text: "Нужно от 2 до 60 символов." };
    }
    if (!phone.value.trim()) {
      return { field: "phone", type: "required", text: "Впиши телефон." };
    }
    if (!payload.phone) {
      return { field: "phone", type: "format", text: "Телефон: +7 и 10 цифр, например +79002220222." };
    }
    if (payload.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(payload.email)) {
      return { field: "email", type: "format", text: "Похоже, в почте ошибка." };
    }
    if (!payload.zone) {
      return { field: "zone", type: "required", text: "Выбери зону." };
    }
    if (payload.lead_type === "booking" && !payload.slot) {
      return { field: "slot", type: "required", text: "Укажи дату и время начала." };
    }
    if (!payload.seats || payload.seats < 1 || payload.seats > 5) {
      return { field: "seats", type: "range", text: "Мест: от 1 до 5." };
    }
    if (payload.zone === "ps5" && payload.seats > 4) {
      return { field: "seats", type: "range", text: "На PlayStation 5 до 4 игроков." };
    }
    if (!consent.checked) {
      return { field: "consent", type: "required", text: "Без согласия на обработку данных заявка не уйдёт." };
    }
    return null;
  }

  function fail(problem) {
    clearErrors();
    setError(problem.field, problem.text);
    status.textContent = "Заявка не отправлена.";
    window.RespawnTrack("form_error", {
      field_name: problem.field,
      error_type: problem.type
    });
  }

  leadType.addEventListener("change", applyMode);
  zone.addEventListener("change", function () {
    quoteTouched = true;
    syncSeats();
    renderSummary();
  });
  seats.addEventListener("change", function () {
    quoteTouched = true;
    renderSummary();
  });
  slot.addEventListener("change", function () {
    quoteTouched = true;
    renderSummary();
  });

  var initial = new URLSearchParams(window.location.search);
  if (initial.get("lead_type") === "tournament" || initial.get("lead_type") === "booking") {
    leadType.value = initial.get("lead_type");
  }
  if (initial.get("zone")) zone.value = initial.get("zone");
  applyMode();

  if (!requestId.value) requestId.value = "REQ-" + crypto.randomUUID().toUpperCase();

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    clearErrors();
    var tournament = leadType.value === "tournament";
    var payload = {
      request_id: requestId.value,
      name: nameInput.value.trim(),
      phone: normalizePhone(phone.value),
      email: email.value.trim(),
      lead_type: leadType.value,
      zone: zone.value,
      slot: tournament ? "" : slot.value,
      seats: tournament ? 5 : Number(seats.value),
      utm_source: utm("utm_source", "direct"),
      utm_medium: utm("utm_medium", "none"),
      utm_campaign: utm("utm_campaign", "not_set"),
      utm_content: utm("utm_content", "not_set")
    };
    var problem = firstProblem(payload);
    if (problem) {
      fail(problem);
      return;
    }

    var endpoint = (window.RESPAWN_CONFIG && window.RESPAWN_CONFIG.webAppUrl) || "";
    if (!/^https:\/\/script\.google\.com\/macros\/s\/[^/]+\/exec$/.test(endpoint)) {
      fail({
        field: "lead_type",
        type: "server",
        text: "В js/config.js ещё не вставлен адрес Apps Script."
      });
      return;
    }

    submit.disabled = true;
    status.textContent = "Отправляем заявку…";
    fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify(payload)
    })
      .then(function (response) { return response.text(); })
      .then(function (text) {
        var data = {};
        var start = text.indexOf("{");
        var end = text.lastIndexOf("}");
        if (start !== -1 && end !== -1) text = text.slice(start, end + 1);
        try { data = JSON.parse(text); } catch (error) { data = { ok: false, error: "bad_response" }; }
        if (!data.ok) throw new Error(data.error || "server");
        var total = currentTotal();
        var lead = { lead_type: payload.lead_type, lead_zone: payload.zone, currency: "RUB" };
        if (typeof total === "number") lead.value = total;
        window.RespawnTrack("generate_lead", lead);
        var next = new URLSearchParams({
          request_id: payload.request_id,
          zone: payload.zone,
          lead_type: payload.lead_type
        });
        if (payload.slot) next.set("slot", payload.slot);
        if (typeof total === "number") next.set("total", String(total));
        window.location.href = "thanks.html?" + next.toString();
      })
      .catch(function () {
        submit.disabled = false;
        fail({
          field: "lead_type",
          type: "server",
          text: "Приёмник не записал заявку. Проверь таблицу и попробуй ещё раз. Номер этой попытки сохранён."
        });
      });
  });
})();
