document.addEventListener("DOMContentLoaded", () => {
  // grid images
  const gridImgs = document.querySelectorAll(".box img");

  // the two side images already in your HTML
  const leftSide = document.querySelector(".side-image.left");
  const rightSide = document.querySelector(".side-image.right");

  if (!leftSide || !rightSide) {
    console.warn("Side images not found. Make sure .side-image.left and .side-image.right exist in HTML.");
    return;
  }

  // Helper to trigger animation (restarting if already animating)
  function trigger(sideEl, className) {
    // Remove any existing animation class to allow restarting
    sideEl.classList.remove(className);
    // Force reflow to restart animation
    void sideEl.offsetWidth;
    sideEl.classList.add(className);
  }

  gridImgs.forEach((img, idx) => {
    img.style.cursor = "pointer";
    img.addEventListener("click", (e) => {
    
      const src = img.getAttribute("src"); // ✅ safer than img.src
      if (!src) return;

      leftSide.src = src;
      rightSide.src = src;

      trigger(leftSide, "animate-side-left");
      trigger(rightSide, "animate-side-right");


      // Optional: after animation ends, clear src (keeps DOM tidy)
      const clearAfter = () => {
        leftSide.removeEventListener("animationend", clearAfter);
        rightSide.removeEventListener("animationend", clearAfter);
        // don't clear src immediately if you plan to keep it — only clear if you want
        // leftSide.src = "";
        // rightSide.src = "";
      };

      leftSide.addEventListener("animationend", clearAfter);
      rightSide.addEventListener("animationend", clearAfter);
    });
  });
});                               
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

