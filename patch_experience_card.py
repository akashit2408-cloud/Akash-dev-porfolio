import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix ExperienceCard styles

# Card outer container active/inactive
content = content.replace(
    "${f ? 'bg-[#67408a] border-luxury-gold shadow-[0_20px_50px_rgba(103,64,138,0.4)]' : 'bg-white border border-gray-200 shadow-[0_15px_40px_rgba(0,0,0,0.06)] hover:shadow-[0_20px_50px_rgba(0,0,0,0.12)]'}",
    "${f ? 'bg-luxury-gold border-luxury-gold shadow-[0_20px_50px_rgba(212,175,55,0.4)]' : 'bg-luxury-card border border-white/5 shadow-lg hover:shadow-[0_20px_50px_rgba(212,175,55,0.1)]'}"
)

# Inner container active/inactive
content = content.replace(
    "${f ? 'bg-luxury-beige/50' : 'bg-[#f8f8f8]'}",
    "${f ? 'bg-luxury-card' : 'bg-luxury-bg'}"
)

# Role text inactive
content = content.replace(
    "${f ? 'text-luxury-ivory' : 'text-gray-900'}",
    "${f ? 'text-luxury-ivory' : 'text-luxury-taupe'}"
)

# Company text inactive
content = content.replace(
    "${f ? 'text-luxury-beige' : 'text-luxury-gold'}",
    "${f ? 'text-luxury-gold' : 'text-luxury-taupe'}"
)

# Tags active/inactive
content = content.replace(
    "${f ? 'bg-violet-900/40 text-luxury-beige border border-luxury-gold/20' : 'bg-white text-gray-700 border border-gray-200 shadow-sm'}",
    "${f ? 'bg-luxury-gold/20 text-luxury-gold border border-luxury-gold/40' : 'bg-luxury-bg text-luxury-taupe border border-white/10 shadow-sm'}"
)

# Details list active/inactive
content = content.replace(
    "${f ? 'text-luxury-beige' : 'text-luxury-taupe'}",
    "${f ? 'text-luxury-ivory/90' : 'text-luxury-taupe/70'}"
)

# Number text and Period text are fine (beige / taupe).

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Experience cards patched")
