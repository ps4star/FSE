Official documentation of FSE

Copyright 2020 @ ps4star


TABLE OF CONTENTS:

1. Environment Variables
2. Key Differences Between FSE and XSE
3. **Command Documentation (what you're probably looking for)**
4. Example Code



## Environment Variables

Environment variables exist mostly for the sake of convenience (while still giving the user plenty of power over what their script does), and can be modified at any point in the script. The variable "autoObtain" for example, will automatically add the traditional fanfare noise as well as "you obtained X!" textbox that appears when receing a pokemon or item.

To set the value of an environment variable, use this:
```
envr <var_name> <var_value>

EXAMPLE:
envr autoObtain false
```

### autoObtain
###### Default Value: true

Adds a fanfare and msgbox after an item or pokemon obtain event. Must be manually set to false to prevent this effect.

### autoLock
###### Default Value: true

Adds "lock" and "faceplayer" calls to the beginning of the script (just after the header). Must be manually set to false to prevent this effect.



## Key Differences Between FSE and XSE

If you're used to scripting in XSE, there are a few things you'll want to be aware of before using FSE.

ORGs are added automatically. This means that rather than writing code such as:
```
msgbox @someOrg 0x4
...
@someOrg
= Let's go to the mall!
```
FSE does it like this:
```
msgbox Let's go to the mall! 0x4
```
And automatically generates an offset name and #org statement afterwards.




