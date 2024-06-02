const buttonCopy1 = document.getElementById("buttonCopy1");
const buttonCopy2 = document.getElementById("buttonCopy2");

const inputCopy1 = document.getElementById("inputCopy1");
const inputCopy2 = document.getElementById("inputCopy2");

buttonCopy1.addEventListener("click", (e) => {
  navigator.clipboard
    .writeText(inputCopy1.value)
    .then(() => {
      if (inputCopy1.value != "") {
        inputCopy1.style.border = "1px solid var(--color-accent)";
        setTimeout(() => {
          inputCopy1.style.border = "";
        }, 500);
      }
    })
    .catch((error) => {
      console.error(`Текст не скопирован ${error}`);
    });
});

buttonCopy2.addEventListener("click", (e) => {
  navigator.clipboard
    .writeText(inputCopy2.value)
    .then(() => {
      if (inputCopy2.value != "") {
        inputCopy2.style.border = "1px solid var(--color-accent)";
        setTimeout(() => {
          inputCopy2.style.border = "";
        }, 500);
      }
    })
    .catch((error) => {
      console.error(`Текст не скопирован ${error}`);
    });
});

const accountContainer = document.querySelector(".account");
const replyRow = document.querySelectorAll(".account__reply-row");

accountContainer.addEventListener("click", (e) => {
  const target = e.target.closest(".account__button-reply");
  if (!target) return;
  if (
    (target.closest(
      ".account__download__actions"
    ).nextElementSibling.style.opacity = 1)
  ) {
    target.closest(
      ".account__download__actions"
    ).nextElementSibling.style.opacity = 1;
  }
});