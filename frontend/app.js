async function getAllUser() {
    const response = await fetch('http://web-app.com/api/users/');
    const user = await response.json();

    console.log(response);
}

window.addEventListener('DOMContentLoaded', getAllUser);