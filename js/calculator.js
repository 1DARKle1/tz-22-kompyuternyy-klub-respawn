(function () {
  var form = document.querySelector("#calculator");
  if (!form || !window.RespawnPricing) return;

  var zone = form.querySelector("#calc-zone");
  var seats = form.querySelector("#calc-seats");
  var start = form.querySelector("#calc-start");
  var hours = form.querySelector("#calc-hours");
  var output = document.querySelector("#calc-result");
  var formula = document.querySelector("#calc-formula");
  var error = document.querySelector("#calc-error");
  var book = document.querySelector("#calc-book");
  var packageName = "";

  function seatBounds(zoneName) {
    if (zoneName === "ps5") return { min: 1, max: 4 };
    if (zoneName === "bootcamp") return { min: 5, max: 5 };
    return { min: 1, max: 5 };
  }

  function syncSeats() {
    var bounds = seatBounds(zone.value);
    seats.min = String(bounds.min);
    seats.max = String(bounds.max);
    var current = Number(seats.value || bounds.min);
    if (current < bounds.min || current > bounds.max) seats.value = String(bounds.min);
    if (zone.value === "bootcamp") seats.value = "5";
  }

  function showError(text) {
    error.textContent = text;
    formula.textContent = "";
    output.textContent = "";
  }

  function calculate() {
    error.textContent = "";
    if (!zone.value || !start.value || !hours.value || !seats.value) {
      showError("Заполни зону, число мест, начало и часы.");
      return;
    }
    var when = new Date(start.value);
    if (Number.isNaN(when.getTime())) {
      showError("Укажи дату и время начала.");
      return;
    }
    var hourCount = Number(hours.value);
    if (hourCount < 1 || hourCount > 12) {
      showError("Часы брони: от 1 до 12.");
      return;
    }
    syncSeats();
    var result = window.RespawnPricing.quote({
      zone: zone.value,
      seats: Number(seats.value),
      hours: hourCount,
      start: when,
      packageName: packageName
    });
    output.textContent = result.total + " ₽";
    formula.textContent = result.formula + " Тариф: " + result.bandLabel + " (" + result.timeBand + ").";
    var payload = {
      zone: result.zone,
      seats: result.seats,
      hours: result.hours,
      slot: start.value,
      total: result.total,
      timeBand: result.timeBand,
      formula: result.formula,
      packageName: result.packageName
    };
    sessionStorage.setItem("respawn_quote", JSON.stringify(payload));
    book.href = "contacts.html?lead_type=booking&zone=" + encodeURIComponent(result.zone);
    window.RespawnTrack("booking_calc", {
      zone: result.zone,
      seats: result.seats,
      hours: result.hours,
      time_band: result.timeBand,
      total_price: result.total
    });
  }

  zone.addEventListener("change", function () {
    packageName = "";
    syncSeats();
  });
  hours.addEventListener("input", function () { packageName = ""; });

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    calculate();
  });

  document.querySelectorAll("[data-package-name]").forEach(function (button) {
    button.addEventListener("click", function () {
      packageName = button.getAttribute("data-package-name");
      if (packageName.indexOf("standard") !== -1) zone.value = "standard";
      if (packageName.indexOf("vip") !== -1) zone.value = "vip";
      if (packageName.indexOf("3h") !== -1) hours.value = "3";
      if (packageName.indexOf("night") !== -1 && start.value) {
        start.value = start.value.slice(0, 11) + "23:00";
      }
      syncSeats();
      if (!seats.value) seats.value = "1";
      if (!start.value) {
        error.textContent = "Пакет выбран. Укажи дату и время начала и нажми «Рассчитать».";
        formula.textContent = "";
        output.textContent = "";
        return;
      }
      calculate();
    });
  });

  syncSeats();
})();
