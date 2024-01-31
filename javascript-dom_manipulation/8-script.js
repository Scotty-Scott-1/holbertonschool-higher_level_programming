document.addEventListener('DOMContentLoaded', function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('response not ok');
      }
      return response.json();
    })
    .then(data => {
      const textElement = document.getElementById('hello');
      textElement.textContent = data.hello;
    });
});
