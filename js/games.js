(function () {
  var input = document.querySelector("#game-search");
  var list = document.querySelectorAll("#game-list .game");
  var count = document.querySelector("#game-count");
  if (!input || !list.length) return;

  var timer = null;

  function apply(term) {
    var needle = term.trim().toLowerCase();
    var found = 0;
    list.forEach(function (item) {
      var hay = (item.getAttribute("data-search") || "").toLowerCase();
      var show = !needle || hay.indexOf(needle) !== -1;
      item.hidden = !show;
      if (show) found += 1;
    });
    count.textContent = "Найдено: " + found;
    return found;
  }

  apply("");

  input.addEventListener("input", function () {
    window.clearTimeout(timer);
    var term = input.value;
    timer = window.setTimeout(function () {
      var found = apply(term);
      window.RespawnTrack("game_search", {
        search_term: term.trim().slice(0, 100),
        results_count: found
      });
    }, 1000);
  });
})();
