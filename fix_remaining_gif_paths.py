import os
import re
from pathlib import Path
from urllib.parse import unquote

# List of files with broken GIF links from verify_image_paths.py output
broken_files = [
    "horvath-work-experience/web3-content-producer-digital-media-animated-memes-pepe-ready-launch-product.html",
    "horvath-work-experience/digital-artist-mint-nft-anamorphic-animtions-bojack-jake-adventure-time-skeeter-doug-zoidberg-glow-up-muscle.html",
    "horvath-work-experience/web3-start-up-content-production-motion-design-memes-futurama-hypnotoad.html",
    "horvath-work-experience/digital-retro-wave-neon-futurism-minted-animated-nfts.html",
    "horvath-work-experience/frame-animate-flag-waving-breeze.html",
    "horvath-work-experience/digital-vector-gif-animation-burning-cash-bitcoin-fiat.html",
    "horvath-work-experience/designer-web3-emoji-animation-branding-tokens-monkey.html",
    "horvath-work-experience/digital-social-content-animation-designer-no-evil-monkey-emoji.html",
    "horvath-work-experience/social-producer-meme-content-pepe-branding-animation.html",
    "horvath-work-experience/visual-artist-content-producer-designs-animated-effects-neon-grid-tunnel-never-ending.html",
    "horvath-work-experience/web3-content-production-animated-meme-olympus-incubator-following.html",
    "horvath-work-experience/motion-designer-3d-logo-animation-blender-content-production.html",
    "horvath-work-experience/tablet-drawn-vector-illustration-animated-dragon-video-content-producer.html",
    "horvath-work-experience/animation-designer-digital-content-production-3d-vr-nft-gallery.html"
]

print("Starting to fix remaining GIF links using direct file targeting...")
fixed_count = 0

for file_path in broken_files:
    print(f"Processing {file_path}")
    
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        original_content = content
        
        # Fix multiple patterns
        
        # 1. Fix instances of ../assets/images/*.gif references
        content = re.sub(r'(src|href)=([\'"])../assets/images/([^\'"]*.gif)([\'"])',
                         r'\1=\2../assets/gifs/\3\4', content)
        
        # 2. Fix background-image URLs
        content = re.sub(r'background-image\s*:\s*url\([\'"]?../assets/images/([^\'"\)]*\.gif)[\'"]?\)',
                         r'background-image: url(../assets/gifs/\1)', content)
        
        # 3. Also fix potential absolute paths to GIFs
        content = re.sub(r'(src|href)=([\'"])/assets/images/([^\'"]*.gif)([\'"])',
                         r'\1=\2/assets/gifs/\3\4', content)
        
        # 4. Fix potential background-image with absolute paths
        content = re.sub(r'background-image\s*:\s*url\([\'"]?/assets/images/([^\'"\)]*\.gif)[\'"]?\)',
                         r'background-image: url(/assets/gifs/\1)', content)
        
        # Check if content was modified
        if content != original_content:
            # Write the modified content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  Fixed references in {file_path}")
            fixed_count += 1
        else:
            print(f"  No changes needed in {file_path}")
    
    except Exception as e:
        print(f"  Error processing {file_path}: {e}")

print(f"\nFixed references in {fixed_count} files")
print("Run verify_image_paths.py again to check if all issues are resolved.") 