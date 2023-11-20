import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./index.css";
import "./form-table.css"
import { mockData } from "../../data/mock-data";

const Form = () =>{
    const [forms, setFormList] = useState([]);
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();
    
    useEffect(() =>{
        setLoading(true);
        fetch("http://localhost:8000/forms",{method:"GET"})
            .then(response => response.json())
            .then(data => {
                console.log(data)
                setFormList(data);
            })
            .catch((e)=>{
                console.debug(e);
            })
            .finally(()=>{
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
        <div className="form-container">
        <div className="welcome-container">
            <div className="title-container">
                <h2>Automated Tools - Home Page</h2>
                <div style={{padding : "10px 0"}}>You can click create button here to submit the form.</div>
                <div style={{padding : "10px 0"}}>All the submitted data will be shown below.</div>
            </div>
            <div className="button-container">
                {/* <button className="back-button" onClick={()=>navigate(-1)}>Back</button> */}
                <button className="back-button" onClick={()=>{
                    if(!forms || (forms && forms.length === 0)){
                        setFormList(mockData);
                    }else{
                        setFormList([]);
                    }
                }}>{(!forms || (forms && forms.length === 0))?"Mock":"Undo"}</button>
                <button className="create-button" onClick={()=>navigate("/form_input")}>Create</button>
            </div>
        </div>
            <table border={1} className="form-table">
            <tr className="table-header-rows">
                <th>Name</th>
                <th>Email</th>
                <th>Message</th>
                <th>Edit</th>
                <th>Delete</th>
            </tr>
            {forms && forms.map((item,i) =>(
                <tr className={`${i % 2 === 0?"row form-table-odd":"row"}`}>
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