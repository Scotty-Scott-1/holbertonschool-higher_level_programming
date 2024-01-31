const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('response not ok');
    }
    return response.json();
  })
  .then(data => {
    const test = document.getElementById('list_movies');
    const myResult = (data.results);
    const myArray = [];
    for (let i = 0; i < myResult.length; i++) {
      const name = myResult[i].title;
      myArray.push(name);
    }
    for (const title of myArray) {
      const listItem = document.createElement('li');
      listItem.textContent = title;
      test.appendChild(listItem);
    }
  });
