/* Все вызовы gtag('event') живут в этом файле.
   Кнопки помечаются data-event. Страницы вызывают RespawnTrack. */
(function () {
  var UTM_KEYS = ["utm_source", "utm_medium", "utm_campaign", "utm_content"];

  function saveUtm() {
    var params = new URLSearchParams(window.location.search);
    UTM_KEYS.forEach(function (key) {
      var value = (params.get(key) || "").trim();
      if (value) sessionStorage.setItem(key, value.slice(0, 100));
    });
  }

  function track(name, params) {
    var payload = {};
    if (params) {
      Object.keys(params).forEach(function (key) {
        var value = params[key];
        if (value === undefined || value === null || value === "") return;
        payload[key] = typeof value === "number" ? value : String(value).slice(0, 100);
      });
    }
    if (typeof window.gtag === "function") {
      window.gtag("event", name, payload);
    }
  }

  var fieldsByEvent = {
    cta_click: ["button_name", "page_section"],
    zone_view: ["zone"],
    package_select: ["package_name"],
    tournament_view: ["tournament_id"],
    contact_click: ["contact_type"],
    messenger_click: ["messenger"],
    social_click: ["network", "page_section"],
    promo_copy: ["promo_code"],
    video_play: ["video_title"]
  };

  function readParams(el, fields) {
    var params = {};
    fields.forEach(function (field) {
      var attr = "data-" + field.replace(/_/g, "-");
      var value = el.getAttribute(attr);
      if (value) params[field] = value;
    });
    return params;
  }

  document.addEventListener("click", function (event) {
    var el = event.target.closest("[data-event]");
    if (!el) return;
    var name = el.getAttribute("data-event");
    var fields = fieldsByEvent[name];
    if (!fields) return;
    track(name, readParams(el, fields));
  });

  saveUtm();
  window.RespawnTrack = track;
})();
