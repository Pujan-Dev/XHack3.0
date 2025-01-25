import React, { useEffect, useState } from "react";

const Disaster = () => {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Function to fetch news
    const fetchNews = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/news'); // Your backend URL
        if (!response.ok) {
          throw new Error('Failed to fetch news');
        }
        const data = await response.json();
        setNews(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchNews();
  }, []);

  return (
    <div>
      <h1>Latest News</h1>

      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p>Error: {error}</p>
      ) : (
        <ul>
          {news.map((article, index) => (
            <li key={index}>
              <h3>{article.title}</h3>
              <p>{article.content}</p>
              <p>Country: {article.country}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Disaster;
