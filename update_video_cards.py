import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_video_card = """          {portfolioVideos.map((video, idx) => (
            <div key={idx} onClick={() => setActiveVideo(video)} data-aos="fade-up" data-aos-delay={100 + (idx * 100)} className="group cursor-pointer relative rounded-2xl overflow-hidden bg-luxury-card border border-white/5 shadow-2xl hover:border-luxury-gold/40 hover:shadow-[0_0_30px_rgba(212,175,55,0.15)] transition-all duration-500 min-h-[250px] md:min-h-[300px] flex flex-col justify-center items-center text-center p-8">
              <div className="absolute inset-0 bg-gradient-to-br from-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
              
              <div className="w-16 h-16 md:w-20 md:h-20 rounded-full border border-white/10 bg-luxury-bg/50 flex items-center justify-center mb-6 group-hover:bg-luxury-gold group-hover:border-luxury-gold transition-all duration-500 group-hover:scale-110 shadow-lg relative z-10">
                <svg className="w-6 h-6 md:w-8 md:h-8 text-luxury-ivory group-hover:text-black ml-1 md:ml-1.5 transition-colors duration-500" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </div>
              
              <h3 className="text-xl md:text-2xl font-black text-luxury-ivory group-hover:text-luxury-gold transition-colors duration-500 relative z-10">{video.title}</h3>
              <span className="mt-4 text-[10px] md:text-xs font-bold uppercase tracking-[0.2em] text-luxury-taupe group-hover:text-luxury-ivory transition-colors duration-500 relative z-10">Watch Video</span>
            </div>
          ))}"""

new_video_card = """          {portfolioVideos.map((video, idx) => (
            <div key={idx} onClick={() => setActiveVideo(video)} data-aos="fade-up" data-aos-delay={100 + (idx * 100)} className="group cursor-pointer relative rounded-2xl overflow-hidden bg-luxury-card border border-white/5 shadow-2xl hover:border-luxury-gold/40 hover:shadow-[0_0_30px_rgba(212,175,55,0.15)] transition-all duration-500 min-h-[250px] md:min-h-[300px] flex flex-col justify-center items-center text-center p-8">
              
              <video autoPlay loop muted playsInline className="absolute inset-0 w-full h-full object-cover opacity-50 group-hover:opacity-70 transition-opacity duration-700 blur-[3px] group-hover:blur-sm scale-110 group-hover:scale-105">
                <source src={video.url} type="video/mp4" />
              </video>
              <div className="absolute inset-0 bg-black/60 group-hover:bg-black/40 transition-colors duration-500 z-0"></div>

              <div className="w-16 h-16 md:w-20 md:h-20 rounded-full border border-white/20 bg-black/60 backdrop-blur-md flex items-center justify-center mb-6 group-hover:bg-luxury-gold group-hover:border-luxury-gold transition-all duration-500 group-hover:scale-110 shadow-[0_0_20px_rgba(0,0,0,0.5)] relative z-10">
                <svg className="w-6 h-6 md:w-8 md:h-8 text-luxury-ivory group-hover:text-black ml-1 md:ml-1.5 transition-colors duration-500" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </div>
              
              <span className="mt-2 text-[10px] md:text-xs font-bold uppercase tracking-[0.25em] text-luxury-ivory group-hover:text-black transition-colors duration-500 relative z-10 bg-black/60 group-hover:bg-luxury-gold px-6 py-2.5 rounded-full backdrop-blur-md border border-white/10 group-hover:border-luxury-gold shadow-lg">Watch Video</span>
            </div>
          ))}"""

content = content.replace(old_video_card, new_video_card)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated video cards styling")
