import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Hero container
# original: className="absolute inset-0 z-20 px-6 pb-20 md:pb-[8%] md:px-12 max-w-7xl mx-auto flex flex-col md:flex-row justify-end md:justify-between items-start md:items-end text-left w-full"
# new: className="absolute inset-0 z-20 pt-28 pb-10 px-6 md:pt-0 md:pb-[8%] md:px-12 max-w-7xl mx-auto flex flex-col md:flex-row justify-center md:justify-between items-start md:items-end text-left w-full overflow-y-auto overflow-x-hidden"
content = content.replace(
    'className="absolute inset-0 z-20 px-6 pb-20 md:pb-[8%] md:px-12 max-w-7xl mx-auto flex flex-col md:flex-row justify-end md:justify-between items-start md:items-end text-left w-full"',
    'className="absolute inset-0 z-20 pt-28 pb-10 px-6 md:pt-0 md:pb-[8%] md:px-12 max-w-7xl mx-auto flex flex-col md:flex-row justify-center md:justify-between items-start md:items-end text-left w-full overflow-y-auto overflow-x-hidden"'
)

# Also fix the paragraph text size on mobile to make it fit better
# original: className="text-luxury-ivory/80 text-sm md:text-lg font-semibold mb-8 max-w-lg drop-shadow-md leading-relaxed aos-init aos-animate"
# new: className="text-luxury-ivory/80 text-xs sm:text-sm md:text-lg font-semibold mb-6 max-w-lg drop-shadow-md leading-relaxed aos-init aos-animate"
content = content.replace(
    'className="text-luxury-ivory/80 text-sm md:text-lg font-semibold mb-8 max-w-lg drop-shadow-md leading-relaxed aos-init aos-animate"',
    'className="text-luxury-ivory/80 text-xs sm:text-sm md:text-lg font-semibold mb-6 max-w-lg drop-shadow-md leading-relaxed"'
)

# Fix Hi, I'm heading on mobile
content = content.replace(
    'className="text-luxury-ivory text-4xl md:text-6xl font-black mb-2 tracking-tight [text-shadow:_-2px_-2px_0_#000,_2px_-2px_0_#000,_-2px_2px_0_#000,_2px_2px_0_#000] aos-init aos-animate"',
    'className="text-luxury-ivory text-3xl sm:text-4xl md:text-6xl font-black mb-2 tracking-tight [text-shadow:_-2px_-2px_0_#000,_2px_-2px_0_#000,_-2px_2px_0_#000,_2px_2px_0_#000]"'
)

# Fix Graphic Designer heading on mobile
content = content.replace(
    'className="text-luxury-gold text-lg md:text-2xl font-black mb-4 tracking-wider uppercase aos-init aos-animate"',
    'className="text-luxury-gold text-base sm:text-lg md:text-2xl font-black mb-3 tracking-wider uppercase"'
)

# Fix buttons wrapping awkwardly. Make them full width on small mobile or smaller text
content = content.replace(
    'className="flex flex-row flex-wrap items-center gap-3 w-full aos-init aos-animate"',
    'className="flex flex-row flex-wrap items-center gap-2 md:gap-3 w-full"'
)

# Make "Preview Resume" button fit better by removing the massive shadow that might cause overflow
content = content.replace(
    'shadow-[0_0_15px_rgba(139,92,246,0.4)] hover:shadow-[0_0_25px_rgba(139,92,246,0.6)]',
    'shadow-[0_0_15px_rgba(212,175,55,0.4)] hover:shadow-[0_0_25px_rgba(212,175,55,0.6)]'
)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile hero section patched")
