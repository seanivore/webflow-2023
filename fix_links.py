import os
import re
from pathlib import Path

# Get all HTML files
html_files = list(Path('.').glob('**/*.html'))

for html_file in html_files:
    # Read the file content
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Find all root-relative paths in href attributes
    absolute_links = re.findall(r'href=\"(/[^\"]+\.html)\"', content)
    
    # Calculate correct relative paths for each link
    for abs_link in absolute_links:
        rel_path = os.path.relpath(abs_link[1:], os.path.dirname(html_file))
        content = content.replace(f'href=\"{abs_link}\"', f'href=\"{rel_path}\"')
    
    # Write the modified content back to the file
    with open(html_file, 'w') as f:
        f.write(content)

print('Internal links have been converted to relative paths') 