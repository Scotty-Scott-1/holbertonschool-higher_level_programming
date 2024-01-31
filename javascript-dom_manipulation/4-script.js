document.getElementById('add_item').addEventListener('click', function () {
  const elementList = document.querySelector('.my_list');
  const listItem = document.createElement('li');
  listItem.textContent = 'Item';
  elementList.appendChild(listItem);
});
