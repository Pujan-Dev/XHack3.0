import React from 'react';
import './Home.css'; // You can style the sections in this file

const Home = () => {
  return (
    <div>

      {/* Home Page */}
      <section className="home-section">
        <div className="header-lines">
          <h1>Welcome to <u><i>Care•Sign•Alert</i></u></h1>
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
                <p>there is more to</p>
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
            <img src="service1.jpg" alt="Service 1" />
            <h3>Hand Sign Detector</h3>
            <p>An app which we have the  of Service 1.</p>
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
        <h2 className="section-title" id='main-pink'>What Others Say</h2>
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
