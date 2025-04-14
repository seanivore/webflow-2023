import os
import re
from pathlib import Path
from urllib.parse import unquote

# Get all HTML files
html_files = list(Path('.').glob('**/*.html'))
fixed_links = 0

print("Starting to fix GIF links...")

for html_file in html_files:
    folder_depth = len(html_file.parts) - 1
    asset_prefix = '../' * folder_depth if folder_depth > 0 else ''
    
    print(f"Processing {html_file} (depth: {folder_depth})")
    
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find all gif references - look for both src attributes and background-image URLs
    gif_srcs = re.findall(r'<img[^>]+src="([^"]+\.gif)"', content)
    bg_gifs = re.findall(r'background-image\s*:\s*url\([\'"]?([^\'"]+\.gif)[\'"]?\)', content)
    
    # Combined list of all gif references
    all_gifs = gif_srcs + bg_gifs
    
    # Track if any changes were made to this file
    file_changed = False
    
    for gif_path in all_gifs:
        gif_path = unquote(gif_path)  # Handle URL-encoded paths
        
        # Skip external URLs
        if gif_path.startswith('http://') or gif_path.startswith('https://'):
            continue
        
        # For each gif, modify the path from assets/images/ to assets/gifs/
        if 'assets/images' in gif_path:
            new_path = gif_path.replace('assets/images', 'assets/gifs')
            content = content.replace(gif_path, new_path)
            file_changed = True
            fixed_links += 1
            print(f"  Fixed: {gif_path} -> {new_path}")
        elif '../assets/images' in gif_path:
            new_path = gif_path.replace('../assets/images', '../assets/gifs')
            content = content.replace(gif_path, new_path)
            file_changed = True
            fixed_links += 1
            print(f"  Fixed: {gif_path} -> {new_path}")
    
    # Only write to file if changes were made
    if file_changed:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"\nFixed {fixed_links} broken GIF links!")
print("Run verify_image_paths.py again to check if all issues are resolved.") 