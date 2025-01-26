import React, { useEffect, useRef, useState } from 'react';
import './Handsign.css';

const Handsign = () => {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [isLoading, setIsLoading] = useState(false);
  const [predictionResult, setPredictionResult] = useState(null);

  useEffect(() => {
    const startVideo = async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      } catch (err) {
        alert('Error accessing webcam: ' + err.message);
      }
    };

    startVideo();
  }, []);

  const handleCapture = async () => {
    if (!videoRef.current || !canvasRef.current) return;

    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');

    canvas.width = videoRef.current.videoWidth;
    canvas.height = videoRef.current.videoHeight;

    ctx.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);

    const imageData = canvas.toDataURL('image/jpeg');

    setIsLoading(true);
    setPredictionResult(null);

    try {
      const response = await fetch('http://localhost:8000/api/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: imageData }),
      });

      const data = await response.json();

      setIsLoading(false);

      if (data.error) {
        setPredictionResult({ error: data.error });
      } else {
        setPredictionResult({
          predictedClass: data.predicted_class,
          confidence: data.confidence,
        });
      }
    } catch (error) {
      setIsLoading(false);
      setPredictionResult({ error: error.message });
    }
  };

  return (
    <div className="handsign-container">
      <h1>Hand Sign Recognition</h1>

      {/* Camera Box */}
      <div className="camera-box">
        <video ref={videoRef} width="320" height="240" autoPlay></video>
        <canvas ref={canvasRef} style={{ display: 'none' }}></canvas>
      </div>

      {/* Capture Button */}
      <button className="capture-button" onClick={handleCapture}>
        Capture
      </button>

      {/* Loading Indicator */}
      {isLoading && <p className="loading">Processing... Please wait.</p>}

      {/* Prediction Results */}
      {predictionResult && (
        <div className="result">
          <h3>Your Hand Prediction Result:</h3>
          {predictionResult.error ? (
            <p>Error: {predictionResult.error}</p>
          ) : (
            <>
              <p>Predicted Class: {predictionResult.predictedClass}</p>
              <p>Confidence: {(predictionResult.confidence * 100).toFixed(2)}%</p>
            </>
          )}
        </div>
      )}
    </div>
  );
};

export default Handsign;
