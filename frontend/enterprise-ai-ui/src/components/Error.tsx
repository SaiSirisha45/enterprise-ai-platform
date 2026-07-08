interface Props{
    message:string
}

export default function Error({message}:Props){

return(

<div>

<h2>Error</h2>

<p>{message}</p>

</div>

)

} 