import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

modal_pattern = r'\s*\{/\* Video Modal \*/\}\s*\{activeVideo && \([\s\S]*?\}\s*</button>\s*<video controls autoPlay className="w-full h-full object-contain">\s*<source src=\{activeVideo\.url\} type="video/mp4" />\s*Your browser does not support the video tag\.\s*</video>\s*</div>\s*</div>\s*\)\}'

# Find the modal code
match = re.search(modal_pattern, content)
if match:
    modal_code = match.group(0)
    
    # Remove it from wherever it currently is
    content = content.replace(modal_code, '')
    
    # Add it right before the final </div> of the App component
    content = content.replace(
        '    </footer>\n  \n    </div>\n  );\n}',
        '    </footer>\n' + modal_code + '\n    </div>\n  );\n}'
    )

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed React crash by moving the modal to the correct component scope")
