import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
const Form =() =>{
    const [forms, setFormList] = useState([]);
    const [loading, setLoading] = useState(false);
    useEffect(() =>{
        setLoading(true);
        fetch("http://localhost:8000/forms",{method:"GET"})
            .then(response => response.json())
            .then(data => {
                console.log(data)
                setFormList(data);
                setLoading(false);
            })
    }, [])
    if (loading) {
        return <p>Loading...</p>;
    }
    async function handleDelete(id){
        await fetch("http://localhost:8000/forms/"+id,
            {method:"DELETE"}).then(res=> {
                if(res.ok){
                    setLoading(false);
                    window.location.reload();
                }else{
                    console.log(res);
                }
            })
            .catch(error=> console.log(error))
    }


    return (
        <>
        <div>
            
        <Link to="/form_input"><button>Create</button></Link>
            <table border={1}>
            <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Message</th>
                <th>Edit</th>
                <th>Delete</th>
            </tr>
            {forms && forms.map(item =>(
                <tr>
                    <td>{item.name}</td>
                    <td>{item.email}</td>
                    <td>{item.message}</td>
                    <td><Link to={"/form_input/?id="+item.id}><button>Edit</button></Link></td>
                    <td><button onClick={()=>handleDelete(item.id)}>Delete</button></td>
                </tr>
            ))}
            </table>
        </div>
        </>
    );
}

export default Form;