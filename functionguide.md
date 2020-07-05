# FSE (Fast Script Editor) Official External Function Guide

TABLE OF CONTENTS:
1. How to Write External Functions
2. List of Standard Lib Functions

### (1) How to Write External Functions

All external functions are stored as JS objects in the variable "allScripts" found in the scripts.js file.

The easiest way to explain how to write external functions is by showing one:
```javascript
var allScripts = {
	"obtain-poke" :
`fanfare 0x13E
msgbox You received a %ARG_1! 0x4`
}
```
body is an array of strings representing lines of FSE code, and args is how many arguments the function takes. Arguments are simply inserted via %ARG_X into the function, and
are replaced with their corresponding values at compile time.

### (2) List of Standard Lib Functions
```
obtain-poke @MESSAGE ;Plays fanfare 0x13E and displays a textbox containing the string @MESSAGE.
```
