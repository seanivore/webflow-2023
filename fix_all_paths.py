import os
import re
from pathlib import Path

# Get all HTML files
html_files = list(Path('.').glob('**/*.html'))

for html_file in html_files:
    # Determine how many directories deep this file is
    folder_depth = len(html_file.parts) - 1  # How many directories deep is this file
    asset_prefix = '../' * (folder_depth - 1) if folder_depth > 1 else ''
    
    print(f"Processing {html_file} (depth: {folder_depth})")
    
    # Read the file content
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Fix asset references for files in subdirectories
    if folder_depth > 1:
        # Fix regular asset references (both with leading slash and without)
        content = re.sub(r'(href|src)="/?assets/', f'\\1="{asset_prefix}assets/', content)
        
        # Fix background image URLs with single quotes
        content = re.sub(r"url\('/?assets/", f"url('{asset_prefix}assets/", content)
        
        # Fix background image URLs with double quotes
        content = re.sub(r'url\("/?assets/', f'url("{asset_prefix}assets/', content)
        
        # Fix meta content URLs
        content = re.sub(r'content="/?assets/', f'content="{asset_prefix}assets/', content)
    
    # Fix any remaining absolute root-relative paths
    content = re.sub(r'href="(/[^"]+\.html)"', f'href="{asset_prefix}\\1"', content)
    
    # Fix ampersands for better display
    content = content.replace('&amp;', '&')
    
    # Write the modified content back to the file
    with open(html_file, 'w') as f:
        f.write(content)

print('All paths have been fixed') 