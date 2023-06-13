document.forms[0].oninput = () => {
  // ищем элемент <select>
  const select = document.querySelector('select')
  // ищем элемент <div class="fruits">
  const fruits = document.querySelector('.fruits');
  // ищем элементы <option>
  const options = select.querySelectorAll('option');
  // собираем значения
  const values = [...options].map(option => option.value);
  // Удаляем все классы из списка классов fruits
  for (const item of values) {
    fruits.classList.remove(item);
  }
  // Добавляем класс fruits равную значению value
  //            из выбранного элемента в <select>
  fruits.classList.add(select.value);
}