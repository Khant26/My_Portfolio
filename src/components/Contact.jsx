import React, { useEffect } from 'react';
import { gsap } from 'gsap';
import '../styles/Contact.css';

function Contact() {
  useEffect(() => {
    // Fallback to ensure text visibility if GSAP fails
    const timeout = setTimeout(() => {
      document.querySelectorAll('.contact h2, .contact p, .contact-info p, .contact-download').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'none';
      });
    }, 2000); // 2-second fallback

    const ctx = gsap.context(() => {
      // Animate h2
      gsap.to('.contact h2', {
        opacity: 1,
        y: 0,
        duration: 1,
        ease: 'power2.out',
      });

      // Animate p
      gsap.to('.contact p', {
        opacity: 1,
        y: 0,
        duration: 1,
        delay: 0.2,
        ease: 'power2.out',
      });

      // Stagger contact-info items
      gsap.to('.contact-info p', {
        opacity: 1,
        y: 0,
        duration: 0.6,
        stagger: 0.1,
        delay: 0.4,
        ease: 'power2.out',
      });

      // Animate download link
      gsap.to('.contact-download', {
        opacity: 1,
        y: 0,
        duration: 0.6,
        delay: 0.6,
        ease: 'power2.out',
      });
    });

    return () => {
      clearTimeout(timeout); // Clear fallback timeout
      ctx.revert(); // Cleanup GSAP animations
    };
  }, []);

  return (
    <section className="contact">
      <h2>Contact Me</h2>
      <p>Feel free to reach out for collaborations or inquiries!</p>
      <div className="contact-info">
        <p>LinkedIn: <a href="https://www.linkedin.com/in/khant-mg-899330280/">Linkin</a></p>
        <p>GitHub: <a href="https://github.com/Khant26">github</a></p>
        <p>Phone: +66-930470721</p>
      </div>
      <a href="/KhantMaung_CV.pdf" download className="contact-download">Download Resume (PDF)</a>
    </section>
  );
}

export default Contact;