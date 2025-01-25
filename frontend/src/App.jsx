import React from 'react';
import Navbar from './Components/Navbar';
import Home from './Components/Home';
// import SignIn from './Pages/SignIn.jsx'; // Import the SignIn component
import { Routes, Route } from 'react-router-dom';
import "./App.css";
import Handsign from './Pages/Handsign.jsx'; // Import the sign component
import Project2 from './Pages/Project2.jsx'; // Import the Project2 component
import Disaster from './Pages/Disaster.jsx'; // Import the Disaster component
const App = () => {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        {/* <Route path="/signin" element={<SignIn />} /> */}
        <Route path="/handsign" element={<Handsign/>} />
        <Route path="/PlantDisease" element={< Project2/>} />
        <Route path="/News" element={< Disaster/>} />


        
      </Routes>
    </div>
  );
};

export default App;
