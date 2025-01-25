import React from 'react';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="logo">
          <a href="#home">
            <img id='Nav-Image' src="src/assets/logo.png" alt="Typecraft Logo" />
          </a>
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
          <a href="/signin" className="sign-in-btn">Sign in</a>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
