import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from "axios";


function App() {
    return (
        <div className="App">

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
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Email"
                               type="email"
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Age"
                               type="number"
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Company"
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Join date"
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Job title"
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Gender"
                        />
                        <input className="mb-2 form-control titleIn"
                               placeholder="Salary"
                               type="number"
                        />
                    </span>
                </div>
            </div>
        </div>
    );
}

export default App;
