document.getElementById('toggle_header').addEventListener('click', function () {
  const elementHeader = document.querySelector('header');
  if (elementHeader.classList.contains('green')) {
    elementHeader.classList.add('red');
    elementHeader.classList.remove('green');
  } else {
    elementHeader.classList.add('green');
    elementHeader.classList.remove('red');
  }
});
