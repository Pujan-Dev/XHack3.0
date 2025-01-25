import React from 'react';
import './Home.css'; // You can style the sections in this file

const Home = () => {
  return (
    <div>

      {/* Home Page */}
      <section className="home-section">
        <div className="header-lines">
          <h1 id='main-pink'>Welcome to <u><i>Care•Sign•Alert</i></u></h1>
          <p>Empowering you to learn and grow with us.</p>
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
              <h2>This is what you need</h2>
            </div>
          </div>
          <div id="rightside">
            <div className="top-section">
              <h2>Our Mission</h2>
              <p>Our mission is to make the world an care free world</p>

            </div>
            <div className="bottom-section">
              <div className="bottom-section-left">
                <h2 id='main-pink'>Community</h2>
                <h3>100+_users</h3>
                <p>Join our community and get access to exclusive content and resources.</p>
              </div>
              <div className="bottom-section-right">
                <h2 id='main-pink'>Our Vision</h2>
                <p>Our vision is to make the world a better place</p>
                <p>there is more too..</p>
              </div>
            </div>
          </div>

        </div>
      </section>


      {/* Services Section */}
      <section class="services">
        <div class="services-header">
          <h2 id='main-pink'>Our Services</h2>
          <p>Explore our most popular services and enhance your experience.</p>
        </div>
        <div class="services-grid">
          <div class="service-card">
            <img src="src/assets/service1.jpeg" alt="Service 1" />
            <h3>Realtime News Highlight</h3>
            <p>A platform that provides up-to-the-minute news highlights from around the world. Stay informed with concise summaries and key updates about trending topics you prefer.</p>
            <p>‎</p>
            <button class="cta-btn lavender-btn">Learn More</button>
          </div>
          <div class="service-card">
            <img src="src/assets/service2.jpeg" alt="Service 2" />
            <h3>Plant Disease Detection</h3>
            <p>An AI-powered tool to detect and diagnose plant diseases by analyzing images of leaves. It helps farmers and gardeners take timely actions to protect their crops and ensure healthy plant growth.</p>

            <button class="cta-btn golden-btn">Learn More</button>
          </div>
          <div class="service-card">
            <img src="src/assets/service3.jpeg" alt="Service 3" />
            <h3>Hand Sign Detection</h3>
<p>An AI-powered tool that uses a camera to recognize and interpret hand gestures or signs in real time. It enables seamless interaction and communication, making it useful for applications like sign language translation, gesture-based controls, and more.</p>
            
          <button class="cta-btn lavender-btn">Learn More</button>
          </div>
        </div>
      </section>


      {/* REVIEWS */}
      <section className="reviews-section">
        <h2 className="section-title" id='main-pink'>What Others Say</h2>
        <p className="subtitle">Trusted by thousands of Users</p>
        <div className="reviews-grid">
          {/* Review 1 */}
          <div className="review-card" style={{ borderColor: "lavender" }}>
            <p>
              Thankyou so much for this features, worth every penny. Worth Recommending.
            </p>
            <div className="review-author">
              <img src="src/assets/img1.jpg" alt="DHH profile" />
              <div>
                <span className="author-name">@SUSAN</span>
                <span className="author-title">  Premium User</span>
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
                <span className="author-name">@MamaShishir</span>
              </div>
            </div>
          </div>

          {/* Review 3 */}
          <div className="review-card" style={{ borderColor: "blue" }}>
            <p>Your services are just top-notch. Loved it</p>
            <div className="review-author">
              <img src="src/assets/img3.jpg" alt="Cutie profile" />
              <div>
                <span className="author-name">@AshritaAdh</span>
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
                <span className="author-name">@PrabinBasyal</span>
              </div>
            </div>
          </div>

          {/* Review 5 */}
          <div className="review-card" style={{ borderColor: "pink" }}>
            <p>Hoping for more features in the coming days.</p>
            <div className="review-author">
              <img src="src/assets/img5.jpg" alt="KatyWilliams profile" />
              <div>
                <span className="author-name">@SelenaGomez</span>
              </div>
            </div>
          </div>
        </div>
      </section>


      <section className="pricing-section">
        <h2 className="section-title">Pricing Plans</h2>
        <div className="pricing-grid">
          {/* Basic Plan */}
          <div className="pricing-card">
            <h3>Basic Plan</h3>
            <p className="price">NRs.50</p>
            <ul>
            <li><b>Access to</b></li>
              <li>Personalized News Briefing</li>
            </ul>
            <p>‎</p>
            <p>‎</p>
            <button className="cta-btn lavender-btn">Buy Now</button>
          </div>

          {/* Premium Plan */}
          <div className="pricing-card">
            <h3>Premium Plan</h3>
            <p className="price">NRs.150</p>
            <ul>
              <li><b>Access to</b></li>
              <li>Personalized News Briefing</li>
              <li>AI powered Plant Disease Detection Tool</li>
            </ul>
            <p>‎</p>
            <button className="cta-btn golden-btn">Buy Now</button>
          </div>

          {/* Elite Plan */}
          <div className="pricing-card">
            <h3>Elite Plan</h3>
            <p className="price">NRs.300</p>
            <ul>
            <li><b>Access to</b></li>
            <li>Personalized News Briefing.</li>
            <li>AI powered Plant Disease Detection Tool.</li>
            <li>AI powered Sign Language & Hand Gesture Interpretation Tool.</li>
            </ul>
            <button className="cta-btn lavender-btn">Buy Now</button>
          </div>
        </div>
      </section>


      {/* About Us Section */}
      <section
        className="footer"
        aria-label="Credits"
        style={{
          bottom: '0',
          left: '0',
          width: '100%',
          padding: '1.5rem',
          textAlign: 'center',
          backgroundColor: 'rgba(15, 23, 42, 0.8)', // Matching dark theme with opacity
          backdropFilter: 'blur(8px)',
          borderTop: '1px solid rgba(214, 147, 250, 0.2)', // Accent color border
          fontSize: '0.9rem',
          color: '#D693FA', // Accent color
          fontWeight: '300',
          letterSpacing: '0.05em',
          transition: 'all 0.3s ease'
        }}
      >
        Created by <span style={{ fontWeight: '500', marginLeft: '0.5rem' }}>Team Neurocipher</span>
      </section>

    </div>
  );
};

export default Home;
