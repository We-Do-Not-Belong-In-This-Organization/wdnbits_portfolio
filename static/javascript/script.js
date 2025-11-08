document.addEventListener("DOMContentLoaded", () => {
  const startButton = document.getElementById("startButton");
  const body = document.body;

  startButton.addEventListener("click", () => {
    // Apply zoom + fade
    body.classList.add("zoom-fade");

    // Hide button immediately
    startButton.style.display = "none";

    // Redirect slightly before animation ends
    setTimeout(() => {
      window.location.href = "/profile";
    }, 1400); // match CSS duration
  });
});