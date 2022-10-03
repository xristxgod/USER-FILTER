import UserItem from "./User";


function UserView(props) {
    return (
        <div>
            <ul>
                {props.userList.map(user => <UserItem user={user} />)}
            </ul>
        </div>
    )
}

export default UserView;