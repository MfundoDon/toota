import "./App.css";
// eslint-disable-next-line no-unused-vars
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import DriverRegistrationForm from "./components/Driver/DriverRegistrationForm";
import DriverLoginForm from "./components/Driver/DriverLoginForm";
import UserLoginForm from "./components/User/UserLoginForm";
import NotFound from "./pages/NotFound";


function App() {
  return (
    <Router>
      <div>
        {/* Other components or content */}
        <Routes>
          <Route path="/signup/driver" element={<DriverRegistrationForm />} />
          <Route path="/login/driver" element={<DriverLoginForm />} />
          <Route path="/" element={<UserLoginForm />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
        {/* Other components or content */}
      </div>
    </Router>
  
  );
}

export default App;