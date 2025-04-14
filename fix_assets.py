import os
import re
from pathlib import Path

# Get all HTML files
html_files = list(Path('.').glob('**/*.html'))

for html_file in html_files:
    # Determine how many directories deep this file is
    folder_depth = len(html_file.parts) - 1  # How many directories deep is this file
    asset_prefix = '../' * (folder_depth - 1) if folder_depth > 1 else ''
    
    # Read the file content
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Fix asset references that lack the proper relative path
    if folder_depth > 1:  # Only for files in subdirectories
        # Fix references to assets/ folder
        content = re.sub(r'(href|src)="assets/', f'\\1="{asset_prefix}assets/', content)
        content = re.sub(r'url\(\'assets/', f'url(\'{asset_prefix}assets/', content)
        content = re.sub(r'url\("assets/', f'url("{asset_prefix}assets/', content)
        content = re.sub(r'content="assets/', f'content="{asset_prefix}assets/', content)
        
        # Also fix any remaining absolute paths starting with /assets/
        content = re.sub(r'(href|src)="/assets/', f'\\1="{asset_prefix}assets/', content)
        content = re.sub(r'url\(\'/assets/', f'url(\'{asset_prefix}assets/', content)
        content = re.sub(r'url\("/assets/', f'url("{asset_prefix}assets/', content)
        content = re.sub(r'content="/assets/', f'content="{asset_prefix}assets/', content)
    
    # Write the modified content back to the file
    with open(html_file, 'w') as f:
        f.write(content)

print('Asset references have been fixed') 