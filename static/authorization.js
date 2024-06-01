const body = document.body;

let authorizationContainer = document.querySelector(".authorization-section");
const login = document.getElementById("login");
const registr = document.getElementById("registr");

body.addEventListener("click", (event) => {
  const target = event.target.closest("[data-action]");
  if (!target || target.classList.contains("authorization__button--active"))
    return;
  const buttons = target.closest(".authorization__buttons");
  if (
    target.dataset.action === "registr" &&
    !target.classList.contains("authorization__button--active")
  ) {
    buttons.children[1].classList.remove("authorization__button--active");
    target.classList.add("authorization__button--active");
    login.hidden = !login.hidden;
    registr.hidden = !registr.hidden;
  }
  if (
    target.dataset.action === "entrance" &&
    !target.classList.contains("authorization__button--active")
  ) {
    target.classList.add("authorization__button--active");
    buttons.children[0].classList.remove("authorization__button--active");

    login.hidden = !login.hidden;
    registr.hidden = !registr.hidden;
  }
});