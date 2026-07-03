import re
from collections import Counter

with open(r'C:\manage\portfolio-source\src\App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all classes like bg-*, text-*, border-*
classes = re.findall(r'(bg-[a-z0-9/-]+|text-[a-z0-9/-]+|border-[a-z0-9/-]+)', content)

counts = Counter(classes)
print("Most common color classes:")
for c, count in counts.most_common(50):
    if any(color in c for color in ['violet', 'black', 'white', 'gray']):
        print(f"{c}: {count}")
