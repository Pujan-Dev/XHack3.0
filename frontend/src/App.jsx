import React from 'react';
import Navbar from './Components/Navbar';
<<<<<<< HEAD
// import Home from './Components/Home';
// import Disaster from './Pages/Disaster';
import Project from './Pages/Project2';

=======
import Home from './Components/Home';
import SignIn from './Pages/SignIn.jsx'; // Import the SignIn component
import { Routes, Route } from 'react-router-dom';
import "./App.css";
import Handsign from './Pages/Handsign.jsx'; // Import the sign component
import Project2 from './Pages/Project2.jsx'; // Import the Project2 component
import Disaster from './Pages/Disaster.jsx'; // Import the Disaster component
>>>>>>> 438835594ed4739651b6734745ab55b72a1d490a
const App = () => {
  return (
    <div>
      <Navbar />
<<<<<<< HEAD
      {/* <Home /> */}
      {/* <Disaster /> */}
      <Project />

=======
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/signin" element={<SignIn />} />
        <Route path="/handsign" element={<Handsign/>} />
        <Route path="/PlantDisease" element={< Project2/>} />
        <Route path="/News" element={< Disaster/>} />


        
      </Routes>
>>>>>>> 438835594ed4739651b6734745ab55b72a1d490a
    </div>
  );
};

export default App;
