import { useEffect, useState } from "react";
import { useLocation, Link } from "react-router-dom";
const FormInput =() =>{
    const [formData, setFormData] = useState({name: "",email: "",message: ""});
    const [submitted, setSubmitted] = useState(false);
    const [loading, setLoading] = useState(false);
    const [id, setId] = useState(new URLSearchParams(useLocation().search).get('id'));

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData((prevFormData) => ({ ...prevFormData, [name]: value }));
    };

    useEffect(() =>{
        if(id){
            setLoading(true);
            fetch("http://localhost:8000/forms/"+id,{method:"GET"})
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    setFormData({name:data.name,email:data.email,message:data.message})
                    setLoading(false);
                })
        }
    }, [])
    if (loading) {
        return <p>Loading...</p>;
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
        if(id){
            await fetch("http://localhost:8000/forms/"+id,
            {method:"PATCH",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body:JSON.stringify(formData)
            }).then(res=> {
                if(res.ok){
                    setSubmitted(true);
                }else{
                    console.log(res);
                }
            })
            .catch(error=> console.log(error))
        }else{
            await fetch("http://localhost:8000/forms",
            {method:"POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body:JSON.stringify(formData)
            }).then(res=> {
                if(res.ok){
                    setSubmitted(true);
                }else{
                    console.log(res);
                }
            })
            .catch(error=> console.log(error))
        }
        //alert(`Name: ${formData.name}, Email: ${formData.email}, Message: ${formData.message}`);
    };


    return (

        <div>
        <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name:</label><br/>
        <input type="text" id="name" name="name" value={formData.name} onChange={handleChange}/><br/>

        <label htmlFor="email">Email:</label><br/>
        <input type="email" id="email" name="email" value={formData.email} onChange={handleChange}/><br/>

        <label htmlFor="message">Message:</label><br/>
        <textarea id="message" name="message" value={formData.message} onChange={handleChange}/><br/>

        <button type="submit">Submit</button>
        </form>
        {submitted && (
            <div>
            <h2>Submitted Data:</h2>
            <p>Name: {formData.name}</p>
            <p>Email: {formData.email}</p>
            <p>Message: {formData.message}</p>
            </div>
        )}
        <Link to="/">Back</Link>
        </div>
    );
}

export default FormInput;