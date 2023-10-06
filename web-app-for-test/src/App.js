import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom"; 
import Form from "./pages/Form"
import FormInput from "./pages/FormInput"

function App() {
  return(
    <BrowserRouter>
      <Routes>
        <Route path="/" index element= {<Form/>} />
        <Route path="/form_input" index element= {<FormInput/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
