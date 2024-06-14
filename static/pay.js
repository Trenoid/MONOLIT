const cardNumber = document.getElementById("card-number");
const cardDate = document.getElementById("card-date");

cardNumber.addEventListener("input", (event) => {
  const valueLength = cardNumber.value;
  if (
    valueLength.length == 4 ||
    valueLength.length == 9 ||
    valueLength.length == 14
  ) {
    cardNumber.value += " ";
    return;
  }
});

cardDate.addEventListener("input", (event) => {
  const valueLength = cardDate.value;
  if (valueLength.length == 2) {
    cardDate.value += "/";
    return;
  }
  if (valueLength.length == 3 && event.data == null) {
    cardDate.value = "";
  }
});