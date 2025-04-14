import os
import re
from pathlib import Path

# Specifically target the portfolio subpages that need fixing
html_files = list(Path('sean-august-horvath-portfolio').glob('**/*.html'))

print(f"Fixing asset paths for {len(html_files)} files in sean-august-horvath-portfolio...")

for html_file in html_files:
    folder_depth = len(html_file.parts) - 1
    # Calculate the correct prefix to get back to the root directory
    root_prefix = '../' * folder_depth
    
    print(f"Processing {html_file} (depth: {folder_depth}, prefix to root: {root_prefix})")
    
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Store original content to check if we made changes
    original_content = content
    
    # Fix href references to CSS files
    content = re.sub(
        r'href="(\.\./)*/assets/',
        f'href="{root_prefix}assets/',
        content
    )
    
    # Fix src references to JavaScript files
    content = re.sub(
        r'src="(\.\./)*/assets/',
        f'src="{root_prefix}assets/',
        content
    )
    
    # Fix navigation links to the root
    content = re.sub(
        r'href="(\.\./)*/index.html"',
        f'href="{root_prefix}index.html"',
        content
    )
    
    # Fix links to other sections that start with the portfolio directory
    content = re.sub(
        r'href="(\.\./)*/sean-august-horvath-portfolio/',
        f'href="{root_prefix}sean-august-horvath-portfolio/',
        content
    )
    
    # Fix links to other sections
    content = re.sub(
        r'href="(\.\./)*/horvath-work-experience/',
        f'href="{root_prefix}horvath-work-experience/',
        content
    )
    
    content = re.sub(
        r'href="(\.\./)*/employment-industry/',
        f'href="{root_prefix}employment-industry/',
        content
    )
    
    content = re.sub(
        r'href="(\.\./)*/professional-title-role/',
        f'href="{root_prefix}professional-title-role/',
        content
    )
    
    content = re.sub(
        r'href="(\.\./)*/sean-august-horvath-information/',
        f'href="{root_prefix}sean-august-horvath-information/',
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