import React from 'react';
import './Home.css'; // You can style the sections in this file

const Home = () => {
  return (
    <div>
      {/* Navigation Links
      <nav className="navbar">
        <div className="navbar-container">
          <div className="logo">
            <a href="#home">
              <img src="logo.png" alt="Logo" />
              <span>typecraft</span>
            </a>
          </div>
          <ul className="nav-links">
            <li>
              <a href="#home">Home</a>
            </li>
            <li>
              <a href="#services">Services</a>
            </li>
            <li>
              <a href="#about-us">About Us</a>
            </li>
          </ul>
        </div>
      </nav> */}

      {/* Home Page */}
<section className="home-section">


  <div className="content-wrapper">
    {/* Left Section: Video or Image */}
    <div className="left-section">
      <video controls className="video-frame">
        <source src="/path-to-your-video.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      <div className="video-text">
        <p>Care•Sign•Alert</p>
        <h2>This is what you need</h2>
      </div>
    </div>

    {/* Right Section: Blocks */}
    <div className="right-section">
      {/* Top Info Blocks */}
      <div className="info-blocks">
        <div className="info-card">
          <h3>Welcome to Care•Sign•Alert</h3>
          <p className="info-title">100,000+ people benefited</p>
          <p>Active Learning</p>
        </div>
        <div className="info-card">
          <h3>Growing Community</h3>
          <p className="info-title highlight">Master Your Learning Subject</p>
          <p>New content added weekly</p>
        </div>
      </div>

      {/* Bottom Content Cards */}
      <div className="content-cards">
        <div className="card">
          <span className="card-label">POPULAR</span>
          <h3>Learn Content 1</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque, molestiae.</p>
          <a href="#" className="read-more">Read More →</a>
        </div>
        <div className="card">
          <span className="card-label">NEW</span>
          <h3>Learn content 2</h3>
          <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Cupiditate, quibusdam!</p>
          <a href="#" className="read-more">Read More →</a>
        </div>
      </div>
    </div>
  </div>
</section>


      {/* Services Section */}
      <section class="services">
  <div class="services-header">
    <h2>Our Services</h2>
    <p>Explore our most popular services and enhance your experience.</p>
  </div>
  <div class="services-grid">
    <div class="service-card">
      <img src="service1.jpg" alt="Service 1" />
      <h3>Service 1</h3>
      <p>A short description of Service 1.</p>
      <a href="#" class="service-link">Learn More →</a>
    </div>
    <div class="service-card">
      <img src="service2.jpg" alt="Service 2" />
      <h3>Service 2</h3>
      <p>A short description of Service 2.</p>
      <a href="#" class="service-link">Learn More →</a>
    </div>
    <div class="service-card">
      <img src="service3.jpg" alt="Service 3" />
      <h3>Service 3</h3>
      <p>A short description of Service 3.</p>
      <a href="#" class="service-link">Learn More →</a>
    </div>
  </div>
</section>


{/* REVIEWS */}
<section className="reviews-section">
  <h2 className="section-title">What Others Say</h2>
  <p className="subtitle">Trusted by thousands of developers</p>
  <div className="reviews-grid">
    {/* Review 1 */}
    <div className="review-card" style={{ borderColor: "lavender" }}>
      <p>
       Thankyou so much for this features, worth every penny. Worth Recommending.
      </p>
      <div className="review-author">
        <img src="src/assets/img1.jpg" alt="DHH profile" />
        <div>
          <span className="author-name">@DHH</span>
          <span className="author-title">  Premium Subscriber</span>
        </div>
      </div>
    </div>

    {/* Review 2 */}
    <div className="review-card" style={{ borderColor: "pink" }}>
      <p>
        Wow. I've seen many other in market but I find this best among all.
      </p>
      <div className="review-author">
        <img src="src/assets/img2.jpg" alt="dandandan01 profile" />
        <div>
          <span className="author-name">@dandandan01</span>
        </div>
      </div>
    </div>

    {/* Review 3 */}
    <div className="review-card" style={{ borderColor: "blue" }}>
      <p>Your services are just top-notch. Loved it</p>
      <div className="review-author">
        <img src="src/assets/img3.jpg" alt="Cutie profile" />
        <div>
          <span className="author-name">@CutiePie</span>
        </div>
      </div>
    </div>

    {/* Review 4 */}
    <div className="review-card" style={{ borderColor: "goldenrod" }}>
      <p>
        Absolutely love the features provided by this platform.
      </p>
      <div className="review-author">
        <img src="src/assets/img4.jpg" alt="Brand0-d9w profile" />
        <div>
          <span className="author-name">@Brand0-d9w</span>
        </div>
      </div>
    </div>

    {/* Review 5 */}
    <div className="review-card" style={{ borderColor: "pink" }}>
      <p>Hoping for more features in the coming days.</p>
      <div className="review-author">
        <img src="src/assets/img5.jpg" alt="KatyWilliams profile" />
        <div>
          <span className="author-name">@Katywilliams</span>
        </div>
      </div>
    </div>
  </div>
</section>


<section className="pricing-section">
  <h2 className="section-title">Pricing Plans</h2>
  <div className="pricing-grid">
    {/* Free Plan */}
    <div className="pricing-card">
      <h3>Free Plan</h3>
      <p className="price">$0.00</p>
      <ul>
        <li>Newsletter with coding tips</li>
        <li>Access to member-only content</li>
      </ul>
      <button className="cta-btn lavender-btn">Get Started</button>
    </div>

    {/* Premium Plan */}
    <div className="pricing-card">
      <h3>Premium Plan</h3>
      <p className="price">$89.99</p>
      <ul>
        <li>Special Discord access</li>
        <li>Early access to features</li>
      </ul>
      <button className="cta-btn golden-btn">Subscribe</button>
    </div>

    {/* Elite Plan */}
    <div className="pricing-card">
      <h3>Elite Plan</h3>
      <p className="price">$129.99</p>
      <ul>
        <li>Exclusive webinars</li>
        <li>Direct mentorship access</li>
      </ul>
      <button className="cta-btn lavender-btn">Buy Now</button>
    </div>
  </div>
</section>


      {/* About Us Section */}
      <section className="about-us-section">
  <h2 className="section-title">About Us</h2>
  <div className="team-list colorful-border">
    <h3>Our Team</h3>
    <ul>
      <li>Pujan Neupane</li>
      <li>Sujal Karki</li>
      <li>Roshan Panthi</li>
      <li>Rabin Kattel</li>
    </ul>
  </div>
  <p className="purpose colorful-border">
    We aim to serve people through innovative and accessible technological solutions. 
    Our mission is to make a positive impact by delivering high-quality services that 
    cater to the needs of individuals and communities.
  </p>
</section>

    </div>
  );
};

export default Home;
