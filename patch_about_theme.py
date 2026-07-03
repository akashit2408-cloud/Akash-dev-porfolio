import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Background gradient -> bg-luxury-card
content = content.replace(
    'className="bg-gradient-to-br from-[#67408a] via-[#523173] to-[#352151] pt-20 pb-40 px-6 md:px-12 w-full relative overflow-hidden font-sans"',
    'className="bg-luxury-card pt-20 pb-40 px-6 md:px-12 w-full relative overflow-hidden font-sans border-b border-luxury-gold/10"'
)

# 2. Hello! heading text-black -> text-luxury-ivory
content = content.replace(
    '<h2 className="text-4xl md:text-5xl font-black text-black mb-4">Hello!</h2>',
    '<h2 className="text-4xl md:text-5xl font-black text-luxury-ivory mb-4">Hello!</h2>'
)

# 3. I am Narayanan R span text-black -> text-luxury-gold
content = content.replace(
    'className="text-black text-xl font-black mx-1 tracking-wide uppercase">NARAYANAN R</span>',
    'className="text-luxury-gold text-xl font-black mx-1 tracking-wide uppercase">NARAYANAN R</span>'
)

# 4. Text paragraphs text-luxury-beige -> text-luxury-taupe
content = content.replace(
    'text-lg font-bold mb-8 leading-relaxed max-w-3xl text-luxury-beige',
    'text-lg font-bold mb-8 leading-relaxed max-w-3xl text-luxury-taupe'
)
content = content.replace(
    'text-sm md:text-base font-semibold leading-relaxed mb-6 max-w-3xl text-luxury-beige',
    'text-sm md:text-base font-semibold leading-relaxed mb-6 max-w-3xl text-luxury-taupe'
)
content = content.replace(
    'text-sm md:text-base font-semibold leading-relaxed mb-12 max-w-3xl text-luxury-beige',
    'text-sm md:text-base font-semibold leading-relaxed mb-12 max-w-3xl text-luxury-taupe'
)

# 5. Decorative stars text-black -> text-luxury-gold
content = content.replace(
    'className="absolute top-10 right-10 md:right-20 text-black opacity-30 animate-pulse"',
    'className="absolute top-10 right-10 md:right-20 text-luxury-gold opacity-10 animate-pulse"'
)
content = content.replace(
    'className="absolute bottom-32 left-4 md:left-20 text-black opacity-30 animate-pulse"',
    'className="absolute bottom-32 left-4 md:left-20 text-luxury-gold opacity-10 animate-pulse"'
)

# 6. Wave fill-white -> fill-luxury-bg
content = content.replace(
    'className="w-full h-12 md:h-20 fill-white"',
    'className="w-full h-12 md:h-20 fill-luxury-bg"'
)

# 7. Add luxury border to the ID card
content = content.replace(
    'className="bg-luxury-card w-full max-w-[280px] rounded-2xl p-4 shadow-[0_20px_40px_rgba(0,0,0,0.4)] relative z-20 transform -rotate-3 hover:rotate-0 transition-transform duration-500 text-luxury-ivory font-mono text-[10px] tracking-wider border border-white/10"',
    'className="bg-[#080808] w-full max-w-[280px] rounded-2xl p-4 shadow-[0_20px_40px_rgba(0,0,0,0.6)] relative z-20 transform -rotate-3 hover:rotate-0 transition-transform duration-500 text-luxury-ivory font-mono text-[10px] tracking-wider border border-luxury-gold/30"'
)

# Top piece of the ID card
content = content.replace(
    'className="absolute -top-3 left-1/2 w-16 h-6 bg-luxury-card rounded-t-xl transform -translate-x-1/2 flex justify-center items-center"',
    'className="absolute -top-3 left-1/2 w-16 h-6 bg-[#080808] border-t border-l border-r border-luxury-gold/30 rounded-t-xl transform -translate-x-1/2 flex justify-center items-center"'
)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched About section theme")
