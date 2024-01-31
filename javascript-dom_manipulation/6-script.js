const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('response not ok');
    }
    return response.json();
  })
  .then(data => {
    const characterElement = document.getElementById('character');
    characterElement.textContent = data.name;
  });
