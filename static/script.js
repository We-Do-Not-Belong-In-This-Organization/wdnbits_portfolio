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

// ------------------- QUEUE PAGE ENQUEUE ANIMATION -------------------
  const queueBox = document.querySelector('.queue-box');
  if (queueBox) {
    queueBox.scrollTop = queueBox.scrollHeight;
  }
