import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the outer card container
# It was: `${f ? 'bg-[#67408a] shadow-[0_20px_50px_rgba(103,64,138,0.4)]' : 'bg-white border border-gray-200 shadow-[0_15px_40px_rgba(0,0,0,0.06)] hover:shadow-[0_20px_50px_rgba(0,0,0,0.12)]'}`
# Change to Graphite bg with Gold glow on active.
content = content.replace(
    "${f ? 'bg-[#67408a] shadow-[0_20px_50px_rgba(103,64,138,0.4)]' : 'bg-white border border-gray-200 shadow-[0_15px_40px_rgba(0,0,0,0.06)] hover:shadow-[0_20px_50px_rgba(0,0,0,0.12)]'}",
    "${f ? 'bg-luxury-card border border-luxury-gold shadow-[0_0_30px_rgba(212,175,55,0.3)]' : 'bg-[#1a1a1a] border border-white/5 shadow-lg'}"
)

# 2. Update the inner dot 
# It was: `${f ? 'bg-white' : 'bg-gray-400'}`
content = content.replace(
    "${f ? 'bg-white' : 'bg-gray-400'}",
    "${f ? 'bg-luxury-gold' : 'bg-gray-600'}"
)

# 3. Update inner container
# It was: `${f ? 'bg-white/10' : 'bg-[#f8f8f8]'}`
content = content.replace(
    "${f ? 'bg-white/10' : 'bg-[#f8f8f8]'}",
    "${f ? 'bg-white/5' : 'bg-black/20'}"
)

# 4. Text updates for card
# Exp number:
content = content.replace(
    "${f ? 'text-white/70' : 'text-gray-400'}",
    "${f ? 'text-luxury-gold' : 'text-gray-500'}"
)
# Role:
content = content.replace(
    "${f ? 'text-white' : 'text-gray-900'}",
    "${f ? 'text-luxury-ivory' : 'text-white/80'}"
)
# Company:
content = content.replace(
    "${f ? 'text-white/80' : 'text-gray-500'}",
    "${f ? 'text-luxury-taupe' : 'text-gray-400'}"
)
# Details list:
content = content.replace(
    "${f ? 'text-white/80' : 'text-gray-600'}",
    "${f ? 'text-white/90' : 'text-gray-400'}"
)
# Tags:
content = content.replace(
    "${f ? 'bg-white/10 text-white/90 border border-white/20' : 'bg-white text-gray-700 border border-gray-200 shadow-sm'}",
    "${f ? 'bg-luxury-gold/10 text-luxury-gold border border-luxury-gold/30' : 'bg-white/5 text-gray-400 border border-white/10'}"
)

# 5. Curve line (SVG paths)
# Replace stroke="black" with stroke="#D4AF37" for the path that gets revealed
content = content.replace(
    'stroke="black" strokeWidth="2" strokeDasharray="8 10" mask="url(#path-mask)"',
    'stroke="#D4AF37" strokeWidth="3" strokeDasharray="8 10" mask="url(#path-mask)"'
)
content = content.replace(
    'stroke="black" strokeWidth="4" strokeDasharray="4 6" mask="url(#path-mask-mobile)"',
    'stroke="#D4AF37" strokeWidth="4" strokeDasharray="4 6" mask="url(#path-mask-mobile)"'
)

# Make the inactive dashed line lighter grey for better contrast if needed, but it's fine for now on white bg.
content = content.replace(
    'stroke="#cbd5e1" strokeWidth="2" strokeDasharray="8 10"',
    'stroke="#e2e8f0" strokeWidth="2" strokeDasharray="8 10"'
)
content = content.replace(
    'stroke="#cbd5e1" strokeWidth="4" strokeDasharray="4 6" vectorEffect',
    'stroke="#e2e8f0" strokeWidth="4" strokeDasharray="4 6" vectorEffect'
)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched Experience styling")
