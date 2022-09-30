async function getAllUser() {
//    const response = await fetch('https://jsonplaceholder.typicode.com/todos/');
    const response = await fetch('http://localhost:8000/api/users/');
    const user = await response.json();

    console.log(response);
}

window.addEventListener('DOMContentLoaded', getAllUser);