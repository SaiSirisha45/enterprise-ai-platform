export default function NotificationPanel(){

const notifications=[

"New document uploaded",
"Workflow completed",
"AI Agent started"

];


return(

<div>

<h3>
Notifications
</h3>


{
notifications.map(n=>(

<p key={n}>
🔔 {n}
</p>

))
}


</div>

)

} 