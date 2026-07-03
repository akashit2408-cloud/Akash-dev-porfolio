import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix mobile menu link clicks to close the menu
content = content.replace(
    'className="text-luxury-ivory hover:text-luxury-gold font-bold text-lg border-b border-white/10 pb-2 transition-colors"',
    'onClick={() => setIsMenuOpen(false)} className="text-luxury-ivory hover:text-luxury-gold font-bold text-lg border-b border-white/10 pb-2 transition-colors"'
)

# Fix mobile Hire Me button colors and add onClick to close
content = content.replace(
    'className="inline-block px-6 py-3 rounded-full bg-white text-[#67408a] font-black hover:bg-luxury-bg hover:text-luxury-ivory transition-colors w-full text-center shadow-lg"',
    'onClick={() => setIsMenuOpen(false)} className="inline-block px-6 py-3 rounded-full bg-luxury-gold text-black font-black hover:bg-luxury-beige hover:shadow-[0_0_15px_rgba(212,175,55,0.4)] transition-colors w-full text-center shadow-lg"'
)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile menu patched")
