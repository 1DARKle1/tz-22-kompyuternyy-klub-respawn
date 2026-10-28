/* Пять удачных попыток. Ранний клик — фальстарт, в среднее не входит. */
(function () {
  var pad = document.querySelector("#reaction-pad");
  var table = document.querySelector("#reaction-table");
  var averageCell = document.querySelector("#reaction-average");
  var note = document.querySelector("#reaction-note");
  if (!pad || !table) return;

  var times = [];
  var phase = "idle";
  var startedAt = 0;
  var timer = null;
  var sent = false;

  function paint(text, go) {
    pad.textContent = text;
    pad.classList.toggle("is-go", Boolean(go));
  }

  function waitNext() {
    phase = "wait";
    paint("Жди зелёный экран", false);
    var delay = 1000 + Math.floor(Math.random() * 3001);
    timer = window.setTimeout(function () {
      phase = "go";
      startedAt = performance.now();
      paint("ЖМИ", true);
    }, delay);
  }

  function finish() {
    phase = "done";
    var sum = times.reduce(function (acc, value) { return acc + value; }, 0);
    var average = Math.round(sum / times.length);
    averageCell.textContent = String(average);
    paint("Среднее " + average + " мс", false);
    note.textContent = "Промокод REACT20 на утреннюю бронь. Скидка и пакеты не суммируются.";
    if (!sent) {
      sent = true;
      window.RespawnTrack("reaction_test_complete", { reaction_ms: average });
    }
  }

  var promo = document.querySelector("#promo-copy");
  var promoStatus = document.querySelector("#promo-status");
  if (promo) {
    promo.addEventListener("click", function () {
      var code = "REACT20";
      function done() {
        if (promoStatus) promoStatus.textContent = "Промокод REACT20 скопирован.";
      }
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(code).then(done, fallback);
      } else {
        fallback();
      }
      function fallback() {
        var area = document.createElement("textarea");
        area.value = code;
        document.body.appendChild(area);
        area.select();
        document.execCommand("copy");
        area.remove();
        done();
      }
    });
  }

  pad.addEventListener("click", function () {
    if (phase === "done") return;
    if (phase === "idle") {
      waitNext();
      return;
    }
    if (phase === "wait") {
      window.clearTimeout(timer);
      note.textContent = "Фальстарт. Эта попытка не засчитана и начнётся заново.";
      waitNext();
      return;
    }
    var ms = Math.round(performance.now() - startedAt);
    times.push(ms);
    var row = table.querySelector('[data-attempt="' + times.length + '"]');
    if (row) row.textContent = String(ms);
    if (times.length === 5) finish();
    else waitNext();
  });
})();
