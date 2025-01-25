import React from 'react';

const SignIn = () => {
  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Sign In</h1>
      <form>
        <div>
          <label>Email: </label>
          <input type="email" placeholder="Enter your email" />
        </div>
        <div>
          <label>Password: </label>
          <input type="password" placeholder="Enter your password" />
        </div>
        <button type="submit" style={{ marginTop: '20px' }}>Sign In</button>
      </form>
    </div>
  );
};

export default SignIn;
