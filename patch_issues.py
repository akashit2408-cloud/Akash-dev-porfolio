import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add isMenuOpen state if it doesn't exist
if 'const [isMenuOpen, setIsMenuOpen] = useState(false);' not in content:
    content = content.replace(
        'const [isVideoPlaying, setIsVideoPlaying] = useState(true);',
        'const [isVideoPlaying, setIsVideoPlaying] = useState(true);\n  const [isMenuOpen, setIsMenuOpen] = useState(false);'
    )

# Fix hamburger button onClick
content = content.replace(
    '<button className="text-luxury-ivory focus:outline-none p-2"><svg',
    '<button onClick={() => setIsMenuOpen(!isMenuOpen)} className="text-luxury-ivory focus:outline-none p-2"><svg'
)

# Fix mobile menu container logic
content = content.replace(
    'className="lg:hidden absolute top-full left-0 w-full transition-all duration-300 overflow-hidden max-h-0 opacity-0 bg-transparent"',
    'className={`lg:hidden absolute top-full left-0 w-full transition-all duration-300 overflow-hidden ${isMenuOpen ? "max-h-96 opacity-100 bg-luxury-bg/95 backdrop-blur-md pb-6 pt-2 border-b border-white/10" : "max-h-0 opacity-0"}`}'
)

# Fix hover:text-black in mobile menu items
content = content.replace(
    'className="text-luxury-ivory hover:text-black font-bold text-lg border-b border-white/20 pb-2 transition-colors"',
    'className="text-luxury-ivory hover:text-luxury-gold font-bold text-lg border-b border-white/10 pb-2 transition-colors"'
)

# Fix Experience section background and text
content = content.replace(
    'className="bg-white pt-24 pb-32 px-6 md:px-12 w-full relative overflow-hidden font-sans bg-[linear-gradient(to_right,#8080800a_1px,transparent_1px),linear-gradient(to_bottom,#8080800a_1px,transparent_1px)] bg-[size:80px_80px]"',
    'className="bg-luxury-bg pt-24 pb-32 px-6 md:px-12 w-full relative overflow-hidden font-sans bg-[linear-gradient(to_right,#ffffff0a_1px,transparent_1px),linear-gradient(to_bottom,#ffffff0a_1px,transparent_1px)] bg-[size:80px_80px]"'
)

# Fix Timeline badge
content = content.replace(
    'className="inline-block border border-gray-300 rounded-full px-5 py-1.5 text-xs text-luxury-taupe font-bold mb-6 shadow-sm bg-white uppercase tracking-widest"',
    'className="inline-block border border-luxury-gold/30 rounded-full px-5 py-1.5 text-xs text-luxury-gold font-bold mb-6 shadow-sm bg-luxury-card uppercase tracking-widest"'
)

# Fix Experience header text color
content = content.replace(
    'className="text-4xl md:text-5xl lg:text-6xl font-black text-gray-900 leading-[1.1] mb-6 tracking-tight relative"',
    'className="text-4xl md:text-5xl lg:text-6xl font-black text-luxury-ivory leading-[1.1] mb-6 tracking-tight relative"'
)

# Any other stray bg-white or text-gray-900 that should be dark
content = content.replace(
    'bg-white rounded-[2rem] p-8 md:p-12',
    'bg-luxury-card rounded-[2rem] p-8 md:p-12 border border-white/5'
)
content = content.replace(
    'text-gray-900 font-bold',
    'text-luxury-ivory font-bold'
)
content = content.replace(
    'text-gray-800',
    'text-luxury-ivory'
)


with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Toggle menu and experience section fixed")
