import os
import re
from pathlib import Path

# Specifically target the portfolio subpages that need fixing
html_files = list(Path('sean-august-horvath-portfolio').glob('**/*.html'))

print(f"Fixing CSS and JS paths for {len(html_files)} files in sean-august-horvath-portfolio...")

for html_file in html_files:
    folder_depth = len(html_file.parts) - 1
    asset_prefix = '../' * folder_depth
    
    print(f"Processing {html_file} (depth: {folder_depth}, prefix: {asset_prefix})")
    
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Store original content to check if we made changes
    original_content = content
    
    # Fix all CSS references from /sean-august-horvath-portfolio/assets/ to use the correct relative path
    content = re.sub(
        r'href=([\'"])/sean-august-horvath-portfolio/assets/',
        f'href=\\1{asset_prefix}assets/',
        content
    )
    
    # Fix all JS references from /sean-august-horvath-portfolio/assets/ to use the correct relative path
    content = re.sub(
        r'src=([\'"])/sean-august-horvath-portfolio/assets/',
        f'src=\\1{asset_prefix}assets/',
        content
    )
    
    # Fix any background images that use /sean-august-horvath-portfolio/assets/
    content = re.sub(
        r'url\([\'"]?/sean-august-horvath-portfolio/assets/',
        f'url({asset_prefix}assets/',
        content
    )
    
    # Check if we made any changes
    if content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Fixed paths in {html_file}")
    else:
        print(f"  No changes needed in {html_file}")

print("\nPath fixing complete! Run the web server again to test.") 