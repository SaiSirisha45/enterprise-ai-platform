import UserCard from "./UserCard";


export default function UserList(){


const users=[

{
name:"Admin User",
email:"admin@company.com",
role:"Admin"
},

{
name:"HR Manager",
email:"hr@company.com",
role:"HR"
},

{
name:"Employee",
email:"employee@company.com",
role:"User"
}

];


return(

<div>


{
users.map(user=>(

<UserCard

key={user.email}

name={user.name}

email={user.email}

role={user.role}

/>


))

}


</div>


)

} 