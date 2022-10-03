import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from "axios";
import UserView from "./components/UserListView";


function App() {

    const [userList, setUserList] = useState([{}]);
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [age, setAge] = useState("");
    const [company, setCompany] = useState("");
    const [joinDate, setJoinDate] = useState("");
    const [jobTitle, setJobTitle] = useState("");
    const [gender, setGender] = useState("");
    const [salary, setSalary] = useState("");

    // Take all users
    useEffect(() => {
        axios.get("http://web-app.com/api/users/")
            .then(res => {
                setUserList(res.data)
            })
    });

    // Post the user
    const addUserHandler = () => {
        axios.post(
            "http://web-app.com/api/users/",
            {
                "name": name,
                "email": email,
                "age": age,
                "company": company,
                "joinDate": joinDate,
                "jobTitle": jobTitle,
                "gender": gender,
                "salary": salary
            }
        ).then(res => console.log(res))
    };





    return (
        <div className="App list-group-item justify-content-center align-items-center mx-auto"
             style={{
                 "width": "400px",
                 "backgroundColor": "white",
                 "marginTop": "15px"
             }}>
            <h1 className="card text-white bg-primary mb-1"
                styleName="max-width: 20rem">
                User manager
            </h1>
            <h6 className="card text-white bg-primary mb-3">
                FastAPI - React - MongoDB
            </h6>
            <div className="card-body">
                <h5 className="card text-white bg-dark mb-3">
                    Add New User
                </h5>
                <span className="card-text">
                        <input className="mb-2 form-control titleIn"
                               placeholder="Full Name"
                               onChange={event => setName(event.target.value)}
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Email"
                               type="email"
                               onChange={event => setEmail(event.target.value)}
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Age"
                               type="number"
                               onChange={event => setAge(event.target.value)}
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Company"
                               onChange={event => setCompany(event.target.value)}
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Join date"
                               type="datetime-local"
                               onChange={event => setJoinDate(event.target.value)}
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Job title"
                               onChange={event => setJobTitle(event.target.value)}
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Gender"
                               onChange={event => setGender(event.target.value)}
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Salary"
                               type="number"
                               onChange={event => setSalary(event.target.value)}
                        />
                        <button className="btn btn-outline-primary mx-2 mb-3"
                                style={{
                                    "borderRadius": "50px",
                                    "font-weight": "bold"
                                }}
                                onClick={addUserHandler}
                        >
                            Add User
                        </button>
                    </span>
                <h5 className="card text-white bg-dark mb-3">
                    All Users
                </h5>
                <div>
                   <UserView userList={userList} />
                </div>
            </div>
            <h6 className="card text-dark bg-warning py-1 mb-0">
                Copyright 2022, All right reserved &copy;
            </h6>
        </div>
    );
}

export default App;
