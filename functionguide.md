# FSE (Fast Script Editor) Official External Function Guide

TABLE OF CONTENTS:
1. How to Write External Functions
2. List of Standard Lib Functions

### (1) How to Write External Functions

All external functions are stored as JSON files in the scripts folder. You MUST place all functions in this folder, or the compiler will error when trying to access your script.
You can, however, create subfolders within scripts, as long as you include the filepath in all references to your script.

The easiest way to explain how to write functions is by showing one:
```
{
	"body" : [
		"lf",
		"fanfare 0x13E",
		"msgbox You obtained a %ARG_1! 0x4",
		"release"
	],
	"args" : 1
}
```
body is an array of strings representing lines of FSE code, and args is how many arguments the function takes. Arguments are simply inserted via %ARG_X into the function, and
are replaced with their corresponding values at compile time.

### (2) List of Standard Lib Functions
```
obtain-pokemon @MESSAGE ;Plays fanfare 0x13E and displays a textbox containing the string @MESSAGE.
```
