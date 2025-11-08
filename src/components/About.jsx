import React, { useEffect } from "react";
import { gsap } from "gsap";
import "../styles/About.css";

function About() {
  useEffect(() => {
    // Fallback to ensure text visibility if GSAP fails
    const timeout = setTimeout(() => {
      document
        .querySelectorAll(
          ".about h2, .about-content, .experience, .skills-list li"
        )
        .forEach((el) => {
          el.style.opacity = "1";
          el.style.transform = "none";
        });
    }, 2000); // 2-second fallback

    const ctx = gsap.context(() => {
      // Animate h2
      gsap.to(".about h2", {
        opacity: 1,
        y: 0,
        duration: 1,
        ease: "power2.out",
      });

      // Animate about-content
      gsap.to(".about-content", {
        opacity: 1,
        y: 0,
        duration: 1,
        delay: 0.2,
        ease: "power2.out",
      });

      // Stagger experience cards
      gsap.to(".experience", {
        opacity: 1,
        x: 0,
        duration: 0.8,
        stagger: 0.2,
        delay: 0.4,
        ease: "power2.out",
      });

      // Stagger skills list
      gsap.to(".skills-list li", {
        opacity: 1,
        y: 0,
        duration: 0.6,
        stagger: 0.1,
        delay: 0.8,
        ease: "power2.out",
      });
    });

    return () => {
      clearTimeout(timeout); // Clear fallback timeout
      ctx.revert(); // Cleanup GSAP animations
    };
  }, []);

  return (
    <section className="about">
      <h2>About Me</h2>
      <div className="about-content">
        <p>
          I'm Khant Maung, a skilled Test Automation Engineer and Full Stack Web
          Developer with a passion for creating dynamic, user-friendly
          applications. My background in translation has sharpened my attention
          to detail, which I apply to both coding and testing.
        </p>
        <h3>Work Experience</h3>
        <div className="experience">
          <h4>Test Automation Engineer - Brillar, Bangkok, Thailand</h4>
          <p className="date">May 2025 - Present</p>
          <ul>
            <li>
              Built responsive web applications using Tosca as an Automation
              Tool.
            </li>
            <li>
              Utilized Tosca's model-based test automation to streamline testing
              processes.
            </li>
            <li>
              Implemented API testing using Tosca to ensure seamless integration
              between services.
            </li>
            <li>
              Leveraged Tosca's risk-based testing to prioritize critical
              functionalities.
            </li>
            <li>
              Integrated Tosca with CI/CD pipelines for continuous testing in
              DevOps workflows.
            </li>
            <li>
              Collaborated with cross-functional teams to manage test data using
              Tosca's data management features.
            </li>
          </ul>
        </div>
        <div className="experience">
          <h4>Full Stack Web Developer – Bangkok, Thailand</h4>
          <p className="date">Since 2023</p>
          <ul>
            <li>
              Developed responsive full-stack web applications using React.js
              and Express.js by 50%.
            </li>
            <li>
              Designed and implemented RESTful APIs, improving server response
              times by 30%.
            </li>
            <li>
              Enhanced application performance through code splitting and lazy
              loading, reducing page load times by 20%.
            </li>
          </ul>
        </div>
        <div className="experience">
          <h4>Translator - Freelance, Bangkok, Thailand</h4>
          <p className="date">January 2021 - December 2022</p>
          <ul>
            <li>
              Translated technical documents between English and Thai with 100%
              accuracy.
            </li>
            <li>Adapted content for cultural nuances, improving usability.</li>
            <li>Managed multiple projects, meeting all deadlines.</li>
          </ul>
        </div>
        <h3>Skills</h3>
        <ul className="skills-list">
          <li>
            <strong>Programming Languages:</strong> C++, JavaScript, Python
          </li>
          <li>
            <strong>Frontend Technologies:</strong> React.js, HTML5, CSS3
          </li>
          <li>
            <strong>Backend Technologies:</strong> Node.js, Express.js
          </li>
          <li>
            <strong>Testing Tools:</strong> Tosca
          </li>
          <li>
            <strong>Other:</strong> Git, RESTful APIs, MongoDB, Agile
            Methodologies, Translation (English-Myanmar)
          </li>
        </ul>
      </div>
    </section>
  );
}

export default About;
