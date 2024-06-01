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
// body.addEventListener("click", (event) => {
//   const target = event.target.closest("[data-action]");
//   if (!target || target.closest(".authorization__button--active")) return;
//   // let buttons = target.closest(".authorization__buttons");
//   if (
//     target.dataset.action === "registr" &&
//     !target.closest("authorization__button--active")
//   ) {
//     target
//       .closest(".authorization__buttons")
//       .lastElementChild.classList.remove("authorization__button--active");
//     console.log(target.closest(".authorization__buttons"));
//     // buttons.children[1].classList.remove("authorization__button--active");
//     target.classList.add("authorization__button--active");
//     login.hidden = true;
//     registr.hidden = false;
//     return;
//   }
//   if (
//     target.dataset.action === "entrance" &&
//     !target.closest("authorization__button--active")
//   ) {
//     target.classList.add("authorization__button--active");
//     target
//       .closest(".authorization__buttons")
//       .firstElementChild.classList.remove("authorization__button--active");
//     // buttons.children[0].classList.remove("authorization__button--active");

    login.hidden = !login.hidden;
    registr.hidden = !registr.hidden;
  }
});
//     login.hidden = false;
//     registr.hidden = true;
//     return;
//   }
// });

// body.addEventListener("click", (event) => {
//   const target = event.target.closest("[data-action]");
//   if (!target || target.closest(".authorization__button--active")) return;
//   if (target.dataset.action === "registr") {
//     target.nextElementSibling.classList.remove("authorization__button--active");
//     target.classList.add("authorization__button--active");
//     registr.hidden = false;
//     login.hidden = true;
//     target = null;
//     return;
//   }
//   if (target.dataset.action === "entrance") {
//     target.previousElementSibling.classList.remove(
//       "authorization__button--active"
//     );
//     target.classList.add("authorization__button--active");
//     registr.hidden = true;
//     login.hidden = false;
//     target = null;
//     return;
//   }
// });