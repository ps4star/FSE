Official documentation of FSE

Copyright 2020 @ ps4star


TABLE OF CONTENTS:

1. Environment Variables
2. Key Differences Between FSE and XSE
3. **Command Documentation (what you're probably looking for)**
4. Example Code




## Environment Variables

Environment variables exist mostly for the sake of convenience (while still giving the user plenty of power over what their script does), and can be modified at any point in the script. The variable "autoobtain" for example, will automatically add the traditional fanfare noise as well as "you obtained X!" textbox that appears when receing a pokemon or item.

To set the value of an environment variable, use this:
```
envr <var_name> <var_value>
EXAMPLE:
envr autoobtain false
```

#### autoobtain
###### Default Value: true

Adds a fanfare and msgbox after an item or pokemon obtain event.
