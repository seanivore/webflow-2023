# August House LLC Portfolio (2023)

This is a static HTML version of a Webflow portfolio site from 2023, converted for GitHub Pages deployment.

## Original Site

The original site was hosted at: https://august-house-llc.webflow.io/

## Custom Domain

This site is deployed at [visual-producer.august.style](https://visual-producer.august.style)

## Conversion Process

The site was converted from Webflow to static HTML using the following steps:

1. Downloaded HTML structure using `wget`
2. Extracted and downloaded all asset files (images, CSS, JS)
3. Fixed all internal links and file paths
4. Simplified the file structure with sensible names
5. Deployed to GitHub Pages

## Path Fixing Scripts

Several scripts were created to fix path issues in the Webflow export:

- `verify_image_paths.py` - Identifies broken image links throughout the site
- `fix_gif_paths.py` - Fixes paths to GIF files that are in assets/gifs instead of assets/images
- `fix_remaining_gif_paths.py` - Targets specific files with broken GIF links
- `fix_css_references.py` - Ensures correct relative paths to CSS from various subdirectories
- `fix_portfolio_paths_advanced.py` - Fixes paths in the sean-august-horvath-portfolio section

## File Structure

- `/index.html` - Main landing page
- `/assets/` - All site assets
  - `/assets/css/simplified/` - Renamed CSS files with sensible names
  - `/assets/js/simplified/` - Renamed JS files with sensible names
  - `/assets/images/` - All image assets
  - `/assets/gifs/` - All GIF animation files
  - `/assets/fonts/` - Font files

## GitHub Pages Setup

The site is configured for GitHub Pages with:

- `_config.yml` - Jekyll configuration with site title, description and custom permalink structure
- `CNAME` - Custom domain configuration for visual-producer.august.style

## Notable Fixes

1. **GIF Path Issue**: The Webflow export referenced GIFs in /assets/images/ but they were actually in /assets/gifs/
2. **Depth-Dependent Path Issues**: Fixed relative paths in subdirectories by calculating the correct path depth
3. **Portfolio Section CSS/JS**: Fixed missing assets in the sean-august-horvath-portfolio section by correctly linking to root assets
4. **Navigation Links**: Ensured all site navigation works correctly regardless of which page you're viewing

## Notes

This site is a portfolio snapshot from 2023 and is maintained as an archive. It showcases Sean August Horvath's work in visual design, illustrations, GIF animations, and web content production.

## Contact

For more information, visit [visual-producer.august.style](https://visual-producer.august.style). 