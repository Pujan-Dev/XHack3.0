import React, { useState } from "react";
// import axios from "axios";
import "./Project2.css"; // Import your CSS file for styling

const Project = () => {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      setError("Please upload a file.");
      return;
    }

    setError("");
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://127.0.0.1:5000/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setPrediction(response.data); // Set the prediction data
    } catch (err) {
      console.error(err);
      setError("An error occurred while uploading the file.");
    }
  };

  return (
    <div className="project-container">
      {/* Description Section */}
      <section className="description-section">
        <h1>File Upload and Prediction</h1>
      </section>

      {/* Form Section */}
      <div className="form-box">
        <form onSubmit={handleSubmit}>
          <div className="upload-section">
            <label htmlFor="file-upload" className="upload-button">
              <img src="src/assets/upload.png" alt="Upload Icon" className="upload-icon" />
              <span>Upload File</span>
            </label>
            <input
              id="file-upload"
              type="file"
              onChange={handleFileChange}
              style={{ display: "none" }}
            />
          </div>
          {error && <p className="error-message">{error}</p>}
          <button type="submit" className="predict-button">
            Predict
          </button>
        </form>
      </div>
      <h2>
          Upload your file Here. Once uploaded, click "Predict" to see the prediction results below.
        </h2>
      {/* Prediction Result Section */}
      {prediction && (
        <div className="result-box">
          <h2>{prediction.title}</h2>
          <div className="result-content">
            <img src={prediction.image} alt="Prediction" className="result-image" />
            <p className="result-description">{prediction.description}</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default Project;
