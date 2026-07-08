import Sidebar from "../components/layouts/Sidebar";
import Topbar from "../components/layouts/Topbar";
import { Outlet } from "react-router-dom";


export default function AppLayout(){

return(

<div className="flex">

<Sidebar/>

<div className="flex-1">

<Topbar/>

<Outlet/>

</div>

</div>

)

} 