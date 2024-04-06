
document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#input-form');

  document.querySelector('#input-form').addEventListener('submit', (event) => {
    const form = document.querySelector('#input-form');
    event.preventDefault();
    if (!form.checkValidity()) {
      event.stopPropagation();
      form.classList.add('was-validated');
    }
    else {
      const query = document.querySelector('#query').value;
      fetch('/query', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
      })
      .then(response => response.json())
      .then((data) => {
        document.querySelector('#sqlOutput').innerHTML = data.response;
      })
      .catch((error) => {
        console.error('Error:', error);
      });
      }
  });
});