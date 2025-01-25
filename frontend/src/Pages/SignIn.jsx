import React, { useState } from 'react';
import axios from 'axios';
import './SignIn.css';

const SignIn = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent the form from refreshing the page

    if (!email || !password) {
      setMessage('Email and password are required');
      return;
    }

    try {
      const response = await axios.post('http://127.0.0.1:5000/login', {
        username: email, // Assuming your backend expects "username" instead of "email"
        password,
      });
      setMessage(response.data.message); // Display success message
    } catch (error) {
      setMessage(error.response?.data?.message || 'An error occurred during login');
    }
  };

  return (
    <div className="signin-container">
      <div className="signin-box">
        <h1>Sign In</h1>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Email</label>
            <input
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="signin-button">
            Sign In
          </button>
        </form>
        {message && <p className="message">{message}</p>}
      </div>
    </div>
  );
};

export default SignIn;