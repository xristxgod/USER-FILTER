async function getAllUser() {
    const response = await fetch('http://web-app.com/api/users/');
    const users = await response.json();

    console.log(users)
    users.forEach(user => usersToHTML(user));
}


window.addEventListener('DOMContentLoaded', getAllUser);


function usersToHTML({id, name, email, age, company, joinDate, jobTitle, gender, salary}) {
    const usersList = document.getElementById("user");

    usersList.insertAdjacentHTML(
        "beforebegin", `
        <div class="form-check" id="user${id}">
            <label class="form-check-label">
                ${name}
            </label>
            <button type="button" class="btn-close"> </button>
        </div>
     `);
}