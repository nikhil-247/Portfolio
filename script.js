(() => {
  const filters = Array.from(document.querySelectorAll(".filter"));
  const cards = Array.from(document.querySelectorAll(".project-card"));
  const emptyState = document.getElementById("empty-state");
  const year = document.getElementById("year");

  if (year) year.textContent = String(new Date().getFullYear());

  function applyFilter(filter) {
    let visible = 0;
    for (const card of cards) {
      const categories = (card.getAttribute("data-categories") || "").split(/\s+/);
      const matches = filter === "all" || categories.includes(filter);
      card.hidden = !matches;
      if (matches) visible += 1;
    }
    if (emptyState) emptyState.hidden = visible !== 0;

    for (const button of filters) {
      const active = button.dataset.filter === filter;
      button.classList.toggle("active", active);
      button.setAttribute("aria-pressed", String(active));
    }
  }

  for (const button of filters) {
    button.addEventListener("click", () => applyFilter(button.dataset.filter || "all"));
  }
})();
