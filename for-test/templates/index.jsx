import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [predictedClass, setPredictedClass] = useState("");
  const [confidence, setConfidence] = useState("");
  const [imagePath, setImagePath] = useState("");
  const [error, setError] = useState("");

  // Handle file selection
  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
    }
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      alert("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://localhost:5000/predict", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      if (response.data.error) {
        setError(response.data.error);
        setPredictedClass("");
        setConfidence("");
        setImagePath("");
      } else {
        setPredictedClass(response.data.predicted_class);
        setConfidence(response.data.confidence);
        setImagePath(response.data.image_path);
        setError("");
      }
    } catch (error) {
      setError("Error uploading the image. Please try again.");
      setPredictedClass("");
      setConfidence("");
      setImagePath("");
    }
  };

  return (
    <div className="App">
      <h1>Plant Disease Prediction</h1>
      <p>Upload a plant image to predict its disease!</p>

      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          required
        />
        <br />
        <button type="submit">Predict</button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {predictedClass && (
        <div>
          <h2>Prediction Result</h2>
          <p>Predicted Class: {predictedClass}</p>
          <p>Confidence: {confidence}%</p>
          <img
            src={imagePath}
            alt="Uploaded"
            style={{ maxWidth: "300px", marginTop: "10px" }}
          />
        </div>
      )}
    </div>
  );
}

export default App;
