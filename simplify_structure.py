import os
import re
import shutil
from pathlib import Path

# Create simplified directory structure
os.makedirs('assets/css/simplified', exist_ok=True)
os.makedirs('assets/js/simplified', exist_ok=True)

# Copy and rename main CSS files
css_files = {
    'assets/css/august-house-llc.webflow.ae9d9c701.css': 'assets/css/simplified/main.css',
    'assets/css/hkh6iuv.css': 'assets/css/simplified/fonts1.css',
    'assets/css/irt3fqd.css': 'assets/css/simplified/fonts2.css',
    'assets/css/hls3mif.css': 'assets/css/simplified/fonts3.css'
}

for src, dest in css_files.items():
    if os.path.exists(src):
        shutil.copy2(src, dest)
        print(f"Copied {src} to {dest}")
    else:
        print(f"Warning: {src} not found")

# Copy and rename main JS files
js_files = {
    'assets/js/webfont.js': 'assets/js/simplified/webfont.js',
    'assets/js/hls3mif.js': 'assets/js/simplified/typekit.js',
    'assets/js/jquery-3.5.1.min.dc5e7f18c8.js': 'assets/js/simplified/jquery.js',
    'assets/js/webflow.schunk.7e0f565b134f05e7.js': 'assets/js/simplified/webflow1.js',
    'assets/js/webflow.schunk.c7c4a20680881f24.js': 'assets/js/simplified/webflow2.js',
    'assets/js/webflow.595f43b9.f65212ec484e883c.js': 'assets/js/simplified/webflow3.js'
}

for src, dest in js_files.items():
    if os.path.exists(src):
        shutil.copy2(src, dest)
        print(f"Copied {src} to {dest}")
    else:
        # Create empty file if source doesn't exist
        with open(dest, 'w') as f:
            f.write('// Placeholder file\n')
        print(f"Created empty placeholder for {dest}")

# Update all HTML files to use the simplified structure
html_files = list(Path('.').glob('**/*.html'))

for html_file in html_files:
    folder_depth = len(html_file.parts) - 1
    asset_prefix = '../' * (folder_depth - 1) if folder_depth > 1 else ''
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Replace CSS references
    content = re.sub(r'href="[^"]*august-house-llc\.webflow\.ae9d9c701\.css"', 
                    f'href="{asset_prefix}assets/css/simplified/main.css"', content)
    content = re.sub(r'href="[^"]*hkh6iuv\.css"', 
                    f'href="{asset_prefix}assets/css/simplified/fonts1.css"', content)
    content = re.sub(r'href="[^"]*irt3fqd\.css"', 
                    f'href="{asset_prefix}assets/css/simplified/fonts2.css"', content)
    content = re.sub(r'href="[^"]*hls3mif\.css"', 
                    f'href="{asset_prefix}assets/css/simplified/fonts3.css"', content)
    
    # Replace JS references
    content = re.sub(r'src="[^"]*webfont\.js"', 
                    f'src="{asset_prefix}assets/js/simplified/webfont.js"', content)
    content = re.sub(r'src="[^"]*hls3mif\.js"', 
                    f'src="{asset_prefix}assets/js/simplified/typekit.js"', content)
    content = re.sub(r'src="[^"]*jquery[^"]*\.js"', 
                    f'src="{asset_prefix}assets/js/simplified/jquery.js"', content)
    content = re.sub(r'src="[^"]*webflow\.schunk\.7e0f565b134f05e7\.js"', 
                    f'src="{asset_prefix}assets/js/simplified/webflow1.js"', content)
    content = re.sub(r'src="[^"]*webflow\.schunk\.c7c4a20680881f24\.js"', 
                    f'src="{asset_prefix}assets/js/simplified/webflow2.js"', content)
    content = re.sub(r'src="[^"]*webflow\.595f43b9\.f65212ec484e883c\.js"', 
                    f'src="{asset_prefix}assets/js/simplified/webflow3.js"', content)
    
    # Write the modified content back
    with open(html_file, 'w') as f:
        f.write(content)

print('Site structure has been simplified with sensible file names') 