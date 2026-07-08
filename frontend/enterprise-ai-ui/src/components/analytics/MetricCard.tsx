interface Props{

title:string;
value:string;

}


export default function MetricCard({
title,
value
}:Props){


return(

<div
style={{
background:"#fff",
padding:"20px",
borderRadius:"12px",
boxShadow:"0 2px 8px rgba(0,0,0,0.08)"
}}
>

<h3>{title}</h3>

<h1>
{value}
</h1>


</div>

)


} 