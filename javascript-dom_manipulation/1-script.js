document.getElementById('red_header').addEventListener('click', function () {
  const elementHeader = document.querySelector('header');
  if (elementHeader) {
    elementHeader.style.color = '#FF0000';
  }
});
