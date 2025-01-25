import React, { useState } from "react";
import axios from "axios";
import "./Project2.css"; // Import your CSS file for styling

const Project2 = () => {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState("");
  const [actualLabel, setActualLabel] = useState("");
  const [predictedLabel, setPredictedLabel] = useState("");
  const [confidence, setConfidence] = useState("");
  const [imagePath, setImagePath] = useState("");

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
      // Send the form data to the backend
      const response = await axios.post("http://127.0.0.1:5000/api/predict_sujal", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      // Log the response data for debugging
      console.log("Response Data:", response.data);

      // Assuming the backend sends a response with the necessary fields
      setPrediction(response.data); // Set the prediction data
      setActualLabel(response.data.actual_label);
      setPredictedLabel(response.data.predicted_label);
      setConfidence(response.data.confidence);
      setImagePath(response.data.image_path);
    } catch (err) {
      console.error("Error fetching prediction:", err);
      setError("An error occurred while uploading the file.");
    }
  };

  return (
    <div className="project-container">
      {/* Description Section */}
      <section className="description-section">
        <h1>Crop Disease Classification</h1>
      </section>

      {/* Form Section */}
      <div className="form-box">
        <form onSubmit={handleSubmit}>
          <div className="upload-section">
            <label htmlFor="file-upload" className="upload-button">
              <img src="src/assets/upload.png" alt="Upload Icon" className="upload-icon" />
              <span>Upload Image</span>
            </label>
            <input
              id="file-upload"
              type="file"
              onChange={handleFileChange}
              style={{ display: "none" }}
              accept=".jpg, .jpeg, .png"
            />
          </div>
          {error && <p className="error-message">{error}</p>}
          <button type="submit" className="predict-button">
            Predict
          </button>
        </form>
      </div>
      <h2>
        Upload your image here. Once uploaded, click "Predict" to see the prediction results below.
      </h2>
      
      {/* Prediction Result Section */}
      {prediction && (
        <div className="result-box">
          <h2>{predictedLabel}</h2>
          <div className="result-content">
            <p className="result-description"><strong>Actual Label:</strong> {actualLabel}</p>
            <br/>
            <p className="result-description"><strong>Confidence:</strong> {confidence}%</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default Project2;
