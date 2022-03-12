const year = document.getElementById('year');
const showYear = new Date().getFullYear();
year.innerHTML = showYear;

let input = document.getElementById('id_title');

if (input) {
  input.focus();
  input.setSelectionRange(input.value.length, input.value.length);
}
