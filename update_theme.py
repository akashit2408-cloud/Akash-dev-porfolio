import re

# 1. Update index.css
css_path = r'C:\manage\portfolio-source\src\index.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

theme_block = """@theme {
  --color-luxury-bg: #080808;
  --color-luxury-card: #18181B;
  --color-luxury-gold: #D4AF37;
  --color-luxury-beige: #C8B88A;
  --color-luxury-ivory: #F8F4E3;
  --color-luxury-taupe: #A8A29E;
}
"""

if "@theme" not in css_content:
    # Insert right after @import "tailwindcss";
    css_content = css_content.replace('@import "tailwindcss";', f'@import "tailwindcss";\n\n{theme_block}')
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

# 2. Update App.jsx
app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    app_content = f.read()

replacements = {
    # Backgrounds
    r'\bbg-black\b': 'bg-luxury-bg',
    r'\bbg-gray-900\b': 'bg-luxury-card',
    r'\bbg-gray-800\b': 'bg-luxury-card',
    r'\bbg-black/10\b': 'bg-luxury-card',
    r'\bbg-black/40\b': 'bg-luxury-card',
    
    # Text Primary
    r'\btext-white\b': 'text-luxury-ivory',
    
    # Text Muted
    r'\btext-gray-300\b': 'text-luxury-taupe',
    r'\btext-gray-400\b': 'text-luxury-taupe',
    r'\btext-gray-500\b': 'text-luxury-taupe',
    r'\btext-gray-600\b': 'text-luxury-taupe',
    r'\btext-white/80\b': 'text-luxury-taupe',
    r'\btext-white/60\b': 'text-luxury-taupe',
    
    # Violets to Golds/Beige
    r'\btext-violet-400\b': 'text-luxury-gold',
    r'\btext-violet-500\b': 'text-luxury-gold',
    r'\btext-violet-600\b': 'text-luxury-gold',
    r'\btext-violet-200\b': 'text-luxury-beige',
    r'\btext-violet-100\b': 'text-luxury-beige',
    r'\btext-violet-50\b': 'text-luxury-beige',
    
    r'\bbg-violet-400\b': 'bg-luxury-gold',
    r'\bbg-violet-500\b': 'bg-luxury-gold',
    r'\bbg-violet-600\b': 'bg-luxury-gold',
    r'\bbg-violet-700\b': 'bg-luxury-beige',
    r'\bbg-violet-700/50\b': 'bg-luxury-gold',
    
    r'\bborder-violet-400\b': 'border-luxury-gold',
    r'\bborder-violet-500\b': 'border-luxury-gold',
    
    # Borders
    r'\bborder-gray-800\b': 'border-white/10',
    r'\bborder-gray-600\b': 'border-luxury-card',
    r'\bborder-gray-900\b': 'border-luxury-card',
    
    # Button styling (White buttons to Ivory, Black text)
    r'\bbg-white text-black\b': 'bg-luxury-ivory text-black',
}

for pattern, replacement in replacements.items():
    app_content = re.sub(pattern, replacement, app_content)

# Specific fixes: 
# The gradient bg-gradient-to-br from-violet-900 to-black -> bg-luxury-bg
app_content = re.sub(r'bg-gradient-to-br from-violet-900 to-black', 'bg-luxury-bg', app_content)
# from-violet-500/20 to-transparent -> from-luxury-gold/20 to-transparent
app_content = re.sub(r'from-violet-500/20', 'from-luxury-gold/20', app_content)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(app_content)

print("Theme updated successfully")
