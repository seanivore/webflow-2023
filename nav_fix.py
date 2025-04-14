import os
import re
from pathlib import Path

# Get all HTML files
html_files = list(Path('.').glob('**/*.html'))

for html_file in html_files:
    folder_depth = len(html_file.parts) - 1
    asset_prefix = '../' * folder_depth if folder_depth > 0 else ''
    
    print(f"Processing {html_file} (depth: {folder_depth}, prefix: {asset_prefix})")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    # 1. Fix home link
    content = re.sub(r'href="\.html"', 'href="index.html"', content)
    
    # 2. Fix the navigation menu links
    content = re.sub(r'href="/sean-august-horvath-portfolio/([^"]+)"', r'href="sean-august-horvath-portfolio/\1"', content)
    content = re.sub(r'href="/horvath-work-experience/([^"]+)"', r'href="horvath-work-experience/\1"', content)
    content = re.sub(r'href="/employment-industry/([^"]+)"', r'href="employment-industry/\1"', content)
    content = re.sub(r'href="/sean-august-horvath-information/([^"]+)"', r'href="sean-august-horvath-information/\1"', content)
    content = re.sub(r'href="/professional-title-role/([^"]+)"', r'href="professional-title-role/\1"', content)
    
    # 3. Add relative prefixes to all file paths for subpages
    if folder_depth > 0:
        # Fix relative paths for navigation links
        content = re.sub(r'href="(sean-august-horvath-portfolio/[^"]+)"', f'href="{asset_prefix}\\1"', content)
        content = re.sub(r'href="(horvath-work-experience/[^"]+)"', f'href="{asset_prefix}\\1"', content)
        content = re.sub(r'href="(employment-industry/[^"]+)"', f'href="{asset_prefix}\\1"', content)
        content = re.sub(r'href="(sean-august-horvath-information/[^"]+)"', f'href="{asset_prefix}\\1"', content)
        content = re.sub(r'href="(professional-title-role/[^"]+)"', f'href="{asset_prefix}\\1"', content)
        content = re.sub(r'href="index.html"', f'href="{asset_prefix}index.html"', content)
    
    # 4. Fix image paths in portfolio folders
    content = re.sub(r'src="/sean-august-horvath-portfolio/assets/images/([^"]+)"', f'src="{asset_prefix}assets/images/\\1"', content)
    content = re.sub(r'src="/horvath-work-experience/assets/images/([^"]+)"', f'src="{asset_prefix}assets/images/\\1"', content)
    
    # 5. Fix background image URLs
    content = re.sub(r'background-image: url\(\'/sean-august-horvath-portfolio/assets/images/([^\']+)\'\)', f'background-image: url(\'{asset_prefix}assets/images/\\1\')', content)
    content = re.sub(r'background-image: url\("/sean-august-horvath-portfolio/assets/images/([^"]+)"\)', f'background-image: url("{asset_prefix}assets/images/\\1")', content)
    
    # 6. Fix remaining JavaScript issues
    content = re.sub(r'src="[^"]*webflow\.a81ba2ca\.f236ca9b0599fa7c\.js"', f'src="{asset_prefix}assets/js/simplified/webflow3.js"', content)
    
    # Write back to file
    with open(html_file, 'w') as f:
        f.write(content)

print("Navigation links and image paths fixed!") 