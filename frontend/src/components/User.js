import axios from "axios";
import React from "react";

function UserItem(props) {
    const deleteUserHandler = (name) => {
        axios.delete("http://web-app.com/api/users/${id}")
            .then(res => console.log(res.data))
    };
    return(
        <div>
            <p>
                <span style={{fontWeight: "bold, underline" }}>
                    {props.user.name}
                </span>
                <button onClick={() => deleteUserHandler(props.user.id)}
                        className="btn btn-outline-danger my-2 mx-2"
                        style={{'borderRadius': "50px"}}
                >
                    X
                </button>
                <hr></hr>
            </p>
        </div>
    )
}

export default UserItem;