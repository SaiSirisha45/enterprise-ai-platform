export default function AnalyticsChart(){

const data=[
{
name:"Mon",
value:120
},
{
name:"Tue",
value:180
},
{
name:"Wed",
value:240
},
{
name:"Thu",
value:300
},
{
name:"Fri",
value:400
}
];


return(

<div
style={{
background:"#fff",
padding:"20px",
borderRadius:"12px",
marginTop:"20px"
}}
>


<h2>
AI Queries Weekly
</h2>


{
data.map(item=>(

<div key={item.name}>

<p>
{item.name}
</p>


<div
style={{
height:"20px",
width:`${item.value}px`,
background:"#2563eb",
borderRadius:"5px"
}}
>


</div>


</div>

))
}


</div>

)

} 