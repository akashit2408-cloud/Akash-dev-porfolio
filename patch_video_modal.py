import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add activeVideo state to App component
if 'const [activeVideo, setActiveVideo] = useState(null);' not in content:
    content = content.replace(
        'const [isVideoPlaying, setIsVideoPlaying] = useState(true);',
        'const [isVideoPlaying, setIsVideoPlaying] = useState(true);\n  const [activeVideo, setActiveVideo] = useState(null);'
    )
    # also replace the false case just in case
    content = content.replace(
        'const [isVideoPlaying, setIsVideoPlaying] = useState(false);',
        'const [isVideoPlaying, setIsVideoPlaying] = useState(false);\n  const [activeVideo, setActiveVideo] = useState(null);'
    )

# 2. Add the Modal at the very end of App component, right before the closing </AnimatePresence> or final </div>
# Wait, the easiest place to add the modal is right before the final `</div>` of the App return.
# Let's find `export default App;` and trace back, or just inject it right after the footer.
modal_code = """
      {/* Video Modal */}
      {activeVideo && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center bg-black/95 backdrop-blur-md p-4 md:p-12" onClick={() => setActiveVideo(null)}>
          <div className="relative w-full max-w-6xl aspect-video bg-black rounded-2xl overflow-hidden shadow-[0_0_50px_rgba(212,175,55,0.15)] border border-luxury-gold/30" onClick={(e) => e.stopPropagation()}>
            <button onClick={() => setActiveVideo(null)} className="absolute top-4 right-4 z-20 text-white bg-black/50 hover:bg-luxury-gold hover:text-black rounded-full p-2 transition-colors">
              <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" /></svg>
            </button>
            <video controls autoPlay className="w-full h-full object-contain">
              <source src={activeVideo.url} type="video/mp4" />
              Your browser does not support the video tag.
            </video>
          </div>
        </div>
      )}
"""
if '{/* Video Modal */}' not in content:
    content = content.replace(
        '  return (\n    <div className',
        '  return (\n    <div className'
    ) # just testing
    # A safe place to put the modal is right after <AnimatePresence> or inside the main div.
    # Let's insert it right after the opening <div className="font-sans text-gray-900 bg-white">
    # Wait, the main wrapper is <div className="font-sans ...">
    content = re.sub(
        r'(return\s*\(\s*<div[^>]*>)',
        r'\1' + modal_code,
        content,
        count=1
    )

# 3. Replace the Projects grid content
old_grid = r'<div className="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12">[\s\S]*?</div>\s*</div>\s*</section>'

new_grid = """<div className="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12">
          {portfolioVideos.map((video, idx) => (
            <div key={idx} onClick={() => setActiveVideo(video)} data-aos="fade-up" data-aos-delay={100 + (idx * 100)} className="group cursor-pointer relative rounded-2xl overflow-hidden bg-luxury-card border border-white/5 shadow-2xl hover:border-luxury-gold/40 hover:shadow-[0_0_30px_rgba(212,175,55,0.15)] transition-all duration-500 min-h-[250px] md:min-h-[300px] flex flex-col justify-center items-center text-center p-8">
              <div className="absolute inset-0 bg-gradient-to-br from-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
              
              <div className="w-16 h-16 md:w-20 md:h-20 rounded-full border border-white/10 bg-luxury-bg/50 flex items-center justify-center mb-6 group-hover:bg-luxury-gold group-hover:border-luxury-gold transition-all duration-500 group-hover:scale-110 shadow-lg relative z-10">
                <svg className="w-6 h-6 md:w-8 md:h-8 text-luxury-ivory group-hover:text-black ml-1 md:ml-1.5 transition-colors duration-500" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </div>
              
              <h3 className="text-xl md:text-2xl font-black text-luxury-ivory group-hover:text-luxury-gold transition-colors duration-500 relative z-10">{video.title}</h3>
              <span className="mt-4 text-[10px] md:text-xs font-bold uppercase tracking-[0.2em] text-luxury-taupe group-hover:text-luxury-ivory transition-colors duration-500 relative z-10">Watch Video</span>
            </div>
          ))}
        </div>
      </div>
    </section>"""

content = re.sub(old_grid, new_grid, content)


with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched projects to use modal instead of inline video")
