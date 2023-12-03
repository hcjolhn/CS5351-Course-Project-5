import { useEffect, useState, useCallback } from "react";
import { useLocation, Link, useNavigate } from "react-router-dom";
import { validateEmail, validateName } from "../../utils/validation-helper";
import "./index.scss";

const FormInput = () => {
    const [formData, setFormData] = useState({name: "",email: "",message: ""});
    const [submitted, setSubmitted] = useState(false);
    const [loading, setLoading] = useState(false);
    const [id, setId] = useState(new URLSearchParams(useLocation().search).get('id'));
    const [errorMsg,setErrorMsg] = useState({});
    const [formSubmitErrMsg,setFormSubmitErrMsg] = useState("");
    const navigate = useNavigate();

    const handleChange = (event) => {
        const { name, value } = event.target;
        if(errorMsg[name] && errorMsg[name] !== ""){
            setErrorMsg({
                ...errorMsg,
                [name]: ""
            })
        }
        if(formSubmitErrMsg && formSubmitErrMsg !== ""){
            setFormSubmitErrMsg("");
        }   
        setFormData((prevFormData) => ({ ...prevFormData, [name]: value }));
    };

    const validate = useCallback(()=>{
        if(/* Object.keys(errorMsg).length > 0 ||  */Object.keys(formData).some((key)=>formData[key] === "")){
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
            setFormSubmitErrMsg("Please make sure you fill in the correct information and submit again.")
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
    <div>
        <div className="welcome-container">
            <div className="title-container">
                    <h1>Automated Tools - Create Page</h1>
            </div>
        </div>
        <div className="form-input-container">
            <h1>Create Form</h1>
        <form onSubmit={handleSubmit}>
        <div className="form-row">
            <div className={`input-fields-container${errorMsg.name?" is-error":""}`}>
                <label htmlFor="name">Name:</label><br/>
                <input type="text" id="name" name="name" value={formData.name} onChange={handleChange} onBlur={handleOnBlur}/>
                {errorMsg.name && 
                <>
                    <span className="input-validate-error">{errorMsg.name}</span><br/>
                </>
                }
            </div>
            <div className={`input-fields-container${errorMsg.email?" is-error":""}`}>
            <label htmlFor="email">Email:</label><br/>
            <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} onBlur={handleOnBlur}/>
            {errorMsg.email && 
                <>
                    <span className="input-validate-error">{errorMsg.email}</span><br/>
                </>
                }
            </div>
        </div>

        <div className="message-container">
            <label htmlFor="message">Message:</label><br/>
            <textarea id="message" name="message" value={formData.message} onChange={handleChange} onBlur={handleOnBlur}/>
        </div>

        <div className="button-container">
            <Link to={"/"}><button className="back-button"><span>Back</span></button></Link>
            <button className="submit-button" type="submit"><span>Submit</span></button>
        </div>
        {errorMsg.submit && 
            <>
                 <span className="input-validate-error">{errorMsg.submit}</span><br/>
            </>
            }
        </form>
        {formSubmitErrMsg !== "" && 
            <div className="form-submit-err-msg-container">
                 <span className="input-validate-error form-err-msg">{formSubmitErrMsg}</span><br/>
            </div>
        }
        {submitted && (
            <div>
            <h2>Submitted Data:</h2>
            <p>Name: {formData.name}</p>
            <p>Email: {formData.email}</p>
            <p>Message: {formData.message}</p>
            </div>
        )}
        </div>
    </div>
    );
}

export default FormInput;