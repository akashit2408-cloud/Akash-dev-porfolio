import React, { useState, useEffect, useRef } from 'react';
import AOS from 'aos';
import 'aos/dist/aos.css';
import { motion, AnimatePresence, useScroll, useSpring, useMotionValueEvent, useTransform } from 'framer-motion';

const projectsTimeline = [
  {
    number: "01",
    role: "GrindLog",
    company: "AI-Powered Fitness & Nutrition Platform",
    period: "Next.js, React, OpenAI, Gemini API, Supabase",
    details: [
      "Built an end-to-end fitness OS and PWA integrating OpenAI and Gemini Vision APIs to analyze user meal logs and generate personalized workout recommendations.",
      "Built a fast, responsive user interface using Next.js App Router, React Suspense loading skeletons, and optimistic UI for instant workout set logging.",
      "Implemented Razorpay subscription payments with webhook verification, automated push notifications via Vercel Cron, and protected user data using Supabase Row Level Security (RLS)."
    ],
    tags: ["Next.js", "React", "TypeScript", "Tailwind CSS", "Supabase", "OpenAI API", "Gemini API", "Razorpay", "PWA"],
    liveUrl: "https://grindlog.in",
    github: null,
    className: "md:absolute md:top-[10px] md:right-[2%] lg:right-[5%] md:rotate-2",
    aosType: "fade-up",
    aosDelay: "100",
    theme: "light"
  },
  {
    number: "02",
    role: "Dark Syndicate",
    company: "Gaming Arena & Venue Operations Platform",
    period: "Next.js, React, Prisma ORM, MySQL",
    details: [
      "Engineered an esports arena & lounge operations platform managing real-time station inventory, online slot reservations, front-desk walk-in POS, and dynamic pricing across PlayStation 5 stations and snooker tables.",
      "Developed an active station countdown timer with audio alerts and built a POS billing system supporting both Cash and UPI payments via Razorpay.",
      "Implemented role-based access for Admin, Staff, and Customers, PWA support for mobile POS use, and CSV reporting for daily sales tracking."
    ],
    tags: ["Next.js", "React", "TypeScript", "Tailwind CSS", "Prisma ORM", "MySQL", "Razorpay", "PWA"],
    liveUrl: "https://darksyndicategw.com",
    github: null,
    className: "md:absolute md:top-[480px] md:left-[2%] lg:left-[5%] md:-rotate-2",
    aosType: "fade-up",
    aosDelay: "200",
    theme: "dark"
  },
  {
    number: "03",
    role: "The Atom",
    company: "Corporate Digital Presence",
    period: "HTML5, CSS3, JS, PHP, MySQL",
    details: [
      "Engineered corporate digital presence from scratch, implementing responsive semantic UI and mobile-first ergonomics.",
      "Optimized asset delivery, image compression, and structured meta-tags to reduce payload size and improve search discoverability."
    ],
    tags: ["HTML5", "CSS3", "JavaScript", "PHP", "MySQL", "SEO Architecture"],
    liveUrl: "https://theatom.biz",
    github: null,
    className: "md:absolute md:top-[1020px] md:right-[2%] lg:right-[8%] md:rotate-3",
    aosType: "fade-up",
    aosDelay: "300",
    theme: "light"
  }
];

const skillsCategories = [
  {
    title: "Frontend",
    skills: [
      "React",
      "Next.js (App Router)",
      "TypeScript",
      "JavaScript (ES6+)",
      "Tailwind CSS",
      "HTML5",
      "CSS3",
      "Bootstrap 5",
      "PWA",
      "Mobile-First UI"
    ]
  },
  {
    title: "Backend & APIs",
    skills: [
      "Node.js",
      "Next.js API Routes",
      "RESTful APIs",
      "Supabase Auth (JWT)",
      "PHP"
    ]
  },
  {
    title: "Databases & Cloud",
    skills: [
      "PostgreSQL",
      "MySQL",
      "Supabase (Database, Auth, Storage, RLS)",
      "Relational Database Design",
      "Vercel"
    ]
  },
  {
    title: "Tools & Workflow",
    skills: [
      "Git",
      "GitHub",
      "GitHub Actions",
      "VS Code",
      "Postman",
      "Vercel"
    ]
  }
];

const TimelineCard = ({ exp, pathLength, containerRef }) => {
  const d = useRef(null);
  const [f, p] = useState(false);

  useMotionValueEvent(pathLength, "change", (e) => {
    if (!d.current || !containerRef.current) return;
    const t = d.current.getBoundingClientRect();
    const n = containerRef.current.getBoundingClientRect();
    const r = t.top - n.top;
    const i = n.height;
    const a = r + 50;
    const o = e * i;
    if (o >= a && !f) {
      p(true);
    } else if (o < a && f) {
      p(false);
    }
  });

  return (
    <div ref={d} data-aos={exp.aosType} data-aos-delay={exp.aosDelay} className={`w-full max-w-[360px] sm:max-w-[400px] lg:w-[420px] mx-auto mb-8 md:mb-0 rounded-[2rem] p-2 relative flex flex-col items-center hover:scale-[1.01] transition-all duration-700 z-10 ${exp.className} ${f ? 'bg-luxury-card border border-luxury-gold shadow-[0_0_30px_rgba(59,130,246,0.3)]' : 'bg-[#1a1a1a] border border-white/5 shadow-lg'}`}>
      <div className={`w-5 h-5 bg-gradient-to-br from-gray-300 to-gray-100 rounded-full shadow-[inset_0_2px_4px_rgba(0,0,0,0.3)] absolute top-4 border border-gray-300 z-10 flex items-center justify-center`}>
        <div className={`w-2 h-2 rounded-full ${f ? 'bg-luxury-gold' : 'bg-gray-600'}`}></div>
      </div>
      <div className={`w-full h-full rounded-[1.5rem] mt-8 p-6 flex flex-col min-h-[300px] transition-colors duration-700 ${f ? 'bg-white/5' : 'bg-black/20'}`}>
        <div className="flex justify-between items-center mb-3">
          <span className={`text-base font-bold font-serif italic transition-colors duration-700 ${f ? 'text-luxury-gold' : 'text-gray-500'}`}>{exp.number}</span>
          <span className={`text-[10px] font-bold tracking-wider uppercase transition-colors duration-700 ${f ? 'text-luxury-gold' : 'text-gray-500'}`}>{exp.period}</span>
        </div>
        <h3 className={`text-xl font-black mb-1 tracking-tight transition-colors duration-700 ${f ? 'text-luxury-ivory' : 'text-white/80'}`}>{exp.role}</h3>
        <h4 className={`text-xs font-bold uppercase tracking-wider mb-4 transition-colors duration-700 ${f ? 'text-luxury-taupe' : 'text-gray-400'}`}>{exp.company}</h4>
        <ul className={`text-xs leading-relaxed font-medium mb-5 list-disc pl-4 flex-grow flex flex-col gap-2 transition-colors duration-700 ${f ? 'text-white/90' : 'text-gray-400'}`}>
          {exp.details.map((e, t) => <li key={t}>{e}</li>)}
        </ul>
        <div className="flex flex-col gap-3 mt-auto pt-4 border-t border-dashed border-gray-300/40">
          <div className="flex flex-wrap justify-center gap-1.5">
            {exp.tags.map((e, t) => (
              <span key={t} className={`text-[9px] font-bold px-2.5 py-1 rounded transition-colors duration-700 ${f ? 'bg-luxury-gold/10 text-luxury-gold border border-luxury-gold/30' : 'bg-white/5 text-gray-400 border border-white/10'}`}>
                {e}
              </span>
            ))}
          </div>
          <div className="flex flex-wrap justify-center items-center gap-2 pt-1">
            {exp.liveUrl && (
              <a
                href={exp.liveUrl}
                target="_blank"
                rel="noopener noreferrer"
                className={`inline-flex items-center gap-1.5 text-[10px] font-bold px-3.5 py-1.5 rounded-full transition-all duration-300 ${
                  f
                    ? 'bg-luxury-gold text-white hover:bg-blue-600 shadow-md shadow-luxury-gold/30'
                    : 'bg-luxury-gold/20 text-luxury-gold border border-luxury-gold/40 hover:bg-luxury-gold hover:text-white'
                }`}
              >
                <svg className="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
                Live Demo
              </a>
            )}
            {exp.github && (
              <a
                href={exp.github}
                target="_blank"
                rel="noopener noreferrer"
                className={`inline-flex items-center gap-1.5 text-[10px] font-bold px-3.5 py-1.5 rounded-full transition-all duration-300 ${
                  f
                    ? 'bg-luxury-ivory text-luxury-bg hover:bg-gray-200'
                    : 'bg-white/10 text-white hover:bg-white/20 border border-white/10'
                }`}
              >
                <svg className="w-3.5 h-3.5" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-3.975-1.395-.03-.075-.315-.825-.765-1.125-.345-.165-.825-.615-.015-.63.78-.015 1.335.72 1.515 1.02 .9 1.515 2.325 1.08 2.91.825.09-.645.345-1.08.63-1.32-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.36.315.675.915.675 1.845 0 1.335-.015 2.415-.015 2.745 0 .33.225.705.84.57A12.015 12.015 0 0 0 24 12c0-6.63-5.37-12-12-12z" />
                </svg>
                GitHub
              </a>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

function App() {
  const [formStatus, setFormStatus] = useState('idle');
  
  const handleFormSubmit = async (e) => {
    e.preventDefault();
    setFormStatus('submitting');
    
    const formData = new FormData(e.target);
    formData.append("access_key", "54bea58c-6255-4d4e-adfb-f30a421d2dc8");
    formData.append("subject", "New Contact from Portfolio");
    
    try {
      const response = await fetch("https://api.web3forms.com/submit", {
        method: "POST",
        body: formData
      });
      const data = await response.json();
      
      if (data.success) {
        setFormStatus('success');
        e.target.reset();
        setTimeout(() => setFormStatus('idle'), 5000);
      } else {
        console.error("Error submitting form", data);
        setFormStatus('error');
        setTimeout(() => setFormStatus('idle'), 5000);
      }
    } catch (err) {
      console.error(err);
      setFormStatus('error');
      setTimeout(() => setFormStatus('idle'), 5000);
    }
  };

  const videoRef = useRef(null);
  const [isVideoPlaying, setIsVideoPlaying] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const toggleVideo = async () => {
    if (!videoRef.current) return;
    if (videoRef.current.paused) {
      try {
        await videoRef.current.play();
        setIsVideoPlaying(true);
      } catch (err) {
        console.error("Video playback failed:", err);
        setIsVideoPlaying(false);
      }
    } else {
      videoRef.current.pause();
      setIsVideoPlaying(false);
    }
  };
  const [loading, setLoading] = useState(true);
  const [scrolled, setScrolled] = useState(false);

  const projectsRef = useRef(null);
  const { scrollYProgress: projectsScrollYProgress } = useScroll({
    target: projectsRef,
    offset: ["start center", "end center"]
  });
  const pathLength = useSpring(projectsScrollYProgress, { stiffness: 60, damping: 20, restDelta: 0.001 });
  
  const contactRef = useRef(null);
  const { scrollYProgress: contactScrollYProgress } = useScroll({
    target: contactRef,
    offset: ["start end", "end start"]
  });
  const contactY = useTransform(contactScrollYProgress, [0, 1], ["-20%", "30%"]);

  useEffect(() => {
    AOS.init({ duration: 900, once: true });
    
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    
    const timer = setTimeout(() => {
      setLoading(false);
      setTimeout(() => AOS.refresh(), 100);
    }, 1100);
    
    return () => {
      window.removeEventListener('scroll', handleScroll);
      clearTimeout(timer);
    };
  }, []);

  return (
    <div className="bg-[#050505] min-h-screen overflow-x-hidden">
      <AnimatePresence>
        {loading && (
          <motion.div
            key="preloader"
            initial={{ y: 0 }}
            exit={{ y: "-100%" }}
            transition={{ duration: 0.75, ease: [0.76, 0, 0.24, 1] }}
            className="fixed inset-0 w-full h-[100dvh] bg-luxury-beige z-[100000] flex items-center justify-center pointer-events-none"
          >
            <motion.div
              exit={{ opacity: 0, scale: 0.95, y: -20 }}
              transition={{ duration: 0.35, ease: "easeOut" }}
              className="relative text-5xl md:text-7xl font-black tracking-tighter uppercase"
            >
              <div className="text-black/10">AKASH B</div>
              <motion.div
                className="absolute top-0 left-0 text-luxury-bg overflow-hidden whitespace-nowrap"
                initial={{ clipPath: "inset(100% 0 0 0)" }}
                animate={{ clipPath: "inset(0% 0 0 0)" }}
                transition={{ duration: 0.9, ease: "easeInOut", delay: 0.1 }}
              >
                AKASH B
              </motion.div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      <nav className={`fixed top-0 left-0 w-full z-50 transition-all duration-300 ${scrolled ? 'bg-[#050505]/85 backdrop-blur-md py-4 border-b border-white/10' : 'bg-transparent py-5 md:py-6'}`}>
        <div className="max-w-7xl mx-auto px-6 lg:px-12 flex justify-between items-center">
          <div className="flex items-center flex-shrink-0">
            <a href="#" className={`text-luxury-ivory text-2xl font-black tracking-tight whitespace-nowrap uppercase transition-opacity duration-300 ${scrolled ? 'opacity-100' : 'opacity-0 pointer-events-none'}`}>AKASH B</a>
          </div>
          <div className="hidden lg:flex space-x-8 flex-shrink-0">
            <a href="#home" className="text-luxury-ivory/80 hover:text-luxury-ivory font-medium relative group transition-colors duration-300 whitespace-nowrap">Home<span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-luxury-gold transition-all duration-300 group-hover:w-full"></span></a>
            <a href="#about" className="text-luxury-ivory/80 hover:text-luxury-ivory font-medium relative group transition-colors duration-300 whitespace-nowrap">About<span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-luxury-gold transition-all duration-300 group-hover:w-full"></span></a>
            <a href="#skills" className="text-luxury-ivory/80 hover:text-luxury-ivory font-medium relative group transition-colors duration-300 whitespace-nowrap">Skills<span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-luxury-gold transition-all duration-300 group-hover:w-full"></span></a>
            <a href="#projects" className="text-luxury-ivory/80 hover:text-luxury-ivory font-medium relative group transition-colors duration-300 whitespace-nowrap">Projects<span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-luxury-gold transition-all duration-300 group-hover:w-full"></span></a>
            <a href="#education" className="text-luxury-ivory/80 hover:text-luxury-ivory font-medium relative group transition-colors duration-300 whitespace-nowrap">Education<span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-luxury-gold transition-all duration-300 group-hover:w-full"></span></a>
            <a href="#experience" className="text-luxury-ivory/80 hover:text-luxury-ivory font-medium relative group transition-colors duration-300 whitespace-nowrap">Experience<span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-luxury-gold transition-all duration-300 group-hover:w-full"></span></a>
            <a href="#contact" className="text-luxury-ivory/80 hover:text-luxury-ivory font-medium relative group transition-colors duration-300 whitespace-nowrap">Contact<span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-luxury-gold transition-all duration-300 group-hover:w-full"></span></a>
          </div>
          <div className="hidden lg:block flex-shrink-0">
            <a href="#contact" className="px-6 py-2.5 rounded-full bg-white/10 border border-white/20 text-luxury-ivory font-semibold hover:bg-white/20 hover:shadow-[0_0_15px_rgba(255,255,255,0.2)] transition-all duration-300 backdrop-blur-md whitespace-nowrap">Hire Me</a>
          </div>
          <div className="lg:hidden flex items-center">
            <button onClick={() => setIsMenuOpen(!isMenuOpen)} className="text-luxury-ivory focus:outline-none p-2" aria-label="Toggle Navigation Menu" aria-expanded={isMenuOpen}>
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
            </button>
          </div>
        </div>
        <div className={`lg:hidden absolute top-full left-0 w-full transition-all duration-300 ${isMenuOpen ? "max-h-[85dvh] opacity-100 overflow-y-auto bg-luxury-bg/95 backdrop-blur-md pb-6 pt-2 border-b border-white/10" : "max-h-0 opacity-0 overflow-hidden pointer-events-none"}`}>
          <div className="flex flex-col px-6 space-y-4">
            <a href="#home" onClick={() => setIsMenuOpen(false)} className="text-luxury-ivory hover:text-luxury-gold font-bold text-lg border-b border-white/10 pb-2 transition-colors">Home</a>
            <a href="#about" onClick={() => setIsMenuOpen(false)} className="text-luxury-ivory hover:text-luxury-gold font-bold text-lg border-b border-white/10 pb-2 transition-colors">About</a>
            <a href="#skills" onClick={() => setIsMenuOpen(false)} className="text-luxury-ivory hover:text-luxury-gold font-bold text-lg border-b border-white/10 pb-2 transition-colors">Skills</a>
            <a href="#projects" onClick={() => setIsMenuOpen(false)} className="text-luxury-ivory hover:text-luxury-gold font-bold text-lg border-b border-white/10 pb-2 transition-colors">Projects</a>
            <a href="#education" onClick={() => setIsMenuOpen(false)} className="text-luxury-ivory hover:text-luxury-gold font-bold text-lg border-b border-white/10 pb-2 transition-colors">Education</a>
            <a href="#experience" onClick={() => setIsMenuOpen(false)} className="text-luxury-ivory hover:text-luxury-gold font-bold text-lg border-b border-white/10 pb-2 transition-colors">Experience</a>
            <a href="#contact" onClick={() => setIsMenuOpen(false)} className="text-luxury-ivory hover:text-luxury-gold font-bold text-lg border-b border-white/10 pb-2 transition-colors">Contact</a>
            <div className="pt-4 pb-2">
              <a href="#contact" onClick={() => setIsMenuOpen(false)} className="inline-block px-6 py-3 rounded-full bg-luxury-gold text-white font-black hover:bg-luxury-beige transition-colors w-full text-center shadow-lg">Hire Me</a>
            </div>
          </div>
        </div>
      </nav>

      <section id="home" className="relative w-full min-h-[100dvh] md:h-screen overflow-hidden bg-luxury-bg flex items-end md:block">
        <video loop playsInline preload="metadata" ref={videoRef} onEnded={() => setIsVideoPlaying(false)} className="absolute top-0 left-0 w-full h-full object-cover z-0">
          <source src="./assets/myselfvideo.mp4" type="video/mp4" />Your browser does not support the video tag.
        </video>
        <div className="absolute inset-0 bg-gradient-to-t from-[#050505]/90 via-[#050505]/45 to-[#050505]/30 z-10 pointer-events-none"></div>
        <div className="relative z-20 pt-28 pb-12 px-6 md:absolute md:inset-0 md:pt-0 md:pb-[8%] md:px-12 max-w-7xl mx-auto flex flex-col md:flex-row justify-end md:justify-between items-start md:items-end text-left w-full">
          <div className="flex flex-col items-start text-left max-w-2xl w-full">
            <h1 className="text-luxury-ivory text-3xl sm:text-4xl md:text-6xl font-black mb-2 tracking-tight">
              Hi, I’m <br /> <span className="text-luxury-ivory uppercase">AKASH B</span>
            </h1>
            <h2 className="text-luxury-gold text-base sm:text-lg md:text-2xl font-black mb-3 tracking-wider uppercase">
              Junior Full-Stack / Web Developer
            </h2>
            <p className="text-luxury-ivory/85 text-xs sm:text-sm md:text-base font-semibold mb-6 max-w-xl drop-shadow-md leading-relaxed">
              Full-Stack Web Developer with hands-on professional experience building and shipping responsive, modern web applications using Next.js, React, TypeScript, Tailwind CSS, and Supabase/PostgreSQL. Skilled at integrating third-party APIs (Razorpay, AI services), developing RESTful API endpoints, and delivering functional end-to-end web applications for real-world businesses.
            </p>
            <div className="flex flex-row flex-wrap items-center gap-2.5 md:gap-3 w-full">
              <a href="#projects" className="px-5 sm:px-6 py-3 text-xs md:text-sm rounded-full bg-luxury-ivory text-black font-bold hover:bg-gray-200 transition-all duration-300 transform hover:scale-105 shadow-md">View Projects</a>
              <a href="#contact" className="px-5 sm:px-6 py-3 text-xs md:text-sm rounded-full bg-luxury-bg/40 border border-white text-luxury-ivory font-bold hover:bg-luxury-bg/60 transition-all duration-300 backdrop-blur-md">Contact Me</a>
              <a href="./assets/Akash_B_Resume.pdf" target="_blank" rel="noopener noreferrer" className="px-5 sm:px-6 py-3 text-xs md:text-sm rounded-full bg-luxury-gold border border-luxury-gold text-white font-bold hover:bg-luxury-beige transition-all duration-300 backdrop-blur-md shadow-[0_0_15px_rgba(59,130,246,0.4)] hover:shadow-[0_0_25px_rgba(59,130,246,0.6)]">Preview Resume</a>
            </div>
          </div>
          <div onClick={toggleVideo} className="mt-8 md:mt-0 flex flex-row md:flex-col items-center gap-2 md:gap-3 cursor-pointer group self-start md:self-auto">
            <div className="w-12 h-12 md:w-20 md:h-20 rounded-full border border-white/30 bg-luxury-bg/20 backdrop-blur-md flex justify-center items-center group-hover:scale-110 group-hover:bg-[#67408a] transition-all duration-500 shadow-[0_0_30px_rgba(255,255,255,0.1)] group-hover:shadow-[0_0_40px_rgba(103,64,138,0.6)]">
              {isVideoPlaying ? (
                <svg className="w-5 h-5 md:w-8 md:h-8 text-luxury-ivory ml-0.5 md:ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"></path></svg>
              ) : (
                <svg className="w-5 h-5 md:w-8 md:h-8 text-luxury-ivory ml-0.5 md:ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"></path></svg>
              )}
            </div>
            <span className="text-luxury-ivory text-[10px] md:text-xs font-bold tracking-widest uppercase opacity-70 group-hover:opacity-100 transition-opacity">
              {isVideoPlaying ? "Pause Reel" : "Play Reel"}
            </span>
          </div>
        </div>
        <div data-aos="fade-up" data-aos-delay="800" className="hidden md:block absolute bottom-8 left-1/2 transform -translate-x-1/2 z-20 pointer-events-none aos-init">
          <div className="animate-bounce">
            <svg className="w-6 h-6 text-black drop-shadow-[0_1px_2px_rgba(255,255,255,0.6)]" fill="none" strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
            </svg>
          </div>
        </div>
      </section>

      <section id="about" className="bg-luxury-card pt-20 pb-40 px-6 md:px-12 w-full relative overflow-hidden font-sans border-b border-luxury-gold/10">
        <div className="absolute inset-0 bg-gradient-to-tr from-white/0 via-white/5 to-white/0 pointer-events-none z-10"></div>
        <div className="absolute top-0 left-1/4 w-[600px] h-[600px] bg-white/5 rounded-full filter blur-[120px] pointer-events-none z-0"></div>
        <div className="absolute bottom-0 right-1/4 w-[600px] h-[600px] bg-luxury-gold/10 rounded-full filter blur-[150px] pointer-events-none z-0"></div>
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row gap-16 items-start relative z-10">
          <div className="flex flex-col items-center w-full md:w-[350px] shrink-0 mt-12 md:mt-0">
            <div data-aos="drop-bounce" className="relative flex justify-center w-full aos-init">
              <div className="absolute -top-32 left-1/2 w-3 h-40 bg-luxury-bg transform -translate-x-1/2 shadow-inner z-0"></div>
              <div className="absolute -top-6 left-1/2 w-6 h-12 bg-gray-300 rounded border border-gray-400 transform -translate-x-1/2 z-10 shadow-[0_2px_10px_rgba(0,0,0,0.3)]"></div>
              <div className="bg-[#080808] w-full max-w-[280px] rounded-2xl p-4 shadow-[0_20px_40px_rgba(0,0,0,0.6)] relative z-20 transform -rotate-3 hover:rotate-0 transition-transform duration-500 text-luxury-ivory font-mono text-[10px] tracking-wider border border-luxury-gold/30">
                <div className="absolute -top-3 left-1/2 w-16 h-6 bg-[#080808] border-t border-l border-r border-luxury-gold/30 rounded-t-xl transform -translate-x-1/2 flex justify-center items-center">
                  <div className="w-8 h-2 bg-luxury-bg/30 rounded-full shadow-inner"></div>
                </div>
                <div className="w-full aspect-[3/4] overflow-hidden rounded-xl bg-luxury-card border border-gray-700 mb-3">
                  <img alt="Profile" className="w-full h-full object-cover grayscale contrast-125" src="./assets/mypicture.png" />
                </div>
                <div className="flex flex-col gap-1 border-t border-white/10 pt-2 opacity-90">
                  <p className="font-bold text-luxury-gold text-[11px] uppercase">AKASH B</p>
                  <p className="text-luxury-taupe uppercase">ROLE: JUNIOR FULL-STACK / WEB DEVELOPER</p>
                  <p className="text-luxury-taupe uppercase">SYS_ID: DEV-01</p>
                  <p className="text-emerald-400 font-bold uppercase">STATUS: ACTIVE // FULL_STACK_DEV</p>
                </div>
                <div className="mt-3 h-6 w-full bg-white relative overflow-hidden flex items-center justify-center rounded">
                  <div className="w-full h-full flex gap-[1.5px] items-center justify-center opacity-90 px-2 bg-white">
                    <div className="bg-luxury-bg h-4" style={{ width: '1px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '3px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '2px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '1px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '4px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '2px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '1px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '3px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '1px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '2px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '4px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '1px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '2px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '3px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '1px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '1px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '3px' }}></div>
                    <div className="bg-luxury-bg h-4" style={{ width: '2px' }}></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div data-aos="fade-up" data-aos-delay="200" className="flex-1 text-luxury-ivory mt-8 md:mt-0 relative z-20 aos-init">
            <h2 className="text-4xl md:text-5xl font-black text-luxury-ivory mb-4">Hello!</h2>
            <p className="text-lg font-bold mb-6 leading-relaxed max-w-3xl text-luxury-taupe">I am <span className="text-luxury-gold text-xl font-black mx-1 tracking-wide uppercase">AKASH B</span>, a Junior Full-Stack / Web Developer with hands-on professional experience building and shipping responsive, modern web applications.</p>
            <p className="text-sm md:text-base font-semibold leading-relaxed mb-6 max-w-3xl text-luxury-taupe">I specialize in full-stack web development with modern technologies including Next.js, React, TypeScript, Tailwind CSS, Node.js, and Supabase/PostgreSQL. Skilled at integrating third-party APIs (Razorpay, OpenAI, Gemini), developing RESTful API endpoints, and delivering functional end-to-end web applications for real-world businesses.</p>
            <p className="text-sm md:text-base font-semibold leading-relaxed mb-10 max-w-3xl text-luxury-taupe">Adept at building secure API integrations, automating workflows, and delivering seamless mobile-first user experiences across viewports.</p>
            <div className="flex flex-wrap items-center gap-3 md:gap-4 mt-6">
              {[
                { name: "React", src: "./assets/React.jpg" },
                { name: "Next.js", src: "./assets/Nestjs.jpg" },
                { name: "TypeScript", src: "./assets/Typescript.jpg" },
                { name: "JavaScript", src: "./assets/js.jpg" },
                { name: "Node.js", src: "./assets/nodejs.svg" },
                { name: "Python", src: "./assets/python.svg" },
                { name: "Tailwind CSS", src: "./assets/Tailwind.jpg" },
                { name: "HTML5", src: "./assets/Html.jpg" },
                { name: "CSS3", src: "./assets/css.jpg" },
                { name: "PHP", src: "./assets/php.jpg" },
                { name: "Java", src: "./assets/java.jpg" },
                { name: "PostgreSQL", src: "./assets/postgresql.svg" },
                { name: "MariaDB", src: "./assets/mariadb.svg" },
                { name: "MySQL", src: "./assets/MySql.jpg" },
                { name: "Supabase", src: "./assets/supabase.svg" },
                { name: "Prisma", src: "./assets/prisma.svg" },
                { name: "OpenAI", src: "./assets/openai.svg" },
                { name: "Gemini", src: "./assets/gemini.svg" },
                { name: "GitHub Actions", src: "./assets/githubactions.svg" },
                { name: "GitHub", src: "./assets/Github.jpg" },
                { name: "Git", src: "./assets/git-K6RyaU-h.png" },
                { name: "Postman", src: "./assets/postman.svg" },
                { name: "Vercel", src: "./assets/vercel.svg" },
              ].map((icon) => (
                <img
                  key={icon.name}
                  alt={icon.name}
                  title={icon.name}
                  loading="lazy"
                  className="w-14 h-14 sm:w-16 sm:h-16 md:w-[72px] md:h-[72px] object-contain hover:scale-110 transition-transform duration-300 cursor-pointer drop-shadow-lg bg-white/10 rounded-2xl p-2.5 md:p-3"
                  src={icon.src}
                />
              ))}
            </div>
          </div>
        </div>
        <div className="absolute bottom-0 left-0 w-full pointer-events-none z-30 transform translate-y-1">
          <svg viewBox="0 0 1200 120" preserveAspectRatio="none" className="w-full h-12 md:h-20 fill-luxury-bg">
            <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V120H0V95.8C59.71,118.08,130.83,119.62,189.5,99.8,242.79,81.82,282.88,63.6,321.39,56.44Z"></path>
          </svg>
        </div>
      </section>

      <section id="skills" className="bg-luxury-bg py-28 px-6 md:px-12 w-full relative overflow-hidden font-sans border-t border-luxury-card">
        <div className="max-w-6xl mx-auto mb-16 md:mb-20 text-center md:text-left">
          <div data-aos="fade-up" className="inline-block border border-white/10 rounded-full px-5 py-1.5 text-xs text-luxury-taupe font-bold uppercase tracking-widest mb-6">Core Competencies</div>
          <h2 data-aos="fade-up" data-aos-delay="100" className="text-4xl md:text-5xl lg:text-6xl font-black text-luxury-ivory leading-tight tracking-tight">Technical <br className="hidden md:block" /><span className="text-luxury-gold">Skills</span></h2>
        </div>
        <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 relative z-10">
          {skillsCategories.map((category, idx) => (
            <div key={category.title} className="col-span-1">
              <div
                data-aos="fade-up"
                data-aos-delay={(idx + 1) * 100}
                className="bg-[#111] border border-white/10 rounded-3xl p-6 sm:p-7 hover:border-luxury-gold hover:shadow-[0_10px_30px_rgba(59,130,246,0.15)] transition-all duration-500 flex flex-col h-full group"
              >
                <h3 className="text-lg font-bold text-luxury-ivory mb-5 border-b border-white/10 pb-3 flex items-center justify-between">
                  <span className="group-hover:text-luxury-gold transition-colors">{category.title}</span>
                  <span className={`w-2.5 h-2.5 rounded-full ${idx === 0 ? 'bg-luxury-gold animate-ping' : 'bg-luxury-gold/60'}`}></span>
                </h3>
                <div className="flex flex-wrap gap-2">
                  {category.skills.map(skill => (
                    <span
                      key={skill}
                      className="text-xs font-semibold px-3 py-1.5 bg-luxury-card border border-white/10 hover:border-luxury-gold/50 hover:text-luxury-gold hover:bg-luxury-bg rounded-full text-luxury-taupe transition-all duration-300 cursor-default"
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section id="projects" ref={projectsRef} className="bg-white pt-24 pb-32 px-6 md:px-12 w-full relative overflow-hidden font-sans bg-[linear-gradient(to_right,#8080800a_1px,transparent_1px),linear-gradient(to_bottom,#8080800a_1px,transparent_1px)] bg-[size:80px_80px]">
        <div className="max-w-6xl mx-auto relative md:h-[1580px]">
          <div data-aos="fade-up" className="md:absolute top-10 left-0 md:w-[450px] z-20 mb-16 md:mb-0">
            <div className="inline-block border border-gray-300 rounded-full px-5 py-1.5 text-xs text-gray-500 font-bold mb-6 shadow-sm bg-white uppercase tracking-widest">
              My Work
            </div>
            <h2 className="text-4xl md:text-5xl lg:text-6xl font-black text-gray-900 leading-[1.1] mb-6 tracking-tight relative">
              Technical Projects
            </h2>
            <p className="text-gray-500 text-sm md:text-base max-w-sm font-semibold leading-relaxed">
              Production platforms, AI health applications, and high-concurrency esports venue management architectures engineered for performance and scale.
            </p>
          </div>

          <svg className="hidden md:block absolute top-0 left-0 w-full h-[1480px] pointer-events-none z-0" viewBox="0 0 1000 1480" preserveAspectRatio="none">
            <path d="M 650,180 C 400,320 200,500 350,750 C 500,1050 400,1250 300,1450" fill="none" stroke="#e2e8f0" strokeWidth="2" strokeDasharray="8 10"></path>
            <mask id="path-mask">
              <motion.path d="M 650,180 C 400,320 200,500 350,750 C 500,1050 400,1250 300,1450" fill="none" stroke="white" strokeWidth="20" style={{ pathLength }} />
            </mask>
            <path d="M 650,180 C 400,320 200,500 350,750 C 500,1050 400,1250 300,1450" fill="none" stroke="#3b82f6" strokeWidth="3" strokeDasharray="8 10" mask="url(#path-mask)" className="drop-shadow-sm"></path>
          </svg>

          <svg className="md:hidden absolute top-0 left-[50%] -translate-x-1/2 w-4 h-[100%] pointer-events-none z-0" viewBox="0 0 4 100" preserveAspectRatio="none">
            <path d="M 2,0 L 2,100" fill="none" stroke="#e2e8f0" strokeWidth="4" strokeDasharray="4 6" vectorEffect="non-scaling-stroke"></path>
            <mask id="path-mask-mobile">
              <motion.path d="M 2,0 L 2,100" fill="none" stroke="white" strokeWidth="20" style={{ pathLength }} />
            </mask>
            <path d="M 2,0 L 2,100" fill="none" stroke="#3b82f6" strokeWidth="4" strokeDasharray="4 6" mask="url(#path-mask-mobile)" vectorEffect="non-scaling-stroke" className="drop-shadow-sm"></path>
          </svg>

          {projectsTimeline.map((exp, idx) => (
            <TimelineCard key={idx} exp={exp} pathLength={pathLength} containerRef={projectsRef} />
          ))}
        </div>
      </section>

      <section id="education" className="bg-[#111] py-28 px-6 md:px-12 w-full relative overflow-hidden font-sans border-t border-luxury-card">
        <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-10">
          <div>
            <div data-aos="fade-up" className="inline-block border border-white/10 rounded-full px-5 py-1.5 text-xs text-luxury-taupe font-bold uppercase tracking-widest mb-6">Education</div>
            <div data-aos="fade-up" className="bg-luxury-card/60 border border-white/10 rounded-3xl p-8 hover:border-luxury-gold transition-all duration-500">
              <h3 className="text-2xl font-black text-luxury-ivory mb-2">B.Sc. in Information Technology</h3>
              <p className="text-luxury-gold font-bold text-base mb-1">Guru Nanak College <span className="text-luxury-taupe font-normal">• Chennai, India</span></p>
              <p className="text-luxury-taupe text-sm font-semibold mb-4">June 2021 – May 2024</p>
              <div className="inline-flex items-center gap-2 px-3.5 py-1.5 bg-luxury-gold/10 border border-luxury-gold/30 rounded-full text-xs font-bold text-luxury-gold">
                <span className="w-2 h-2 rounded-full bg-luxury-gold"></span>
                CGPA: 7.0 / 10.0
              </div>
            </div>
          </div>
          <div>
            <div data-aos="fade-up" className="inline-block border border-white/10 rounded-full px-5 py-1.5 text-xs text-luxury-taupe font-bold uppercase tracking-widest mb-6">Certifications</div>
            <div data-aos="fade-up" className="bg-luxury-card/60 border border-white/10 rounded-3xl p-8 hover:border-luxury-gold transition-all duration-500">
              <h3 className="text-2xl font-black text-luxury-ivory mb-2">Java Full Stack Development Certification</h3>
              <p className="text-luxury-gold font-bold text-base mb-1">Besant Technologies <span className="text-luxury-taupe font-normal">• Chennai, India</span></p>
              <p className="text-luxury-taupe text-sm font-semibold mb-4">Comprehensive Enterprise Full-Stack Program</p>
              <div className="inline-flex items-center gap-2 px-3.5 py-1.5 bg-emerald-500/10 border border-emerald-500/30 rounded-full text-xs font-bold text-emerald-400">
                <span className="w-2 h-2 rounded-full bg-emerald-400"></span>
                Credential Verified
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="experience" className="bg-luxury-bg py-28 px-6 md:px-12 w-full relative overflow-hidden font-sans border-t border-luxury-card">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <div data-aos="fade-up" className="inline-block border border-luxury-gold/30 rounded-full px-5 py-1.5 text-xs text-luxury-gold font-bold uppercase tracking-widest mb-6 bg-luxury-card shadow-sm">Professional Career</div>
            <h2 data-aos="fade-up" data-aos-delay="100" className="text-4xl md:text-5xl font-black text-luxury-ivory mb-4">Work Experience</h2>
          </div>
          
          <div className="max-w-4xl mx-auto" data-aos="fade-up" data-aos-delay="200">
            <div className="bg-[#111] border border-white/10 rounded-[2rem] p-8 md:p-12 hover:border-luxury-gold hover:shadow-[0_10px_40px_rgba(59,130,246,0.15)] transition-all duration-500">
              <div className="flex flex-col md:flex-row md:justify-between md:items-start mb-6 gap-4 border-b border-white/10 pb-6">
                <div>
                  <h3 className="text-2xl md:text-3xl font-black text-luxury-ivory mb-1">Junior Web Developer</h3>
                  <p className="text-luxury-gold font-bold text-lg">The Atom <span className="text-luxury-taupe text-base font-normal">• Chennai, India</span></p>
                </div>
                <div className="bg-luxury-card px-4 py-2 rounded-full border border-white/5 self-start">
                  <span className="text-luxury-ivory text-sm font-bold tracking-wider">March 2025 – Present</span>
                </div>
              </div>

              <div className="flex flex-wrap items-center gap-2 mb-8">
                <span className="text-xs font-bold text-luxury-taupe uppercase tracking-wider mr-1">Tech Stack:</span>
                {["Next.js", "React", "TypeScript", "Tailwind CSS", "PHP", "MySQL", "PostgreSQL", "REST APIs", "Git"].map((tech) => (
                  <span key={tech} className="text-[11px] font-semibold px-3 py-1 bg-white/5 border border-white/10 rounded-full text-luxury-gold">
                    {tech}
                  </span>
                ))}
              </div>
              
              <div className="space-y-4">
                <h4 className="text-luxury-taupe font-bold uppercase tracking-widest text-xs mb-4">Key Contributions &amp; Impact</h4>
                <ul className="text-luxury-ivory/85 space-y-4 font-medium text-sm md:text-base">
                  <li className="flex items-start">
                    <span className="text-luxury-gold mr-3 mt-1 text-lg leading-none">•</span>
                    <span>Built and deployed responsive client websites and web applications using <strong className="text-luxury-ivory">Next.js, React, and Tailwind CSS</strong>.</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-luxury-gold mr-3 mt-1 text-lg leading-none">•</span>
                    <span>Developed REST API endpoints and connected relational databases (<strong className="text-luxury-ivory">MySQL, PostgreSQL</strong>) to handle dynamic client data.</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-luxury-gold mr-3 mt-1 text-lg leading-none">•</span>
                    <span>Integrated <strong className="text-luxury-ivory">Supabase storage</strong> for image/media uploads and built automated WhatsApp notification links to streamline client workflows.</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-luxury-gold mr-3 mt-1 text-lg leading-none">•</span>
                    <span>Collaborated on frontend UI components, ensuring smooth mobile-first responsiveness across all viewports.</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section ref={contactRef} id="contact" className="bg-[#0a0a0a] w-full min-h-screen relative overflow-hidden flex items-end pt-32 pb-0 md:pb-0 border-t border-luxury-card">
        <motion.div className="absolute top-0 left-0 w-full h-full flex flex-col justify-start items-center overflow-hidden pointer-events-none z-0 pt-16 md:pt-12" style={{ y: contactY }}>
          <h1 className="text-[25vw] leading-[0.75] font-black text-luxury-ivory uppercase tracking-tighter select-none scale-y-[1.6] origin-top" style={{ fontFamily: "'Impact', 'Arial Black', sans-serif" }}>Contact</h1>
        </motion.div>
        <div className="relative z-10 w-full flex justify-end items-end">
          <div data-aos="fade-up" className="bg-luxury-card/90 backdrop-blur-xl border-t border-l border-white/10 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.5)] w-full md:w-[85%] lg:w-[75%] p-8 md:p-16 rounded-t-[2.5rem] md:rounded-tr-none md:rounded-tl-[4rem] text-white flex flex-col justify-between min-h-[600px] transition-all duration-500">
            <div className="w-full flex flex-col justify-between h-full" style={{ opacity: '1', transform: 'none' }}>
              <div>
                <div className="text-xs font-bold tracking-[0.2em] mb-12 md:mb-16 uppercase text-luxury-gold">Reach Us</div>
              </div>
              <form onSubmit={handleFormSubmit} className="flex flex-col gap-12 md:gap-16 w-full">
                <div className="flex flex-col md:flex-row gap-12 md:gap-20 w-full">
                  <div className="flex-1 flex flex-col gap-10">
                    <div className="relative"><input id="firstName" name="firstName" required placeholder="First Name *" className="w-full bg-transparent border-b border-white/20 pb-3 text-lg focus:outline-none focus:border-luxury-gold transition-colors placeholder-gray-500 font-medium rounded-none disabled:opacity-50 text-white" type="text" /></div>
                    <div className="relative"><input id="lastName" name="lastName" placeholder="Last Name" className="w-full bg-transparent border-b border-white/20 pb-3 text-lg focus:outline-none focus:border-luxury-gold transition-colors placeholder-gray-500 font-medium rounded-none disabled:opacity-50 text-white" type="text" /></div>
                    <div className="relative"><input id="email" name="email" required placeholder="Email *" className="w-full bg-transparent border-b border-white/20 pb-3 text-lg focus:outline-none focus:border-luxury-gold transition-colors placeholder-gray-500 font-medium rounded-none disabled:opacity-50 text-white" type="email" /></div>
                  </div>
                  <div className="flex-1 flex flex-col">
                    <div className="relative h-full flex flex-col"><textarea id="message" name="message" required placeholder="Type your message here *" className="w-full h-full min-h-[120px] bg-transparent border-b border-white/20 pb-3 text-lg focus:outline-none focus:border-luxury-gold transition-colors placeholder-gray-500 font-medium resize-none rounded-none disabled:opacity-50 text-white"></textarea></div>
                  </div>
                </div>
                <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-8 mt-4">
                  <button disabled={formStatus === 'submitting'} className="group relative inline-flex items-center gap-4 text-xl md:text-2xl font-black uppercase tracking-tight hover:text-luxury-gold transition-colors disabled:opacity-50 text-white" type="submit">
                    {formStatus === 'submitting' ? 'Sending...' : formStatus === 'success' ? 'Message Sent!' : formStatus === 'error' ? 'Error, Try Again' : 'Send Message'}
                    <span className="w-12 h-12 rounded-full bg-luxury-gold flex items-center justify-center text-white group-hover:scale-110 transition-transform duration-500">
                      {formStatus === 'success' ? (
                        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M5 13l4 4L19 7"></path></svg>
                      ) : (
                        <svg className="w-5 h-5 translate-x-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                      )}
                    </span>
                  </button>
                  <div className="flex gap-4">
                    <a href="https://github.com/akashit2408-cloud" target="_blank" rel="noopener noreferrer" aria-label="GitHub" className="w-12 h-12 rounded-full border border-white/20 flex items-center justify-center text-white hover:bg-luxury-gold hover:text-white hover:border-luxury-gold transition-all duration-300">
                      <svg className="w-5 h-5" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-3.975-1.395-.03-.075-.315-.825-.765-1.125-.345-.165-.825-.615-.015-.63.78-.015 1.335.72 1.515 1.02 .9 1.515 2.325 1.08 2.91.825.09-.645.345-1.08.63-1.32-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.36.315.675.915.675 1.845 0 1.335-.015 2.415-.015 2.745 0 .33.225.705.84.57A12.015 12.015 0 0 0 24 12c0-6.63-5.37-12-12-12z"></path></svg>
                    </a>
                    <a href="https://www.linkedin.com/in/akash-b-504659283/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" className="w-12 h-12 rounded-full border border-white/20 flex items-center justify-center text-white hover:bg-luxury-gold hover:text-white hover:border-luxury-gold transition-all duration-300">
                      <svg className="w-5 h-5" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"></path></svg>
                    </a>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </section>

      <footer className="bg-[#111111] text-[#d4d4d4] py-16 px-6 md:px-12 w-full font-mono text-[10px] md:text-xs tracking-widest flex flex-col justify-between min-h-[50vh] border-t border-luxury-card">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-12 md:gap-8 w-full font-medium">
          <div className="flex flex-col gap-1">
            <p className="text-luxury-gold font-bold mb-1 uppercase tracking-widest">// PROFILE</p>
            <p>Akash B</p>
            <p>Junior Full-Stack / Web Developer</p>
          </div>
          <div className="flex flex-col gap-1 md:items-center">
            <p className="text-luxury-gold font-bold mb-1 uppercase tracking-widest">// NAVIGATE</p>
            <a href="#projects" className="underline hover:text-luxury-ivory transition-colors mt-1 underline-offset-4 decoration-1">Projects</a>
            <a href="#experience" className="underline hover:text-luxury-ivory transition-colors mt-1 underline-offset-4 decoration-1">Experience</a>
          </div>
          <div className="flex flex-col gap-1 md:items-end">
            <p className="text-luxury-gold font-bold mb-1 uppercase tracking-widest">// LOCATION</p>
            <p>Chennai, India</p>
            <p>2026</p>
          </div>
        </div>
        <div className="w-full flex justify-center items-center py-20 md:py-24 overflow-hidden">
          <h2 data-aos="fade-up" data-aos-delay="100" className="text-[18vw] md:text-[16vw] leading-none font-sans font-bold tracking-tighter select-none text-[#f4f4f4] w-full text-center uppercase">
            Akash B
          </h2>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-12 md:gap-8 w-full items-end font-medium">
          <div className="flex flex-col gap-4">
            <a href="#contact" className="underline hover:text-luxury-ivory transition-colors underline-offset-4 decoration-1 font-bold">Get In Touch</a>
            <p className="text-luxury-ivory/60 font-mono text-[9px] md:text-[10px]">© 2026 Akash B | Junior Full-Stack / Web Developer</p>
          </div>
          <div className="flex flex-col gap-1 md:items-center">
            <a href="mailto:akashit2408@gmail.com" className="underline hover:text-luxury-ivory transition-colors underline-offset-4 decoration-1 lowercase">akashit2408@gmail.com</a>
            <a href="tel:+918248590767" className="text-luxury-ivory/60 hover:text-luxury-ivory transition-colors mt-1">+91 8248590767</a>
          </div>
          <div className="flex flex-col gap-2 md:items-end font-bold text-luxury-ivory">
            <a href="https://github.com/akashit2408-cloud" target="_blank" rel="noopener noreferrer" className="underline hover:text-luxury-gold transition-colors underline-offset-4 decoration-1">GitHub</a>
            <a href="https://www.linkedin.com/in/akash-b-504659283/" target="_blank" rel="noopener noreferrer" className="underline hover:text-luxury-gold transition-colors underline-offset-4 decoration-1">LinkedIn</a>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
