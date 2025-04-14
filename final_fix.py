import os
import re
from pathlib import Path

# Get all HTML files
html_files = list(Path('.').glob('**/*.html'))

for html_file in html_files:
    # Determine how many directories deep this file is
    folder_depth = len(html_file.parts) - 1  # How many directories deep is this file
    asset_prefix = '../' * folder_depth if folder_depth > 0 else ''
    
    print(f"Processing {html_file} (depth: {folder_depth}, prefix: {asset_prefix})")
    
    # Read the file content
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Fix simplified CSS and JS references for files in subdirectories
    if folder_depth > 0:
        # Fix CSS references
        content = re.sub(r'href="assets/css/simplified/', f'href="{asset_prefix}assets/css/simplified/', content)
        
        # Fix JS references
        content = re.sub(r'src="assets/js/simplified/', f'src="{asset_prefix}assets/js/simplified/', content)
        
        # Fix image references
        content = re.sub(r'src="assets/images/', f'src="{asset_prefix}assets/images/', content)
        
        # Fix background image URLs
        content = re.sub(r"url\('assets/", f"url('{asset_prefix}assets/", content)
        content = re.sub(r'url\("assets/', f'url("{asset_prefix}assets/', content)
        
        # Fix meta content URLs
        content = re.sub(r'content="assets/', f'content="{asset_prefix}assets/', content)
    
    # Write the modified content back to the file
    with open(html_file, 'w') as f:
        f.write(content)

print('All paths have been fixed for local preview') 