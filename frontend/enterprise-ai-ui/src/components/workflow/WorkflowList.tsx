import WorkflowCard from "./WorkflowCard";


export default function WorkflowList(){

const workflows=[

{
name:"Leave Approval Workflow",
status:"Running" as const
},

{
name:"Payroll Processing Workflow",
status:"Completed" as const
},

{
name:"Employee Onboarding Workflow",
status:"Failed" as const
}

];


return(

<div>

{
workflows.map((workflow)=>(

<WorkflowCard
key={workflow.name}
name={workflow.name}
status={workflow.status}
/>

))
}

</div>

)

} 