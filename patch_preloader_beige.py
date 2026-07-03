import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the preloader background
content = content.replace(
    'className="fixed inset-0 w-full h-screen bg-luxury-bg z-[100000] flex items-center justify-center"',
    'className="fixed inset-0 w-full h-screen bg-luxury-beige z-[100000] flex items-center justify-center"'
)

# Replace the preloader inner cutout shadow text color
content = content.replace(
    '<div className="text-white/5">',
    '<div className="text-black/10">'
)

# The sliding text (white currently, let's make it black or graphite for contrast against beige)
content = content.replace(
    'className="absolute top-0 left-0 text-luxury-ivory overflow-hidden whitespace-nowrap"',
    'className="absolute top-0 left-0 text-luxury-bg overflow-hidden whitespace-nowrap"'
)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched preloader theme to beige")
