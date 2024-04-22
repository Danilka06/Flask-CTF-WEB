const button_login = document.getElementById('submit');
const username_field = document.getElementById("username");
const password_field = document.getElementById("password");

button_submit.addEventListener('click', async _ => {
  try {
    // creating request
    fetch('http://127.0.0.1:5000/api/check',
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: username_field.value
        password: password_field.value
      })  // json with answer from input field
    })
    .then(response => response.json())
    .then(data => response_text.innerText = data["status"])

  // catching all errorsd
  } catch(err) {
    console.error(`Error: ${err}`);
  }
});
