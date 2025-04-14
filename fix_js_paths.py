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
    
    # Fix JS file references with incorrect paths
    if "assets/images/js/webflow" in content:
        # Create the directory for the JS files if it doesn't exist yet
        js_dir = Path('assets/js/webflow')
        js_dir.mkdir(parents=True, exist_ok=True)
        
        # Replace incorrect JS paths
        content = re.sub(
            r'src="(?:assets|/assets)/images/js/(webflow[^"]+)"', 
            f'src="{asset_prefix}assets/js/\\1"', 
            content
        )
    
    # Write the modified content back to the file
    with open(html_file, 'w') as f:
        f.write(content)

print('JS path references have been fixed') 