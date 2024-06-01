var pinContainer = document.querySelector(".pin-code");
console.log("There is " + pinContainer.length + " Pin Container on the page.");

pinContainer.addEventListener(
  "keyup",
  function (event) {
    var target = event.srcElement;

    var maxLength = parseInt(target.attributes["maxlength"].value, 10);
    var myLength = target.value.length;

    if (myLength >= maxLength) {
      var next = target;
      while ((next = next.nextElementSibling)) {
        if (next == null) break;
        if (next.tagName.toLowerCase() == "input") {
          next.focus();
          break;
        }
      }
    }

    if (myLength === 0) {
      var next = target;
      while ((next = next.previousElementSibling)) {
        if (next == null) break;
        if (next.tagName.toLowerCase() == "input") {
          next.focus();
          break;
        }
      }
    }
  },
  false
);

pinContainer.addEventListener(
  "keydown",
  function (event) {
    var target = event.srcElement;
    target.value = "";
  },
  false
);

// const recoveryFormButtons = document.querySelectorAll(".recovery__form-button");
// const recoveryTypeButton = document.getElementById("recovery-type");
// const formEmail = document.getElementById("recovery-email");
// const formPhone = document.getElementById("recovery-phone");

// recoveryTypeButton.addEventListener("click", (event) => {
//   const article = event.target.closest("article");
//   article.hidden = !article.hidden;
//   if ((recoveryFormButtons[0].firstElementChild.chicked = true)) {
//     formEmail.hidden = !formEmail.hidden;
//     return;
//   } else if ((recoveryFormButtons[1].firstElementChild.chicked = true)) {
//     formPhone.hidden = !formPhone.hidden;
//   }
// });