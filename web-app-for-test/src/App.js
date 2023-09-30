import './App.css';
import { useState } from "react";

function App() {
  const [formData, setFormData] = useState({name: "",email: "",message: ""});
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevFormData) => ({ ...prevFormData, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    setSubmitted(true);
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
    </div>
  );
}

export default App;
