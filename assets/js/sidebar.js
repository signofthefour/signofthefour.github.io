
document.addEventListener('DOMContentLoaded', function() {
  const toggleButton = document.querySelector('.sidebar__toggle');
  const sidebar = document.querySelector('.sidebar');
  const overlay = document.querySelector('.sidebar__overlay');
  const urlsToggle = document.querySelector('.author__urls-toggle');
  const urls = document.querySelector('.author__urls');

  if (toggleButton && sidebar && overlay) {
    toggleButton.addEventListener('click', function() {
      sidebar.classList.toggle('active');
      overlay.classList.toggle('active');
      document.body.classList.toggle('overflow--hidden');
    });

    overlay.addEventListener('click', function() {
      sidebar.classList.remove('active');
      overlay.classList.remove('active');
      document.body.classList.remove('overflow--hidden');
      if (urls) urls.classList.remove('active');
    });
  }

  if (urlsToggle && urls) {
    urlsToggle.addEventListener('click', function() {
      urls.classList.toggle('active');
    });
  }
});
