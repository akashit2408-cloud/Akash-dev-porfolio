import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert the ExperienceCard component entirely
old_card_start = 'const ExperienceCard = ({ exp, pathLength, containerRef }) => {'
old_card_end = '};\n\n\n\nfunction App() {'

new_card_code = """const ExperienceCard = ({ exp, pathLength, containerRef }) => {
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
    <div ref={d} data-aos={exp.aosType} data-aos-delay={exp.aosDelay} className={`w-80 sm:w-96 rounded-[2rem] p-2 relative flex flex-col items-center hover:scale-[1.01] transition-all duration-700 z-10 ${exp.className} ${f ? 'bg-[#67408a] shadow-[0_20px_50px_rgba(103,64,138,0.4)]' : 'bg-white border border-gray-200 shadow-[0_15px_40px_rgba(0,0,0,0.06)] hover:shadow-[0_20px_50px_rgba(0,0,0,0.12)]'}`}>
      <div className={`w-5 h-5 bg-gradient-to-br from-gray-300 to-gray-100 rounded-full shadow-[inset_0_2px_4px_rgba(0,0,0,0.3)] absolute top-4 border border-gray-300 z-10 flex items-center justify-center`}>
        <div className={`w-2 h-2 rounded-full ${f ? 'bg-white' : 'bg-gray-400'}`}></div>
      </div>
      <div className={`w-full h-full rounded-[1.5rem] mt-8 p-6 flex flex-col min-h-[300px] transition-colors duration-700 ${f ? 'bg-white/10' : 'bg-[#f8f8f8]'}`}>
        <div className="flex justify-between items-center mb-3">
          <span className={`text-base font-bold font-serif italic transition-colors duration-700 ${f ? 'text-white/70' : 'text-gray-400'}`}>{exp.number}</span>
          <span className={`text-[10px] font-bold tracking-wider uppercase transition-colors duration-700 ${f ? 'text-white/70' : 'text-gray-400'}`}>{exp.period}</span>
        </div>
        <h3 className={`text-xl font-black mb-1 tracking-tight transition-colors duration-700 ${f ? 'text-white' : 'text-gray-900'}`}>{exp.role}</h3>
        <h4 className={`text-xs font-bold uppercase tracking-wider mb-4 transition-colors duration-700 ${f ? 'text-white/80' : 'text-gray-500'}`}>{exp.company}</h4>
        <ul className={`text-xs leading-relaxed font-medium mb-5 list-disc pl-4 flex-grow flex flex-col gap-2 transition-colors duration-700 ${f ? 'text-white/80' : 'text-gray-600'}`}>
          {exp.details.map((e, t) => <li key={t}>{e}</li>)}
        </ul>
        <div className="flex flex-wrap gap-1 mt-auto pt-3 border-t border-dashed border-gray-300/40">
          {exp.tags.map((e, t) => (
            <span key={t} className={`text-[9px] font-bold px-2.5 py-1 rounded transition-colors duration-700 ${f ? 'bg-white/10 text-white/90 border border-white/20' : 'bg-white text-gray-700 border border-gray-200 shadow-sm'}`}>
              {e}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
};"""

content = re.sub(
    r'const ExperienceCard = \({ exp, pathLength, containerRef }\) => \{.*?\};\s*function App\(\) \{',
    new_card_code + '\n\n\nfunction App() {',
    content,
    flags=re.DOTALL
)

# 2. Revert the Experience section container
content = content.replace(
    'className="bg-luxury-bg pt-24 pb-32 px-6 md:px-12 w-full relative overflow-hidden font-sans bg-[linear-gradient(to_right,#ffffff0a_1px,transparent_1px),linear-gradient(to_bottom,#ffffff0a_1px,transparent_1px)] bg-[size:80px_80px]"',
    'className="bg-white pt-24 pb-32 px-6 md:px-12 w-full relative overflow-hidden font-sans bg-[linear-gradient(to_right,#8080800a_1px,transparent_1px),linear-gradient(to_bottom,#8080800a_1px,transparent_1px)] bg-[size:80px_80px]"'
)

# 3. Revert the Timeline badge
content = content.replace(
    'className="inline-block border border-luxury-gold/30 rounded-full px-5 py-1.5 text-xs text-luxury-gold font-bold mb-6 shadow-sm bg-luxury-card uppercase tracking-widest"',
    'className="inline-block border border-gray-300 rounded-full px-5 py-1.5 text-xs text-gray-500 font-bold mb-6 shadow-sm bg-white uppercase tracking-widest"'
)
# (In case my previous replace was slightly different, let's just use regex)
content = re.sub(
    r'className="inline-block border[^"]+uppercase tracking-widest">\s*Timeline\s*</div>',
    'className="inline-block border border-gray-300 rounded-full px-5 py-1.5 text-xs text-gray-500 font-bold mb-6 shadow-sm bg-white uppercase tracking-widest">\n            Timeline\n          </div>',
    content
)

# 4. Revert "Professional Experience" header
content = content.replace(
    'className="text-4xl md:text-5xl lg:text-6xl font-black text-luxury-ivory leading-[1.1] mb-6 tracking-tight relative"',
    'className="text-4xl md:text-5xl lg:text-6xl font-black text-gray-900 leading-[1.1] mb-6 tracking-tight relative"'
)

# 5. Revert the paragraph under the header
content = content.replace(
    'text-luxury-taupe text-sm md:text-base max-w-sm font-semibold leading-relaxed',
    'text-gray-500 text-sm md:text-base max-w-sm font-semibold leading-relaxed'
)


with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted experience section to light theme")
