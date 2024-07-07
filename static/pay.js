const cardNumber = document.getElementById("card-number");
const cardDate = document.getElementById("card-date");

cardNumber.addEventListener("input", (event) => {
  let value = cardNumber.value.replace(/\D/g, '');
  if (event.inputType === 'deleteContentBackward') {
    // This handles the backspace or delete key
    cardNumber.value = value.replace(/(\d{1,4})(?=\d)/g, '$1 ').trim();
    return;
  }
  cardNumber.value = value.replace(/(\d{4})(?=\d)/g, '$1 ').trim();
});

cardDate.addEventListener("input", (event) => {
  let value = cardDate.value.replace(/\D/g, '');
  if (event.inputType === 'deleteContentBackward') {
    // This handles the backspace or delete key
    cardDate.value = value.replace(/(\d{2})(?=\d)/g, '$1/').substring(0, 7);
    return;
  }
  if (value.length > 2) {
    value = value.replace(/(\d{2})(\d{4})/, '$1/$2');
  }
  cardDate.value = value;
});
