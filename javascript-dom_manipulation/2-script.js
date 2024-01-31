document.getElementById('red_header').addEventListener('click', function () {
  const elementHeader = document.querySelector('header');
  if (elementHeader) {
    elementHeader.classList.add('red');
  }
});
