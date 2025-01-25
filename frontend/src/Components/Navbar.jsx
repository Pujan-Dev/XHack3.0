import React from 'react';
import './Navbar.css';
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="logo">
          <Link to="/">
            <img id="Nav-Image" src="src/assets/logo.png" alt="Typecraft Logo" />
          </Link>
        </div>

        <ul className="nav-links">
          <li>
            <a href="#home">Home</a>
          </li>
          <li>
            <a href="#features">Services</a>
          </li>
          <li>
            <a href="#pricing">Pricing</a>
          </li>
        </ul>

        <div>
          <Link to="/signin" className="sign-in-btn">Sign in</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
