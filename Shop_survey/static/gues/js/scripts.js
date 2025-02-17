document.addEventListener("DOMContentLoaded", function() {
    const steps = document.querySelectorAll(".form-step");
    const nextBtns = document.querySelectorAll(".next");
    const prevBtns = document.querySelectorAll(".prev");
    const progressBar = document.getElementById("progress-bar");

    let currentStep = 0;

    function updateForm() {
        steps.forEach((step, index) => {
            step.classList.toggle("active", index === currentStep);
        });
        progressBar.style.width = `${((currentStep + 1) / steps.length) * 100}%`;
    }

    nextBtns.forEach(button => {
        button.addEventListener("click", () => {
            if (currentStep < steps.length - 1) {
                currentStep++;
                updateForm();
            }
        });
    });

    prevBtns.forEach(button => {
        button.addEventListener("click", () => {
            if (currentStep > 0) {
                currentStep--;
                updateForm();
            }
        });
    });

    document.getElementById("surveyForm").addEventListener("submit", function(event) {
        event.preventDefault();
        alert("Thank you for your feedback!");
    });
});