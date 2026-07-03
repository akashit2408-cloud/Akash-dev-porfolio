import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add the videos array near the top of the file, after the experiences array
videos_array = """
const portfolioVideos = [
  {
    title: "Project 1",
    url: "https://ifwibdbxfsgzhcuctdjw.supabase.co/storage/v1/object/public/folder/ppn/videos/19-06-2026%20part%202.mp4"
  },
  {
    title: "Content DM",
    url: "https://ifwibdbxfsgzhcuctdjw.supabase.co/storage/v1/object/public/folder/ppn/videos/content%20dm.mp4"
  },
  {
    title: "Navy Webinar",
    url: "https://ifwibdbxfsgzhcuctdjw.supabase.co/storage/v1/object/public/folder/ppn/videos/NAVY%20WEBINAR.mp4"
  },
  {
    title: "Simp 1.1",
    url: "https://ifwibdbxfsgzhcuctdjw.supabase.co/storage/v1/object/public/folder/ppn/videos/simp1.1.mp4"
  }
];
"""

if 'const portfolioVideos' not in content:
    content = content.replace(
        'function App() {',
        videos_array + '\nfunction App() {'
    )


# The old projects section
old_projects = r'<section id="projects"[\s\S]*?className="bg-\[#0a0a0a\] py-28 px-6 md:px-12 w-full relative overflow-hidden font-sans border-t border-luxury-card flex items-center justify-center min-h-\[50vh\]">[\s\S]*?<div className="text-center">[\s\S]*?<h2 data-aos="fade-up" className="text-4xl md:text-5xl font-black text-luxury-ivory mb-4">Design Portfolio</h2>[\s\S]*?<p data-aos="fade-up" data-aos-delay="100" className="text-luxury-taupe text-lg">My creative projects and visual showcase will be updated here soon.</p>[\s\S]*?</div>[\s\S]*?</section>'

new_projects = """<section id="projects"
      className="bg-luxury-bg py-28 px-6 md:px-12 w-full relative overflow-hidden font-sans border-t border-luxury-card min-h-[50vh]">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <div data-aos="fade-up" className="inline-block border border-luxury-gold/30 rounded-full px-5 py-1.5 text-xs text-luxury-gold font-bold uppercase tracking-widest mb-6 bg-luxury-card shadow-sm">My Work</div>
          <h2 data-aos="fade-up" data-aos-delay="100" className="text-4xl md:text-5xl font-black text-luxury-ivory mb-4">Design Portfolio</h2>
          <p data-aos="fade-up" data-aos-delay="200" className="text-luxury-taupe text-lg max-w-2xl mx-auto">A selection of my best video edits, motion graphics, and visual storytelling projects.</p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12">
          {portfolioVideos.map((video, idx) => (
            <div key={idx} data-aos="fade-up" data-aos-delay={100 + (idx * 100)} className="group relative rounded-2xl overflow-hidden bg-luxury-card border border-white/5 shadow-2xl hover:border-luxury-gold/40 transition-all duration-500">
              <div className="aspect-video w-full relative bg-black flex items-center justify-center">
                <video 
                  controls 
                  preload="metadata" 
                  className="w-full h-full object-contain"
                  style={{ maxHeight: '100%' }}
                >
                  <source src={video.url} type="video/mp4" />
                  Your browser does not support the video tag.
                </video>
              </div>
              <div className="p-6 border-t border-white/5">
                <h3 className="text-xl font-bold text-luxury-ivory group-hover:text-luxury-gold transition-colors">{video.title}</h3>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>"""

content = re.sub(old_projects, new_projects, content)


with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Projects section patched with videos")
