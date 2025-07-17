document.addEventListener('DOMContentLoaded', function() {
  const urlsToggle = document.querySelector('.author__urls-toggle');
  const urls = document.querySelector('.author__urls');

  if (urlsToggle && urls) {
    urlsToggle.addEventListener('click', function() {
      urls.classList.toggle('active');
    });
  }
});