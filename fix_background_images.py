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
    
    # Fix background-image styles in style attributes
    # Original format: style="background-image: url('https://cdn.prod.website-files.com/632a96df13f59cf284722156/63c283a64553f6cdd7b5d092_web-character-illustration-web3-branding-artist.png');"
    content = re.sub(r'background-image: url\(\'[^\']*?/([^/\']+)\'\)', f'background-image: url(\'{asset_prefix}assets/images/\\1\')', content)
    content = re.sub(r'background-image: url\("[^"]*?/([^/"]+)"\)', f'background-image: url("{asset_prefix}assets/images/\\1")', content)
    
    # Fix any remaining issues with portfolio image references
    content = re.sub(r'src="/sean-august-horvath-portfolio/[^"]*?/([^/"]+)"', f'src="{asset_prefix}assets/images/\\1"', content)
    
    # Write back to file
    with open(html_file, 'w') as f:
        f.write(content)

print("Background image URLs fixed!") 