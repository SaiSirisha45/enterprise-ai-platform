interface Props{
title:string;
enabled:boolean;
}


export default function SettingsCard({
title,
enabled
}:Props){

return(

<div
style={{
background:"#fff",
padding:"20px",
borderRadius:"12px",
marginTop:"15px"
}}
>

<h3>{title}</h3>

<p>
Status :
{enabled ? " Enabled":" Disabled"}
</p>


<button>
Toggle
</button>


</div>

)

} 