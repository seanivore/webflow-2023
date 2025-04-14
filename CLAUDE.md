# Claude: About 'Webflow-2023' Project 

This is a pretty, custom designed portfolio for myself back in 2023. Original site is at: 

--> https://august-house-llc.webflow.io/

## Objectives

- Pull with 'wget' or other tools
- Convert to static HTML
- Deploy to Github Pages

### Challenges 

Previously we used this command: 

```bash
wget -m -p -E -k -np https://august-house-llc.webflow.io/
```

We've been encountering similar issues with each site we pull from Webflow or Framer. I'd have some ideas as to have we can be more proactive about anticipating these issues, and thus overall more efficient. 

#### Notes from Previous Attempt 

I'm pulling an old Webflow site and having some interesting issues. 
1. The wget tool is getting messed up with the quotes around the URLs and the ampersands being spelled out, the tool, and the IDE is not liking the HTML output because it is combining URLs. 
2. Same issue with getting them to all replace with paths in the IDE. 
3. And the fact that it names the directory "www.website.io" so that the URL says "www.website.io/pages/www.website.io/image_name.webp" it compounding the problem. 
   - Solution would be if we can have the tool output to a chosen directory name, and if we were able to search and control the search and replace better to be able to remove the quotes and ampersands, and we need to only use absolute paths but it always uses relative. 
   - This is what has been causing the same issues with the Framer website too. 
   - Interestingly, but too late in the process, I can "inspect" the website and copy the HTML and paste it on top of the terrible block of text wget output and it works — but again this is right *after* the tool is done finding HTML files and the paths are already relative. 
   - Ideally we could fix before wget runs or alter the process a bit. Otherwise we'll just have to backtrack. 
   - Take the output: Remove quotes and ampersands. Then run a script to collect all URLs. Run tool in terminal to make sure we have all the HTML files we need. Then change all the paths and leftover URLs to absolute paths. 
    > --2025-03-30 03:41:57--  https://august-house-llc.webflow.io/professional-title-role/&quot;https://cdn.prod.website-files.com/632a96df13f59cf284722156/63b3ff520e890923667505f3_img-wide-forms.png&quot;
    > Reusing existing connection to [august-house-llc.webflow.io]:443.
    > HTTP request sent, awaiting response... 404 Not Found
    > 2025-03-30 03:41:59 ERROR 404: Not Found.

### Potential Solutions 

I would like to break down the process into smaller steps instead of doing a bunch in one command. This will:

1. Help me learn better exactly what the process actually is. 
2. Allow me to address each error before we run the command for that step. 
3. I am going to record each step myself so that I can learn better. 
4. Instead of running commends, please provide them so that I can record them with what they do; this act of recording is what helps me learn. 

### Objective Requirements 

   - Because of the complexity of the HTML that is a mess and that Webflow has changed over the years, I don't want the command to automatically change things to paths. 
   - I want to be able to look at the HTML and see if we have similar issues like the ampersands and quotes and then make a decision on how to proceed. 
   - This will also let me set up the project's directory structure the way it should be for Github Pages. 
   - From there we will be able to make sure we have all essential files such as the index.html, robots.txt, sitemap.xml, all images, and all CSS and JS files. 

### Setup 

- I've removed completely the old project directory and repository so that we can start fresh. 
- We are currently working in the Project Directory that I would like to be the main directory for this project. 
- I just set up a new git branch 'webflow-2023' and a Github Repository 'webflow-2023' and we have made our first commit. 

If all makes sense, let us proceed from here. 

----

# Fully Detailed Process with No Combined Command Steps 

Making my old 2023 Webflow portfolio site static and deploying it to Github Pages. 

## Common Argument Flags 

- `-np` (or `--no-parent`) would get /section/ but not the entire site above /section/ 
- `-r` follow links within the website and download not just the initial page but also all linked pages it finds. It will traverse through the entire website structure, going from the homepage to all other pages by following the links between them.
- `-H` (span hosts) allows wget to follow links to other domains. Webflow sites typically store their assets (images, CSS, JS) on CDN domains like cdn.prod.website-files.com. Without -H, wget would only download files from august-house-llc.webflow.io and ignore all those external assets. We probably didn't use it before because other options like -p (page requisites) implicitly enable similar behavior. 
- `--no-convert-links`: This prevents wget from automatically modifying links in the downloaded HTML files. By default, wget tries to convert all links to work locally, but as you've experienced, this process is error-prone, especially with complex modern websites that have quotes, ampersands, and other special characters in URLs. 
- `-r -np -H`: Recursive download with no parent and span hosts
- `--tries=2`: Limit retries to 2 attempts
- `--domains=...`: Only follow links to these specific domains
- `--exclude-domains=...`: Skip these domains entirely
- `--no-convert-links`: Don't modify links in downloaded files
- `--html-extension`: Add .html extension to HTML files
- `--no-host-directories`: Don't create hostname directories
- `--reject "..."`: Skip downloading these file types in this step


## Step 1: 
Let's use a script to extract links and then download them separately. Here's how we could implement that approach. 

1. First, download just the HTML files:
```bash
wget -r -np -H --tries=2 --domains=august-house-llc.webflow.io,cdn.prod.website-files.com --exclude-domains=barnesandnoble.com,bn.com --no-convert-links --html-extension --no-host-directories --reject "*.css,*.js,*.png,*.jpg,*.jpeg,*.gif,*.webp,*.svg,*.ttf,*.woff,*.woff2" https://august-house-llc.webflow.io/
```

2. We need to capture more file types from the CDN, not just PNGs (.webp, .css, .js, etc.)
3. We need to handle the internal link structure for page navigation
4. We should create separate directories for different asset types

```bash
# Extract all CDN URLs (including CSS, JS, webp, etc.)
grep -r -o 'https://cdn.prod.website-files.com[^"'\'']*' . | sort | uniq > all-cdn-urls.txt

# Extract font URLs
grep -r -o 'https://ajax.googleapis.com[^"'\'']*' . | sort | uniq > font-urls.txt
grep -r -o 'https://fonts.googleapis.com[^"'\'']*' . | sort | uniq >> font-urls.txt
grep -r -o 'https://fonts.gstatic.com[^"'\'']*' . | sort | uniq >> font-urls.txt
grep -r -o 'https://use.typekit.net[^"'\'']*' . | sort | uniq >> font-urls.txt
```

Those have a relative path attached to the URL. We need to remove that. 

```bash
# Clean the CDN URLs file
cat all-cdn-urls.txt | sed 's/^.*:\(https:\/\/cdn\.prod\.website-files\.com[^[:space:]]*\).*$/\1/g' | sort | uniq > clean-cdn-urls.txt

# Clean the font URLs file
cat font-urls.txt | sed 's/^.*:\(https:\/\/[^[:space:]]*\).*$/\1/g' | sort | uniq > clean-font-urls.txt

# Combine the clean files
cat clean-cdn-urls.txt clean-font-urls.txt > all-external-assets.txt
```

Now lets remove duplicates. Then download them. 

```bash
# Remove duplicates and create a final clean list
sort all-external-assets.txt | uniq > final-assets-list.txt

# Download using the deduplicated list
wget -i final-assets-list.txt --no-host-directories --content-disposition --directory-prefix=assets
```

Fix the Ampersands. 
```bash
find . -name "*.html" -exec sed -i '' 's/&amp;/\&/g' {} \;
``` 

Fix URLs and paths. 

```bash
# Fix image URLs in background-image styles with single quotes
find . -name "*.html" -exec sed -i '' "s|url('https://cdn.prod.website-files.com/[^/]*/\([^']*\)')|url('assets/images/\1')|g" {} \;

# Fix image URLs in background-image styles with double quotes
find . -name "*.html" -exec sed -i '' 's|url("https://cdn.prod.website-files.com/[^/]*/\([^"]*\)")|url("assets/images/\1")|g' {} \;

# Fix image URLs in content attributes
find . -name "*.html" -exec sed -i '' 's|content="https://cdn.prod.website-files.com/[^/]*/\([^"]*\)"|content="assets/images/\1"|g' {} \;

# Fix image URLs in img src attributes
find . -name "*.html" -exec sed -i '' 's|src="https://cdn.prod.website-files.com/[^/]*/\([^"]*\)"|src="assets/images/\1"|g' {} \;

# Fix CSS file references
find . -name "*.html" -exec sed -i '' 's|href="https://cdn.prod.website-files.com/[^/]*/css/\([^"]*\)"|href="assets/css/\1"|g' {} \;

# Fix JS file references
find . -name "*.html" -exec sed -i '' 's|src="https://cdn.prod.website-files.com/[^/]*/js/\([^"]*\)"|src="assets/js/\1"|g' {} \;

# Fix Google webfont reference
find . -name "*.html" -exec sed -i '' 's|src="https://ajax.googleapis.com/ajax/libs/webfont/[^"]*"|src="assets/js/webfont.js"|g' {} \;

# Fix typekit references
find . -name "*.html" -exec sed -i '' 's|src="https://use.typekit.net/\([^"]*\)"|src="assets/js/\1"|g' {} \;
find . -name "*.html" -exec sed -i '' 's|href="https://use.typekit.net/\([^"]*\)"|href="assets/css/\1"|g' {} \;

# Fix Google Fonts references
find . -name "*.html" -exec sed -i '' 's|href="https://fonts.googleapis.com|href="assets/css/fonts.googleapis.com|g' {} \;
```

Target some that were missed. 

```bash
# Add .html extension to internal links
find . -name "*.html" -exec sed -i '' 's|href="\(/[^"]*\)"|href="\1.html"|g' {} \;

# Then fix any double extensions that might have been created
find . -name "*.html" -exec sed -i '' 's|href="\([^"]*\)\.html\.html"|href="\1.html"|g' {} \;
find . -name "*.html" -exec sed -i '' 's|href="\([^"]*\)\.css\.html"|href="\1.css"|g' {} \;
find . -name "*.html" -exec sed -i '' 's|href="\([^"]*\)\.js\.html"|href="\1.js"|g' {} \;
```
