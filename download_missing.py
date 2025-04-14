import os
import re
import urllib.request
from pathlib import Path

# Create directories
os.makedirs('assets/js', exist_ok=True)

# Get unique JS file names from HTML files
js_file_urls = set()
for html_file in Path('.').glob('**/*.html'):
    with open(html_file, 'r') as f:
        content = f.read()
        # Find webflow JS references
        matches = re.findall(r'webflow\.schunk\.[a-f0-9]+\.js', content)
        for match in matches:
            js_file_urls.add(f"https://cdn.prod.website-files.com/js/{match}")

# Download the JS files
for url in js_file_urls:
    filename = url.split('/')[-1]
    output_path = f"assets/js/{filename}"
    
    print(f"Downloading {url} to {output_path}")
    try:
        urllib.request.urlretrieve(url, output_path)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Also download jquery and webflow.js
jquery_url = "https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js"
webflow_url = "https://assets.website-files.com/assets/js/webflow.595f43b9.f65212ec484e883c.js"

try:
    urllib.request.urlretrieve(jquery_url, "assets/js/jquery-3.5.1.min.dc5e7f18c8.js")
    print("Downloaded jQuery")
except Exception as e:
    print(f"Error downloading jQuery: {e}")

try:
    urllib.request.urlretrieve(webflow_url, "assets/js/webflow.595f43b9.f65212ec484e883c.js")
    print("Downloaded Webflow.js")
except Exception as e:
    print(f"Error downloading Webflow.js: {e}")

print("Download complete!") 