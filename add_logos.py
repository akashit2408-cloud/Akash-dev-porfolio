import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add activeImage state
if 'const [activeImage, setActiveImage] = useState(null);' not in content:
    content = content.replace(
        'const [activeVideo, setActiveVideo] = useState(null);',
        'const [activeVideo, setActiveVideo] = useState(null);\n  const [activeImage, setActiveImage] = useState(null);'
    )

# 2. Add portfolioLogos array right after portfolioVideos
logos_array = """
const portfolioLogos = [
  {
    title: "ML Logo",
    url: "https://ifwibdbxfsgzhcuctdjw.supabase.co/storage/v1/object/public/folder/ppn/LOGO's/ML/ML-LOGO-V1-17.png"
  },
  {
    title: "Smart Pura",
    url: "https://ifwibdbxfsgzhcuctdjw.supabase.co/storage/v1/object/public/folder/ppn/LOGO's/SMART%20PURA/SP-PRESENTATION%201-18-15.jpg"
  },
  {
    title: "Buzz Creations",
    url: "https://ifwibdbxfsgzhcuctdjw.supabase.co/storage/v1/object/public/folder/ppn/LOGO's/Buzz%20Creations/with%20text-01-01.png"
  }
];
"""

if 'const portfolioLogos = [' not in content:
    content = content.replace(
        'const portfolioVideos = [',
        logos_array + '\nconst portfolioVideos = ['
    )

# 3. Add Logo grid in the Projects section
# Find the end of the video grid
video_grid_end = """          ))}
        </div>"""

logo_grid_jsx = """
        <div className="mt-20 mb-8 text-center">
          <h3 data-aos="fade-up" className="text-2xl md:text-3xl font-black text-luxury-ivory">Logo & Branding</h3>
          <div className="w-16 h-1 bg-luxury-gold mx-auto mt-4 rounded-full"></div>
        </div>
        
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">
          {portfolioLogos.map((logo, idx) => (
            <div key={idx} onClick={() => setActiveImage(logo)} data-aos="fade-up" data-aos-delay={100 + (idx * 100)} className="group cursor-pointer relative rounded-2xl overflow-hidden bg-luxury-card border border-white/5 shadow-2xl hover:border-luxury-gold/40 hover:shadow-[0_0_30px_rgba(212,175,55,0.15)] transition-all duration-500 aspect-square flex flex-col items-center">
              <div className="absolute inset-0 bg-black/40 group-hover:bg-transparent transition-colors duration-500 z-10"></div>
              <img src={logo.url} alt={logo.title} className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
              
              <div className="absolute bottom-0 left-0 w-full p-6 bg-gradient-to-t from-black/90 via-black/50 to-transparent z-20 translate-y-2 group-hover:translate-y-0 transition-transform duration-500">
                <h3 className="text-lg font-black text-luxury-ivory group-hover:text-luxury-gold transition-colors duration-500">{logo.title}</h3>
                <span className="text-[10px] font-bold uppercase tracking-widest text-luxury-taupe group-hover:text-luxury-ivory transition-colors duration-500">View Logo</span>
              </div>
            </div>
          ))}
        </div>
"""

# Insert logo grid after video grid
if 'Logo & Branding' not in content:
    # First, let's add a small heading for Videos if we want, or just insert Logos below.
    # The user has title "Design Portfolio". I'll just add Logos below videos.
    content = content.replace(
        video_grid_end,
        video_grid_end + '\n' + logo_grid_jsx
    )


# 4. Add Image Modal (similar to Video Modal) at the very bottom
image_modal_jsx = """
      {/* Image Modal */}
      {activeImage && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center bg-black/95 backdrop-blur-md p-4 md:p-12" onClick={() => setActiveImage(null)}>
          <div className="relative w-full max-w-5xl bg-luxury-card rounded-2xl overflow-hidden shadow-[0_0_50px_rgba(212,175,55,0.15)] border border-luxury-gold/30" onClick={(e) => e.stopPropagation()}>
            <button onClick={() => setActiveImage(null)} className="absolute top-4 right-4 z-20 text-white bg-black/50 hover:bg-luxury-gold hover:text-black rounded-full p-2 transition-colors">
              <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" /></svg>
            </button>
            <div className="w-full h-[80vh] flex items-center justify-center p-4">
              <img src={activeImage.url} alt={activeImage.title} className="max-w-full max-h-full object-contain rounded" />
            </div>
          </div>
        </div>
      )}
"""

if '{/* Image Modal */}' not in content:
    content = content.replace(
        '{/* Video Modal */}',
        image_modal_jsx + '\n      {/* Video Modal */}'
    )

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added logos to Portfolio")
