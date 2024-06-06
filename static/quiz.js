const quizesContainer = document.querySelector(".quiz-section");

if (quizesContainer) {
  quizesContainer.addEventListener("click", (event) => {
    const target = event.target;
    if (!target.closest(".form-quistions__actions")) return;
    let currentQuiz = target.closest(".quiz");

    if (!currentQuiz) return;

    if (
      target.closest(".button-continue") &&
      currentQuiz.nextElementSibling &&
      currentQuiz.nextElementSibling.classList.contains("quiz")
    ) {
      currentQuiz.nextElementSibling.hidden = false;
      currentQuiz.hidden = true;
    } else if (
      target.closest(".button-back") &&
      currentQuiz.previousElementSibling &&
      currentQuiz.previousElementSibling.classList.contains("quiz")
    ) {
      currentQuiz.previousElementSibling.hidden = false;
      currentQuiz.hidden = true;
    }
  });
} else {
  console.error("Element with class .quiz-section not found");
}