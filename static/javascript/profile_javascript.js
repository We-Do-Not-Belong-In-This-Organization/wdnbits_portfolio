window.addEventListener('load', () => {
  const loadingScreen = document.querySelector('.loading-screen');
  setTimeout(() => {
    loadingScreen.classList.add('hidden');
    setTimeout(() => loadingScreen.remove(), 1000); // remove from DOM after fade
  }, 2000); // stays for 2 seconds before fade
});

document.addEventListener("DOMContentLoaded", () => {
  const characters = document.querySelectorAll(".character");

  characters.forEach(char => {
    let leftImg, rightImg;

    char.addEventListener("mouseenter", () => {
      // Create left image
      leftImg = document.createElement("img");
      leftImg.src = `/static/images/${char.dataset.left}`;
      leftImg.className = "side-image left-side";
      leftImg.style.position = "absolute";
      leftImg.style.top = "50%";
      leftImg.style.left = "-150px";
      leftImg.style.transform = "translateY(-50%)";
      leftImg.style.transition = "all 0.5s ease";
      leftImg.style.zIndex = 10;
      document.body.appendChild(leftImg);

      // Create right image
      rightImg = document.createElement("img");
      rightImg.src = `/static/images/${char.dataset.right}`;
      rightImg.className = "side-image right-side";
      rightImg.style.position = "absolute";
      rightImg.style.top = "50%";
      rightImg.style.right = "-150px";
      rightImg.style.transform = "translateY(-50%)";
      rightImg.style.transition = "all 0.5s ease";
      rightImg.style.zIndex = 10;
      document.body.appendChild(rightImg);

      // Force reflow then slide in
      requestAnimationFrame(() => {
        leftImg.style.left = "10px";
        rightImg.style.right = "10px";
      });
    });

    char.addEventListener("mouseleave", () => {
      // Slide out and remove
      if (leftImg && rightImg) {
        leftImg.style.left = "-150px";
        rightImg.style.right = "-150px";

        setTimeout(() => {
          leftImg.remove();
          rightImg.remove();
        }, 500); // matches transition
      }
    });
  });
});