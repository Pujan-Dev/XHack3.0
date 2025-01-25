import React, { useEffect, useState } from "react";
import "./Disaster.css"; // Import the CSS file

const Disaster = () => {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/news");
        if (!response.ok) {
          throw new Error("Failed to fetch news");
        }
        const data = await response.json();
        setNews(data);
      } catch (error) {
        console.error("Error fetching news:", error);
        setError(error.message); // Set error state
      } finally {
        setLoading(false);
      }
    };
  
    fetchNews();
  }, []); // Empty dependency array to run once

  return (
    <div className="disaster-container">
      <h1 className="disaster-heading">🌍 Latest News on Agriculture</h1>
      
      {loading ? (
        <div className="loader-container">
          <div className="spinner"></div>
          <p className="loader-text">Getting the latest news...</p>
        </div>
      ) : error ? (
        <p className="error-text">⚠️ Error: {error}</p>
      ) : (
        <div className="news-container">
          {news.map((article, index) => (
            <div key={index} className="news-card">
              <h3 className="news-title">{article.title}</h3>
              <p className="news-content">{article.content}</p>
              <p className="news-country">🌍 Country: {article.country}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Disaster;
