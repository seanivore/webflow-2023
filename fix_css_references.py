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
    
    # Update CSS links that might still have absolute paths or incorrect relative paths
    content = re.sub(r'href="/assets/css/([^"]+)"', f'href="{asset_prefix}assets/css/\\1"', content)
    content = re.sub(r'href="https?://[^"]+/assets/css/([^"]+)"', f'href="{asset_prefix}assets/css/\\1"', content)
    
    # Also fix any JS references that might be still problematic
    content = re.sub(r'src="/assets/js/([^"]+)"', f'src="{asset_prefix}assets/js/\\1"', content)
    content = re.sub(r'src="https?://[^"]+/assets/js/([^"]+)"', f'src="{asset_prefix}assets/js/\\1"', content)
    
    # Fix any inline style references to web fonts or other assets
    content = re.sub(r'url\(/assets/fonts/([^)]+)\)', f'url({asset_prefix}assets/fonts/\\1)', content)
    content = re.sub(r'url\("?/assets/images/([^)"]+)"?\)', f'url("{asset_prefix}assets/images/\\1")', content)
    
    # Write back to file
    with open(html_file, 'w') as f:
        f.write(content)

print("CSS and asset references fixed!") 