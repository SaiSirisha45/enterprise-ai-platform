interface Props {
  name:string;
  status:"Running"|"Failed"|"Completed";
}


export default function WorkflowCard({
  name,
  status
}:Props){

return(

<div
style={{
background:"#fff",
padding:"20px",
borderRadius:"12px",
marginBottom:"15px",
boxShadow:"0 2px 8px rgba(0,0,0,0.08)",
display:"flex",
justifyContent:"space-between"
}}
>

<div>

<h3>{name}</h3>

<p
style={{
color:
status==="Running"
?"green"
:
status==="Failed"
?"red"
:"blue"
}}
>
● {status}
</p>

</div>


<div>

<button
style={{
marginRight:"10px",
padding:"8px",
background:"#2563eb",
color:"#fff",
border:"none",
borderRadius:"6px"
}}
>
Retry
</button>


<button
style={{
padding:"8px",
background:"#dc2626",
color:"#fff",
border:"none",
borderRadius:"6px"
}}
>
Cancel
</button>


</div>


</div>

)

} 