// assets/js/masthead.js
document.addEventListener('DOMContentLoaded', function() {
  const toggleButton = document.querySelector('.greedy-nav button');
  const visibleLinks = document.querySelector('.visible-links');
  const hiddenLinks = document.querySelector('.hidden-links');

  if (toggleButton && visibleLinks && hiddenLinks) {
    toggleButton.addEventListener('click', function() {
      this.classList.toggle('active');
      visibleLinks.classList.toggle('active');
      hiddenLinks.classList.toggle('active');
    });
  }
});