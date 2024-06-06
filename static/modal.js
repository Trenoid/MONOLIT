const modalTemplate = `<div class="modal">
<div class="modal__wrapper">
  <div class="modal__button-wrapper">
    <button class="modal__button" data-action="modal-close">X</button>
  </div>
  <div class="modal__content">
    <h2 class="modal__title">%title%</h2>
    <p class="modal__discr">
      %discr%
    </p>
  </div>
</div>
</div>`;

const wrapper = document.querySelector(".wrapper");
const overlay = document.getElementById("overlay");

if (wrapper && overlay) {
  wrapper.addEventListener("click", (event) => {
    const target = event.target.closest("[data-tooltip='open']");
    if (!target) return;
    const currentItem = target.closest(".structure__item");
    const currentTitle = currentItem.firstElementChild;
    const currentDiscr = currentItem.dataset.discr;
    const replaceTitle = modalTemplate.replace("%title%", currentTitle.textContent);
    const replaceDiscr = replaceTitle.replace("%discr%", currentDiscr);

    overlay.classList.add("active");
    wrapper.insertAdjacentHTML("beforeend", replaceDiscr);
  });

  document.body.addEventListener("click", (e) => {
    const target = e.target.closest("[data-action='modal-close']");

    if (target) {
      const modal = target.closest(".modal");
      modal.remove();
      overlay.classList.remove("active");
    } else if (e.target.classList.contains("overlay")) {
      overlay.classList.remove("active");
      const modal = document.querySelector(".modal");
      if (modal) {
        modal.remove();
      }
    }
  });
}


