(function () {
  var button = document.querySelector(".nav-toggle");
  var nav = document.querySelector("#site-nav");
  if (!button || !nav) return;

  button.addEventListener("click", function () {
    var open = nav.classList.toggle("is-open");
    button.setAttribute("aria-expanded", open ? "true" : "false");
  });

  nav.addEventListener("click", function (event) {
    if (!event.target.closest("a")) return;
    nav.classList.remove("is-open");
    button.setAttribute("aria-expanded", "false");
  });

  document.addEventListener("keydown", function (event) {
    if (event.key !== "Escape") return;
    nav.classList.remove("is-open");
    button.setAttribute("aria-expanded", "false");
  });
})();
