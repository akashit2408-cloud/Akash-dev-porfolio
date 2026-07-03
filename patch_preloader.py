import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the preloader background gradient
content = content.replace(
    'className="fixed inset-0 w-full h-screen bg-gradient-to-br from-[#67408a] via-[#523173] to-[#352151] z-[100000] flex items-center justify-center"',
    'className="fixed inset-0 w-full h-screen bg-luxury-bg z-[100000] flex items-center justify-center"'
)

# Replace the preloader inner cutout shadow text color
content = content.replace(
    '<div className="text-violet-950/30">',
    '<div className="text-white/5">'
)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched preloader theme")
