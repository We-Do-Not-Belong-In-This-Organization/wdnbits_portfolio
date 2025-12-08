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
const grid = document.querySelector(".grid");

characters.forEach(char => {
  let leftImg, rightImg;

  char.addEventListener("mouseenter", () => {
    if (!grid) return;

    if (leftImg) leftImg.remove();
    if (rightImg) rightImg.remove();

    leftImg = document.createElement("img");
    leftImg.src = `/static/images/${char.dataset.left}`;
    leftImg.className = "side-image left-side";

    rightImg = document.createElement("img");
    rightImg.src = `/static/images/${char.dataset.right}`;
    rightImg.className = "side-image right-side";

    grid.appendChild(leftImg);
    grid.appendChild(rightImg);

    requestAnimationFrame(() => {
      leftImg.classList.add("show");
      rightImg.classList.add("show");
    });
  });

  char.addEventListener("mouseleave", () => {
    if (!leftImg || !rightImg) return;

    leftImg.classList.remove("show");
    rightImg.classList.remove("show");

    setTimeout(() => {
      leftImg.remove();
      rightImg.remove();
    }, 500);
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
const tips = [
  'The "WDNBITS" name was founded by Jayvee',
  "If you're reading this, tag your tropa!",
  "Hassan is the youngest in the WDNBITS group",
  "Eh naglapag ng tips",
  "Some tips are randomly given!",
  "Si Jed ay Bass Player",
  "Si Matt ay may 7 dogs",
  "Tag mo yung tropa mo!",
  ".--- .- -. ....... .-. ..- --.. --..\\n . .-.. .-.. ....... --- .-. --.- ..- .. .-",
  "3-I",
  "Did you know? WDNBITS stands for 'We Do Not Belong In This School'!",
  "Did you know? 'Ruzzel' in 'Jan Ruzzel Orquia' actually has 2 'L's! It's actually 'Ruzzell'!",
];

// Picks a random phrase
const randomTip = tips[Math.floor(Math.random() * tips.length)];

// Displayer CAPITAL P, Powerful to!
document.getElementById("randText").textContent = randomTip;
});

// ------------------- QUEUE PAGE ENQUEUE ANIMATION -------------------
const queueBox = document.querySelector('.queue-box');
if (queueBox) {
  queueBox.scrollTop = queueBox.scrollHeight;
}

// Auto-scroll deque box to bottom on page load
window.addEventListener('load', () => {
    const dequeBox = document.querySelector('.queue-box');
    if (dequeBox) {
        dequeBox.scrollTop = dequeBox.scrollHeight;
    }
});

