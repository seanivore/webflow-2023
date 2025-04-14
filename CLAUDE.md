# Claude: About 'Webflow-2023' Project 

This is a pretty, custom designed portfolio for myself back in 2023. Original site is at https://august-house-llc.webflow.io/. 

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

## Step 1: 

