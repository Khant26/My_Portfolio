import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { gsap } from 'gsap';
import '../styles/Hero.css';

function Hero() {
  useEffect(() => {
    const ctx = gsap.context(() => {
      // Animate h1
      gsap.from('.hero h1', {
        opacity: 0,
        scale: 0.8,
        duration: 1,
        ease: 'power2.out',
      });

      // Animate p
      gsap.from('.hero p', {
        opacity: 0,
        y: 30,
        duration: 1,
        delay: 0.2,
        ease: 'power2.out',
      });

      // Animate CTA button with bounce
      gsap.from('.cta-button', {
        opacity: 0,
        y: 20,
        duration: 0.8,
        delay: 0.4,
        ease: 'bounce.out',
      });
    });

    return () => ctx.revert(); // Cleanup animations
  }, []);

  return (
    <section className="hero">
      <h1>Welcome to My Portfolio</h1>
      <p>Hi, I'm Khant Maung, a Test Automation Engineer and Full Stack Web Developer with experience in React.js, Node.js, and Express. Previously, I worked as a Translator, honing my attention to detail.</p>
      <Link to="/projects" className="cta-button">View My Projects</Link>
    </section>
  );
}

export default Hero;