async function getAllUser() {
    const response = await fetch('http://web-app.com/api/users/');
    const users = await response.json();

    console.log(users)
    users.forEach(user => usersToHTML(user));
}


window.addEventListener('DOMContentLoaded', getAllUser);


function singleUser({id, name, email, age, company, joinDate, jobTitle, gender, salary}) {

    const user = document.getElementById("user")

    user.insertAdjacentHTML(
        "beforebegin",
    )

}


function usersToHTML({id, name}) {
    const usersList = document.getElementById("users");

    usersList.insertAdjacentHTML(
        "beforebegin", `
        <div class="col" id="${id}">
            <div class="card">
                <div class="card-body">
                    <a href=""><h5 class="card-title">${name}</h5></a>
                </div>
            </div>
        </div>
     `);
}