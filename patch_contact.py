import re

app_path = r'C:\manage\portfolio-source\src\App.jsx'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the main form container
old_container = 'className="bg-gradient-to-br from-[#67408a]/85 via-[#67408a]/65 to-[#4d2f70]/45 backdrop-blur-xl border border-white/10 shadow-[inset_0_1.5px_2px_rgba(255,255,255,0.3),0_25px_50px_-12px_rgba(0,0,0,0.5)] w-full md:w-[85%] lg:w-[75%] p-8 md:p-16 text-luxury-ivory flex flex-col justify-between min-h-[600px] transition-all duration-500 aos-init"'
new_container = 'className="bg-luxury-gold backdrop-blur-xl border border-black/10 shadow-[inset_0_1.5px_2px_rgba(255,255,255,0.3),0_25px_50px_-12px_rgba(0,0,0,0.5)] w-full md:w-[85%] lg:w-[75%] p-8 md:p-16 text-black flex flex-col justify-between min-h-[600px] transition-all duration-500"'
content = content.replace(old_container, new_container)
# Note: 'aos-init' gets added by the AOS library dynamically sometimes, but the base class doesn't need it. 
# In case it's in the source without aos-init:
old_container2 = 'className="bg-gradient-to-br from-[#67408a]/85 via-[#67408a]/65 to-[#4d2f70]/45 backdrop-blur-xl border border-white/10 shadow-[inset_0_1.5px_2px_rgba(255,255,255,0.3),0_25px_50px_-12px_rgba(0,0,0,0.5)] w-full md:w-[85%] lg:w-[75%] p-8 md:p-16 text-luxury-ivory flex flex-col justify-between min-h-[600px] transition-all duration-500"'
content = content.replace(old_container2, new_container)

# 2. Update inputs and textarea classes
old_input = 'className="w-full bg-transparent border-b border-white/40 pb-3 text-lg focus:outline-none focus:border-white transition-colors placeholder-white/70 font-medium rounded-none disabled:opacity-50"'
new_input = 'className="w-full bg-transparent border-b border-black/40 pb-3 text-lg focus:outline-none focus:border-black transition-colors placeholder-black/70 font-medium rounded-none disabled:opacity-50 text-black"'
content = content.replace(old_input, new_input)

old_textarea = 'className="w-full h-full min-h-[120px] bg-transparent border-b border-white/40 pb-3 text-lg focus:outline-none focus:border-white transition-colors placeholder-white/70 font-medium resize-none rounded-none disabled:opacity-50"'
new_textarea = 'className="w-full h-full min-h-[120px] bg-transparent border-b border-black/40 pb-3 text-lg focus:outline-none focus:border-black transition-colors placeholder-black/70 font-medium resize-none rounded-none disabled:opacity-50 text-black"'
content = content.replace(old_textarea, new_textarea)

# 3. Update the checkbox and its label container
old_checkbox_container = 'className="flex-1 flex items-start gap-4 text-sm font-medium text-luxury-ivory/90"'
new_checkbox_container = 'className="flex-1 flex items-start gap-4 text-sm font-medium text-black/90"'
content = content.replace(old_checkbox_container, new_checkbox_container)

old_checkbox = 'className="mt-1 w-4 h-4 rounded-sm border-white/40 bg-transparent text-luxury-ivory focus:ring-white focus:ring-offset-0 focus:ring-offset-transparent cursor-pointer disabled:opacity-50"'
new_checkbox = 'className="mt-1 w-4 h-4 rounded-sm border-black/40 bg-transparent text-black focus:ring-black focus:ring-offset-0 focus:ring-offset-transparent cursor-pointer disabled:opacity-50"'
content = content.replace(old_checkbox, new_checkbox)
content = content.replace("style={{ accentColor: 'white' }}", "style={{ accentColor: 'black' }}")

# 4. Update the "Send ->" button
old_button = 'className="flex items-center gap-3 px-8 py-3 rounded-full border border-white/20 hover:bg-white hover:text-black transition-all duration-300 font-bold text-sm tracking-widest uppercase disabled:opacity-50"'
new_button = 'className="flex items-center gap-3 px-8 py-3 rounded-full border border-black/20 hover:bg-black hover:text-luxury-gold transition-all duration-300 font-bold text-sm tracking-widest uppercase disabled:opacity-50"'
content = content.replace(old_button, new_button)

# Also fix the SVG color inside the Send button
content = content.replace('<svg className="w-4 h-4 group-hover:translate-x-1 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" /></svg>',
'<svg className="w-4 h-4 group-hover:translate-x-1 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" /></svg>') # Nothing actually needs to change for the SVG as it uses currentColor

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Contact Section styling")
