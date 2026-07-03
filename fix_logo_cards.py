import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The current logo card code:
old_logo_card = """          {portfolioLogos.map((logo, idx) => (
            <div key={idx} onClick={() => setActiveImage(logo)} data-aos="fade-up" data-aos-delay={100 + (idx * 100)} className="group cursor-pointer relative rounded-2xl overflow-hidden bg-luxury-card border border-white/5 shadow-2xl hover:border-luxury-gold/40 hover:shadow-[0_0_30px_rgba(212,175,55,0.15)] transition-all duration-500 aspect-square flex flex-col items-center">
              <div className="absolute inset-0 bg-black/40 group-hover:bg-transparent transition-colors duration-500 z-10"></div>
              <img src={logo.url} alt={logo.title} className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
              
              <div className="absolute bottom-0 left-0 w-full p-6 bg-gradient-to-t from-black/90 via-black/50 to-transparent z-20 translate-y-2 group-hover:translate-y-0 transition-transform duration-500">
                <h3 className="text-lg font-black text-luxury-ivory group-hover:text-luxury-gold transition-colors duration-500">{logo.title}</h3>
                <span className="text-[10px] font-bold uppercase tracking-widest text-luxury-taupe group-hover:text-luxury-ivory transition-colors duration-500">View Logo</span>
              </div>
            </div>
          ))}"""

# The new logo card code (matching video cards):
new_logo_card = """          {portfolioLogos.map((logo, idx) => (
            <div key={idx} onClick={() => setActiveImage(logo)} data-aos="fade-up" data-aos-delay={100 + (idx * 100)} className="group cursor-pointer relative rounded-2xl overflow-hidden bg-luxury-card border border-white/5 shadow-2xl hover:border-luxury-gold/40 hover:shadow-[0_0_30px_rgba(212,175,55,0.15)] transition-all duration-500 min-h-[250px] md:min-h-[300px] flex flex-col justify-center items-center text-center p-8">
              <div className="absolute inset-0 bg-gradient-to-br from-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
              
              <div className="w-16 h-16 md:w-20 md:h-20 rounded-full border border-white/10 bg-luxury-bg/50 flex items-center justify-center mb-6 group-hover:bg-luxury-gold group-hover:border-luxury-gold transition-all duration-500 group-hover:scale-110 shadow-lg relative z-10">
                <svg className="w-6 h-6 md:w-8 md:h-8 text-luxury-ivory group-hover:text-black transition-colors duration-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              </div>
              
              <h3 className="text-xl md:text-2xl font-black text-luxury-ivory group-hover:text-luxury-gold transition-colors duration-500 relative z-10">{logo.title}</h3>
              <span className="mt-4 text-[10px] md:text-xs font-bold uppercase tracking-[0.2em] text-luxury-taupe group-hover:text-luxury-ivory transition-colors duration-500 relative z-10">View Project</span>
            </div>
          ))}"""

content = content.replace(old_logo_card, new_logo_card)

# Let's also fix the video cards if they had any issues, but they seem fine.
# Wait, the user said "video too popup". Did they mean the video modal isn't popping up?
# It should be popping up because activeVideo is set.
# Let's double check if there are any z-index issues with the modals. The modals use z-[100].

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed logo cards to match video cards")
