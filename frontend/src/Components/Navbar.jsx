import React from 'react';
import './Navbar.css';
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        {/* Logo */}
        <div className="logo">
          <Link to="/">
            <img id="Nav-Image" src="src/assets/logo.png" alt="Typecraft Logo" />
          </Link>
        </div>

        {/* Navigation Links */}
        <ul className="nav-links">
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/PlantDisease">Plant Disease</Link>
          </li>
          <li>
            <Link to="/News">Agriculture News</Link>
          </li>
          <li>
            <Link to="/handsign">Sign Detector</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
