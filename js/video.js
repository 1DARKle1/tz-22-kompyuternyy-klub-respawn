(function () {
  var button = document.querySelector("#video-play");
  var frame = document.querySelector("#video-frame");
  if (!button || !frame) return;

  var frames = [
    "Общий зал: 40 мест «Стандарт», RTX 4060, мониторы 165 Гц.",
    "VIP: RTX 4080, мониторы 240 Гц, кресла премиум. 12 мест.",
    "Комната bootcamp на пятерых. Цена за комнату, не за место.",
    "PlayStation 5 и телевизор 65 дюймов, до четырёх игроков."
  ];
  var index = 0;
  var timer = null;

  button.addEventListener("click", function () {
    if (timer) return;
    frame.hidden = false;
    index = 0;
    frame.textContent = frames[0];
    timer = window.setInterval(function () {
      index += 1;
      if (index >= frames.length) {
        window.clearInterval(timer);
        timer = null;
        button.textContent = "Смотреть ещё раз";
        return;
      }
      frame.textContent = frames[index];
    }, 1600);
  });
})();
