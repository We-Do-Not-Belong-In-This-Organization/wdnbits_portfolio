document.addEventListener("DOMContentLoaded", () => {

  // ------------------- PRESS ANY BUTTON -------------------
  const startButton = document.getElementById("startButton");
  const body = document.body;

  function startGame() {
    body.classList.add("zoom-fade");
    startButton.style.display = "none";
    setTimeout(() => {
      window.location.href = "/profile";
    }, 1400);
  }

  if (startButton) {
    startButton.addEventListener("click", startGame);
    document.addEventListener("keydown", startGame); // any key also works
  }

// ------------------- PROFILE HOVER SIDE IMAGES -------------------
const characters = document.querySelectorAll(".character");

characters.forEach(char => {
  let leftImg, rightImg;

  char.addEventListener("mouseenter", () => {
    const grid = document.querySelector(".grid"); // append relative to grid

    leftImg = document.createElement("img");
    leftImg.src = `/static/images/${char.dataset.left}`;
    leftImg.className = "side-image left-side";
    grid.appendChild(leftImg);

    rightImg = document.createElement("img");
    rightImg.src = `/static/images/${char.dataset.right}`;
    rightImg.className = "side-image right-side";
    grid.appendChild(rightImg);

    requestAnimationFrame(() => {
      leftImg.classList.add("show");
      rightImg.classList.add("show");
    });
  });

  char.addEventListener("mouseleave", () => {
    if (leftImg && rightImg) {
      leftImg.classList.remove("show");
      rightImg.classList.remove("show");

      setTimeout(() => {
        leftImg.remove();
        rightImg.remove();
      }, 500);
    }
  });
});

  // ------------------- LOADING SCREEN -------------------
  const loadingScreen = document.querySelector('.loading-screen');
  if (loadingScreen) {
    setTimeout(() => {
      loadingScreen.classList.add('hidden');
      setTimeout(() => loadingScreen.remove(), 1000);
    }, 2000);
  }

});

// Jan Ruzzel Easter Egg

document.addEventListener("DOMContentLoaded", () => {
  let inactivityTimer;
const flashImages = window.flashImages || [];

const flashImg = document.createElement("img");
flashImg.style.position = "fixed";
flashImg.style.top = "0";
flashImg.style.left = "0";
flashImg.style.width = "100%";
flashImg.style.height = "100%";
flashImg.style.objectFit = "cover";
flashImg.style.zIndex = "9999";
flashImg.style.display = "none";
flashImg.style.transition = "opacity 0.15s";
document.body.appendChild(flashImg);

function flashMultipleTimes(times = 5, interval = 400) {
  let count = 0;
    const flashInterval = setInterval(() => {
      if (count >= times) {
        clearInterval(flashInterval);
        return;
      }

      const randomImage =
        flashImages[Math.floor(Math.random() * flashImages.length)];
      flashImg.src = randomImage;
      flashImg.style.display = "block";
      flashImg.style.opacity = "1";

      new Audio(window.screamSound).play();

      setTimeout(() => {
        flashImg.style.opacity = "0";
        setTimeout(() => (flashImg.style.display = "none"), 150);
      }, 150);

      count++;
    }, interval);
  }

  function showRandomFlash() {
    if (flashImages.length === 0) return;
    flashMultipleTimes(6, 300); // 6 flashes every 300ms
  }

  function resetInactivityTimer() {
    clearTimeout(inactivityTimer);
    inactivityTimer = setTimeout(showRandomFlash, 15000); // 15 seconds
  }

  ["mousemove", "keydown", "click", "scroll"].forEach((event) =>
    document.addEventListener(event, resetInactivityTimer)
  );

  resetInactivityTimer();
});
