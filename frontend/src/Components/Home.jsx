import React from 'react';
import './Home.css'; // Style the sections in this file

const Home = () => {
  return (
    <div>

      {/* Home Page */}
      <section className="home-section">
        <div className="header-lines">
          <h1 id="main-pink">Welcome to <u><i>Care•Sign•Alert</i></u></h1>
          <p>Empowering lives through agriculture and accessibility.</p>
        </div>

        <div className="content-wrapper">
          {/* Left Section: Video or Image */}
          <div className="left-section">
            <video controls className="video-frame">
              <source src="/path-to-your-video.mp4" type="video/mp4" />
              Your browser does not support the video tag.
            </video>
            <div className="video-text">
              <p>Care•Sign•Alert</p>
              <h2>Your Partner in Growth and Care</h2>
            </div>
          </div>
          <div id="rightside">
            <div className="top-section">
              <h2>Our Mission</h2>
              <p>To create a sustainable future for agriculture and improve accessibility for children with disabilities.</p>
            </div>
            <div className="bottom-section">
              <div className="bottom-section-left">
                <h2 id="main-pink">Community</h2>
                <h3>1000+ members</h3>
                <p>Join our community to access resources for modern farming and inclusive education.</p>
              </div>
              <div className="bottom-section-right">
                <h2 id="main-pink">Our Vision</h2>
                <p>To blend technology with empathy for a world that grows together.</p>
                <p>We aim to empower farmers and children with tools for a brighter future.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section className="services">
        <div className="services-header">
          <h2 id="main-pink">Our Services</h2>
          <p>Explore our innovative solutions for agriculture and accessibility.</p>
        </div>
        <div className="services-grid">
          <div className="service-card">
            <img src="src/assets/service1.jpeg" alt="Service 1" />
            <h3>Realtime Agriculture News</h3>
            <p>Stay updated with the latest agriculture news and trends. Get expert insights and actionable advice to improve your yields.</p>
            <button className="cta-btn lavender-btn">Learn More</button>
          </div>
          <div className="service-card">
            <img src="src/assets/service2.jpeg" alt="Service 2" />
            <h3>Plant Health Monitor</h3>
            <p>An AI tool to detect plant diseases through leaf analysis. Prevent crop loss and improve productivity with actionable insights.</p>
            <button className="cta-btn golden-btn">Learn More</button>
          </div>
          <div className="service-card">
            <img src="src/assets/service3.jpeg" alt="Service 3" />
            <h3>Sign Language Assistant</h3>
            <p>An AI-powered tool that aids in learning and understanding sign language. Ideal for children with disabilities and their caregivers.</p>
            <button className="cta-btn lavender-btn">Learn More</button>
          </div>
        </div>
      </section>

      {/* Reviews Section */}
      <section className="reviews-section">
        <h2 className="section-title" id="main-pink">What People Say</h2>
        <p className="subtitle">Loved by farmers and caregivers alike</p>
        <div className="reviews-grid">
          <div className="review-card" style={{ borderColor: "lavender" }}>
            <p>“The plant disease detection tool has saved my crops multiple times. A game-changer for farmers!”</p>
            <div className="review-author">
              <img src="src/assets/img1.jpg" alt="Profile 1" />
              <div>
                <span className="author-name">@Ramesh Singh</span>
              </div>
            </div>
          </div>
          <div className="review-card" style={{ borderColor: "pink" }}>
            <p>“This platform helps me stay updated with agriculture trends. Highly recommended!”</p>
            <div className="review-author">
              <img src="src/assets/img2.jpg" alt="Profile 2" />
              <div>
                <span className="author-name">@Priya Sharma</span>
              </div>
            </div>
          </div>
          <div className="review-card" style={{ borderColor: "blue" }}>
            <p>“The sign language tool is incredible. My students love it and have improved so much!”</p>
            <div className="review-author">
              <img src="src/assets/img3.jpg" alt="Profile 3" />
              <div>
                <span className="author-name">@Arjun Patel</span>
              </div>
            </div>
          </div>
          <div className="review-card" style={{ borderColor: "goldenrod" }}>
            <p>“This app truly bridges the gap between technology and care. Amazing work!”</p>
            <div className="review-author">
              <img src="src/assets/img4.jpg" alt="Profile 4" />
              <div>
                <span className="author-name">@Anjali Mehra</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section className="pricing-section">
        <h2 className="section-title">Affordable Plans</h2>
        <div className="pricing-grid">
          <div className="pricing-card">
            <h3>Starter Plan</h3>
            <p className="price">NRs. 50</p>
            <ul>
              <li>Access to real-time agriculture news</li>
            </ul>
            <button className="cta-btn lavender-btn">Get Started</button>
          </div>
          <div className="pricing-card">
            <h3>Growth Plan</h3>
            <p className="price">NRs. 150</p>
            <ul>
              <li>Access to news</li>
              <li>Plant disease detection</li>
            </ul>
            <button className="cta-btn golden-btn">Get Started</button>
          </div>
          <div className="pricing-card">
            <h3>Pro Plan</h3>
            <p className="price">NRs. 300</p>
            <ul>
              <li>Access to news</li>
              <li>Plant disease detection</li>
              <li>Sign language assistance</li>
            </ul>
            <button className="cta-btn lavender-btn">Get Started</button>
          </div>
        </div>
      </section>

      {/* Footer */}
      <section
        className="footer"
        aria-label="Credits"
        style={{
          bottom: '0',
          left: '0',
          width: '100%',
          padding: '1.5rem',
          textAlign: 'center',
          backgroundColor: 'rgba(15, 23, 42, 0.8)',
          backdropFilter: 'blur(8px)',
          borderTop: '1px solid rgba(214, 147, 250, 0.2)',
          fontSize: '0.9rem',
          color: '#D693FA',
          fontWeight: '300',
          letterSpacing: '0.05em',
          transition: 'all 0.3s ease',
        }}
      >
        Created by <span style={{ fontWeight: '500', marginLeft: '0.5rem' }}>Team Care•Sign•Alert</span>
      </section>

    </div>
  );
};

export default Home;
