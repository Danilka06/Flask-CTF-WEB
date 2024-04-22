console.log('123')
const button_login = document.getElementById('login_button');
const login_field = document.getElementById("login");
const password_field = document.getElementById("password");
const error_field = document.getElementById("error_field");

button_login.addEventListener('click', async _ => {
  try {
    // creating request
    fetch('http://127.0.0.1:5000/api/login',
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        login: login_field.value,
        password: password_field.value,
      })  // json with answer from input field
    })
    .then(response => response.json())
    .then(data => (data["status"] == "correct") ? (window.location.replace("http://127.0.0.1:5000/")) : (error_field.innerText = data["status"]))

  // catching all errors
  } catch(err) {
    console.error(`Error: ${err}`);
  }
});
