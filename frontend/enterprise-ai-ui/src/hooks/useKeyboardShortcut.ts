export default function useKeyboardShortcut(
callback:()=>void
){

window.addEventListener(
"keydown",
(e)=>{

if(e.ctrlKey && e.key==="k")
{
callback();
}

});


} 