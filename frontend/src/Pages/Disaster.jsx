import React, { useEffect, useState } from "react";
import "./Disaster.css"; // Your styles here

const Disaster = () => {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchNews = async () => {
      try {
        // Make a GET request to the Flask API
        const response = await fetch("http://127.0.0.1:5000/news?keyword=disaster&lang=en&country=us&max=10");
        
        if (!response.ok) {
          throw new Error("Failed to fetch news data");
        }

        const data = await response.json();
        setNews(data.articles || []); // `articles` is the key for the news list
        setLoading(false);
      } catch (error) {
        console.error("Error fetching news:", error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchNews();
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
        <p>Loading news...</p>
      ) : error ? (
        <p className="error">{error}</p>
      ) : (
        <div className="disaster-grid">
          {news.map((article, index) => (
            <div key={index} className="disaster-card">
              <h3>{article.title}</h3>
              <p className="date">{new Date(article.publishedAt).toLocaleDateString()}</p>
              <p className="briefing">{article.description}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Disaster;
