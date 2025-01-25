import React, { useState } from 'react';
import './Project2.css';

const Project2 = () => {
  const [uploadedFile, setUploadedFile] = useState(null);
  const [predictedData, setPredictedData] = useState(null);

  const handleFileUpload = (event) => {
    setUploadedFile(event.target.files[0]); // Save uploaded file in state
  };

  const handlePredict = async () => {
    if (!uploadedFile) {
      alert('Please upload a file first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', uploadedFile);

    try {
      const response = await fetch('https://your-backend-api.com/predict', { // Replace with actual API
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Failed to fetch prediction');
      }

      const data = await response.json(); // Parse JSON data from backend
      setPredictedData(data); // Update state with received data
    } catch (error) {
      console.error('Error predicting data:', error);
    }
  };

  return (
    <div className="project2">
      {/* Hero Section */}
      <section className="hero">
        <h1 className="hero-title">Welcome to Project 2</h1>
        <p className="hero-description">Upload a file and see predictions from the backend below!</p>

        {/* Upload Button */}
        <label htmlFor="file-upload" className="upload-button">
          <img src="src/assets/upload.png" alt="Upload" className="upload-icon" />
          Upload
        </label>
        <input
          type="file"
          id="file-upload"
          onChange={handleFileUpload}
          style={{ display: 'none' }}
        />
      </section>

      {/* Predict Button */}
      <button className="predict-button" onClick={handlePredict}>
        Predict
      </button>

      {/* Display Content Section */}
      {predictedData && (
        <div className="content-section">
          <div className="item-box">
            <h3 className="item-title">{predictedData.title}</h3>
            <div className="item-content-wrapper">
              <img src={predictedData.imageUrl} alt="Prediction" className="item-image" />
              <div className="item-content">
                <p>{predictedData.description}</p>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Project2;