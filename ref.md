# Official Documentation of FSE

Copyright 2020 @ ps4star


TABLE OF CONTENTS:

1. Important notes about FSE
<br>1a. Types
<br>1b. Variables and Flags
2. Environment Variables
3. **Command Documentation (what you're probably looking for)**
4. Example Code

A note about the format of this document: placeholder values will appear in parentheses (like this). Any time you see this, ignore the parentheses. FSE currently does not support them in any way, so please don't include them in real FSE code, or it will probably not compile.





## Important notes about FSE

If you're used to scripting in XSE, there are a few things you'll want to be aware of before using FSE.

### ORG statements are added automatically. 
This means that rather than writing code such as:
```
msgbox @someOrg 0x4
...
#org @someOrg
= Let's go to the mall!
```
FSE does it like this:
```
msgbox Let's go to the mall! 0x4
```
And automatically generates an offset name and #org statement afterwards.

### FSE typically has multiple names for the same commands.
This may be a controversial feature, but yeah, most FSE commands have several names. The main point of this is to reduce the time the user has to spend looking up stuff in the documentation. So, if you forgot what the name of a command is, just take a guess, and you'll probably get it right. As a bonus, a lot of the aliases are shorter than the original XSE commands, which is always nice. However, if you're familiar with the standard XSE names and don't have any particular reason not to use them, then use them for the sake of standardization.

### EVERYTHING IS A TABLE!
While FSE does support raw hex values for the most part, it's highly recommended that you take advantage of the built-in tables. There are currently tables for pokemon IDs, item IDs, and movement IDs. More to (possibly) come in the future. The formatting for these tables is lowercased, no spaces, and no special characters. Items or pokemon with "." or "-" in their names can either be written with or without them. Some examples of weird names:

- up-grade OR upgrade
- mr.mime OR mrmime (notice how neither includes the space)
- exp.share OR expshare
- rm.1key OR rm1key (same for rm(.)2key, rm(.)4key, etc)



## Types in FSE

### String
Since technically everything in FSE is initially processed as a JavaScript string, string literals do not require quotes, unlike most languages. Example:
```
Hello, I am a string (look ma, no quotes).
```

### Decimal Int
FSE does support decimal ints, though there's not really any reason to use them (remember that there are tables for item and pokemon IDs).

### Hex Int
Hex ints can be used as alternatives to the built-in tables, and in some cases are required (such as msgbox types). Formatted as 0x****.



## Environment Variables

Environment variables exist mostly for the sake of convenience (while still giving the user plenty of power over what their script does), and can be modified at any point in the script. The variable "autoObtain" for example, will automatically add the traditional fanfare noise as well as "you obtained X!" textbox that appears when receing a pokemon or item.

To set the value of an environment variable, use this:
```
envr (var name) (var value)

EXAMPLE:
envr autoObtain false
```

### autoObtain
###### Default Value: true
###### Type: boolean

Adds a fanfare and msgbox after an item or pokemon obtain event. Must be manually set to false to prevent this effect.

### autoLock
###### Default Value: true
###### Type: boolean

Adds "lock" and "faceplayer" calls to the beginning of the script (just after the header). Must be manually set to false to prevent this effect.



## Command Documentation

Below is a list of all commands currently usable in FSE.

### msgbox (string) (mode)
###### Other Names: msg, message, messagebox, text, txt, filltext, domsgbox

Calls XSE msgbox. (string) is a string literal (or constant), representing the text you want to display, and (mode) is a hex integer representing the type of msgbox. See XSE msgbox documentation for more information on msgbox types.





















