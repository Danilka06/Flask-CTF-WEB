document.querySelector('.toggle-btn').addEventListener('click', function() {
    const sidebar = document.querySelector('.sidebar');
    if (sidebar.style.width === '200px') {
        sidebar.style.width = '0';
    } else {
        sidebar.style.width = '200px';
    }
});

const button_submit = document.getElementById('submit');
const answer_text = document.getElementById("answer");
const response_text = document.getElementById("response_text");

button_submit.addEventListener('click', async _ => {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/check',
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({answer: answer_text.value})
    });
    console.log('Completed!', response);
    if (response.status == 200) response_text.innerText = 'correct'
    else response_text.innerText = 'incorrect';
    response_text.innerText = response.status;
  } catch(err) {
    console.error(`Error: ${err}`);
  }
});
