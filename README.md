# Welcome to FSE (FastScriptEditor) 1.1

This tool is designed to speed up the scripting process in ROM hack development by translating proprietary FSE code (documentation found in "ref.md") into standard XSE code.
There are several benefits to scripting this way rather than with XSE directly, with the main ones being that you're only going to be writing about 1/2 the amount of code to achieve the same outcome you would in XSE, as well as the fact that FSE comes pre-loaded with plenty of data tables (simply put in the common string name, like "potion", or "pokeball", and the hex value will be generated), and allows one to define and call custom functions.

# HOW TO INSTALL

There are 3 ways to install FSE.

## 1. GitHub Site

Although this is the easiest way to access FSE, it comes with a rather big drawback: you can't edit scripts.js. This means you can't define external functions. While saving internal functions to the cache is still an option, it's not as permanent as saving them externally.

link: https://ps4star.github.io/FSE/

## 2. Local (browser) \[RECOMMENDED\]

1. Download all the files from this repo as a .zip.
2. Extract files to a folder.
3. Find "index.html" in the folder.
4. Right click index.html.
5. "Open with..."
6. Select your preferred web browser.
7. Open.

## 3. Local (nw.js)

1. Download all the files from this repo as a .zip.
2. Go to https://nwjs.io/ and download the appropriate version of nw.js for your machine/OS.
3. Go inside "nwjs-sdk..." and find the file "nw.exe".
4. Whatever directory "nw.exe" is in, copy it and all other files in the directory into the same directory as FSE's "index.html", "package.json", "scripts.js", etc.
5. Once nw.exe and all other nw files are in the same directory as FSE, double click nw.exe and it should launch the program.

### New in 1.1
- Small bugfixes
- multichoice now recognized (takes 4 arguments: x, y, multichoice ID, can B cancel? (0x0=yes))

Tutorial: https://www.youtube.com/watch?v=fI1cGKpfEDw&feature=youtu.be
