import { useEffect, useState, useCallback } from "react";
import { useLocation, Link } from "react-router-dom";
import { validateEmail, validateName } from "../utils/validation-helper";
import "./FormInput.css";

const FormInput =() =>{
    const [formData, setFormData] = useState({name: "",email: "",message: ""});
    const [submitted, setSubmitted] = useState(false);
    const [loading, setLoading] = useState(false);
    const [id, setId] = useState(new URLSearchParams(useLocation().search).get('id'));
    const [errorMsg,setErrorMsg] = useState({});
    const [formSubmitErrMsg,setFormSubmitErrMsg] = useState("");

    console.log(errorMsg);

    const handleChange = (event) => {
        const { name, value } = event.target;
        if(errorMsg[name] && errorMsg[name] !== ""){
            setErrorMsg({
                ...errorMsg,
                [name]: ""
            })
        }
        setFormData((prevFormData) => ({ ...prevFormData, [name]: value }));
    };

    const validate = useCallback(()=>{
        if(Object.keys(errorMsg).length > 0 || Object.keys(formData).some((key)=>formData[key] === "")){
            return false;
        }
        return true;
    },[formData,errorMsg])

    const handleOnBlur = useCallback((e) => {
        const { name, value } = e.target;
        const message = `Please input correct ${name}`;
        switch(name){
            case "name":
                if(!validateName(value)){
                    setErrorMsg({
                        ...errorMsg,
                        [name]: message
                    })
                    return;
                }
                break;
            case "email":
                if(!validateEmail(value)){
                    setErrorMsg({
                        ...errorMsg,
                        [name]: message
                    })
                    return;
                }
                break;
            default:
                break;
        }
    },[errorMsg])

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
        if(!validate()){
            alert("Please make sure you fill in the correct information and submit again.")
            return;
        }
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

        <div className="form-input-container">
        <form onSubmit={handleSubmit}>
        <div className={`input-fields-container${errorMsg.name?" is-error":""}`}>
            <label htmlFor="name">Name:</label><br/>
            <input type="text" id="name" name="name" value={formData.name} onChange={handleChange} onBlur={handleOnBlur}/><br/>
            {errorMsg.name && 
            <>
                 <span className="input-validate-error">{errorMsg.name}</span><br/>
            </>
            }
        </div>
        <div className={`input-fields-container${errorMsg.email?" is-error":""}`}>
        <label htmlFor="email">Email:</label><br/>
        <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} onBlur={handleOnBlur}/><br/>
        {errorMsg.email && 
            <>
                 <span className="input-validate-error">{errorMsg.email}</span><br/>
            </>
            }
        </div>

        <label htmlFor="message">Message:</label><br/>
        <textarea id="message" name="message" value={formData.message} onChange={handleChange} onBlur={handleOnBlur}/><br/>

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