interface Props{

name:string;
email:string;
role:string;

}


export default function UserCard({
name,
email,
role
}:Props){


return(

<div

style={{

background:"#fff",
padding:"20px",
borderRadius:"12px",
marginBottom:"15px",
display:"flex",
justifyContent:"space-between",
boxShadow:"0 2px 8px rgba(0,0,0,0.08)"

}}

>


<div>

<h3>
{name}
</h3>


<p>
{email}
</p>


<p>
Role : {role}
</p>


</div>


<button

style={{
background:"#dc2626",
color:"#fff",
border:"none",
padding:"8px 15px",
borderRadius:"6px"
}}

>
Delete
</button>


</div>


)

} 