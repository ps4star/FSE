# FSE (Fast Script Editor) Official External Function Guide

TABLE OF CONTENTS:
1. How to Write External Functions

## (1) How to Write External Functions

All external functions are stored as JS objects in the variable "allScripts" found in the scripts.js file.

The easiest way to explain how to write external functions is by showing one:
```javascript
var allScripts = {

	"obtain-poke" :
	
`fanfare 0x13E
msgbox You received a %ARG_1! 0x4`

}
```
Notice the %ARG_1 at the end. When an external function is being evaluated, the number of arguments is determined by the highest %ARG_X value found within the code, and when a function is called, any %ARG_X references are replaced with the argument values (in other words, the parameters the function is called with get passed into the function), just like how functions in languages like Python or JS work.

You can also reference other external functions within an external function definition:
```javascript
var allScripts = {

	"obtain-poke" :
	
`fanfare 0x13E
msgbox You received a %ARG_1! 0x4`,

	"name-poke" :
	
`msg Would you like to give a\\nnickname to %ARG_1? 0x5
compare 0x800D 0x1
if 0x1 call %ARG_2`,

	"obtain-and-name" :
	
`fcall obtain-poke %ARG_1
fcall name-poke %ARG_1 %ARG_2`

}
```
