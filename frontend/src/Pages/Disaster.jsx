import React, { useEffect, useState } from "react";
import "./Disaster.css"; // Your styles here

const Disaster = () => {
  const [disasters, setDisasters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Function to fetch disaster news
  const fetchDisasters = async () => {
    try {
      setLoading(true);
      const response = await fetch('http://localhost:5000/news?keyword=natural disaster');
      const data = await response.json();
      
      if (response.ok) {
        setDisasters(data);
      } else {
        setError("Failed to fetch disaster data.");
      }
    } catch (error) {
      setError("An error occurred while fetching disaster data.");
    } finally {
      setLoading(false);
    }
  };

  // Fetch data on component mount
  useEffect(() => {
    fetchDisasters();
  }, []);

  return (
    <div className="disaster-page">
      {/* Hero Section */}
      <section className="hero-section">
        <h1>Latest Disasters</h1>
        <p>Discover the latest disasters and their impact around the globe.</p>
      </section>

      {/* Display Loading State */}
      {loading ? (
        <div className="loading">
          <p>Loading disasters...</p>
        </div>
      ) : error ? (
        <div className="error">
          <p>{error}</p>
        </div>
      ) : (
        // Show disasters
        <div className="disaster-list">
          {disasters.length === 0 ? (
            <p>No disasters found.</p>
          ) : (
            disasters.map((disaster, index) => (
              <div key={index} className="disaster-item">
                <h3>{disaster.title}</h3>
                <p className="date">{disaster.date}</p>
                <p className="content">{disaster.content}</p>
                <p className="country">Country: {disaster.country}</p>
              </div>
            ))
          )}
        </div>
      )}
    </div>
  );
};

export default Disaster;
