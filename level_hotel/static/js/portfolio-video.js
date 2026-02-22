document.addEventListener("DOMContentLoaded", () => {
  const video = document.getElementById("portfolioVideo");
  const button = document.getElementById("playButton");

  // If the portfolio section isn't on this page, do nothing
  if (!video || !button) return;

  const icon = button.querySelector("i");
  if (!icon) return;

  const setPlayIcon = () => {
    icon.classList.remove("fa-pause-circle");
    icon.classList.add("fa-play-circle");
  };

  const setPauseIcon = () => {
    icon.classList.remove("fa-play-circle");
    icon.classList.add("fa-pause-circle");
  };

  button.addEventListener("click", () => {
    if (video.paused) {
      video.play();
      setPauseIcon();
    } else {
      video.pause();
      setPlayIcon();
    }
  });

  video.addEventListener("play", setPauseIcon);
  video.addEventListener("pause", setPlayIcon);
});
