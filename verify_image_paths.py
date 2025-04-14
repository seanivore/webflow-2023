import os
import re
from pathlib import Path
from urllib.parse import unquote

# Get all HTML files
html_files = list(Path('.').glob('**/*.html'))
broken_links = []

for html_file in html_files:
    folder_depth = len(html_file.parts) - 1
    asset_prefix = '../' * folder_depth if folder_depth > 0 else ''
    
    print(f"Checking {html_file} (depth: {folder_depth})")
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Find all image references
    # Look for src attributes in img tags
    img_srcs = re.findall(r'<img[^>]+src="([^"]+)"', content)
    
    # Look for background-image URLs in style attributes or inline CSS
    bg_imgs = re.findall(r'background-image\s*:\s*url\([\'"]?([^\'"]+)[\'"]?\)', content)
    
    # Combined list of all image references
    all_images = img_srcs + bg_imgs
    
    # Check each image path
    for img_path in all_images:
        img_path = unquote(img_path)  # Handle URL-encoded paths
        
        # Skip external URLs
        if img_path.startswith('http://') or img_path.startswith('https://'):
            continue
            
        # Handle both absolute and relative paths
        if img_path.startswith('/'):
            # This was an absolute path, so it's relative to the project root
            actual_path = img_path.lstrip('/')
        else:
            # This was already a relative path
            # Calculate the actual path relative to the project root
            if folder_depth > 0:
                parts = html_file.parts[:-1]  # Get the directory parts
                actual_path = str(Path(*parts) / img_path)
            else:
                actual_path = img_path
        
        # Check if the file exists
        if not os.path.exists(actual_path):
            broken_links.append((str(html_file), img_path, actual_path))

# Report broken links
if broken_links:
    print("\n--- Broken Image Links ---")
    for html_file, img_path, actual_path in broken_links:
        print(f"File: {html_file}")
        print(f"  Referenced: {img_path}")
        print(f"  Expected at: {actual_path}")
        print()
    
    print(f"Total broken links: {len(broken_links)}")
else:
    print("\nAll image links verified successfully! No broken links found.") 