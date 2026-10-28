(function () {
  var params = new URLSearchParams(window.location.search);
  var id = params.get("request_id") || "";
  var zone = params.get("zone") || "";
  var slot = params.get("slot") || "";
  var leadType = params.get("lead_type") || "booking";
  var names = {
    standard: "Стандарт",
    vip: "VIP",
    bootcamp: "Bootcamp",
    ps5: "PlayStation 5"
  };
  var idNode = document.querySelector("#thanks-id");
  var zoneNode = document.querySelector("#thanks-zone");
  var timeNode = document.querySelector("#thanks-time");
  if (!idNode) return;
  idNode.textContent = id || "Номер появится после отправки формы";
  zoneNode.textContent = names[zone] || "—";
  if (leadType === "tournament") {
    timeNode.textContent = "Финал 19 декабря в клубе. Поля времени у регистрации нет.";
  } else if (slot) {
    var when = new Date(slot);
    timeNode.textContent = Number.isNaN(when.getTime())
      ? slot
      : when.toLocaleString("ru-RU", { dateStyle: "long", timeStyle: "short" });
  } else {
    timeNode.textContent = "—";
  }
})();
