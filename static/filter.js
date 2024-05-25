const filterButton = document.querySelector("[data-action='filter-open']");
const filterForm = document.getElementById("filter-form");

filterButton.addEventListener("click", (event) => {
  filterForm.hidden = !filterForm.hidden;
});