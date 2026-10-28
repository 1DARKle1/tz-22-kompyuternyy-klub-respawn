(function () {
  var book = document.querySelector("#zone-book");
  if (!book) return;
  document.querySelectorAll("[data-zone-pick]").forEach(function (card) {
    card.addEventListener("click", function () {
      var picked = card.getAttribute("data-zone-pick");
      book.href = "contacts.html?lead_type=booking&zone=" + encodeURIComponent(picked);
    });
  });
})();