# Official Documentation of FSE (Fast Script Editor)

Copyright 2020 @ ps4star


TABLE OF CONTENTS:

1. Important notes about FSE
<br>1a. Types
<br>1b. Constants
<br>1c. Comments
2. Environment Variables
3. **Command Documentation (what you're probably looking for)**
4. Example Code

A note about the format of this document: placeholder values will appear in parentheses (like this). Any time you see this, ignore the parentheses. FSE currently does not support them in any way, so please don't include them in real FSE code, or it will probably not compile.





## (1) Important notes about FSE

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

### EVERYTHING IS A TABLE!
While FSE does support raw hex values for the most part, it's highly recommended that you take advantage of the built-in tables. There are currently tables for pokemon IDs, item IDs, and movement IDs. More to (possibly) come in the future. The formatting for these tables is lowercased, no spaces, and no special characters. Items or pokemon with "." or "-" in their names can either be written with or without them. Some examples of weird names:

- up-grade OR upgrade
- mr.mime OR mrmime (notice how neither includes the space)
- exp.share OR expshare
- rm.1key OR rm1key (same for rm(.)2key, rm(.)4key, etc)

The internal tables can be located in the "Data Parsers" folder of this repo if you'd like to see for yourself how to use them.

### Case-insensitivity
All command names and environment variable names are case-insensitive. Obviously, things like string literals and defined constants and flags aren't, as they are user-defined.



## (1a) Types

### String
Since technically everything in FSE is initially processed as a JavaScript string, string literals do not require quotes, unlike most languages, but including them without the addition of escape characters **shouldn't** cause compilation problems. Example:
```
Hello, I am a string (look ma, no quotes).
```

### Decimal Int
If you really want to, you can use decimal int IDs for items and pokemon (again, just use the built-in table). They are also used for certain commands, such as warp.

### Hex Int
Hex ints can be used as alternatives to the built-in tables, and in some cases are required (such as msgbox types). Formatted as 0x**.

### Floating-point Numbers
There is currently no support for floating-point numbers, and likely never will be, as they're not used in XSE as far as I'm aware. Attempting to create a floating-point number will either cause it to be interpreted as a string or floored by JavaScript parseInt() to an integer.

## (1b) Constants

FSE has support for constants. Constants are simply "shortcuts" and cannot be modified after definition (as in any other language).

NOTE: Do not use "=" when assigning values to consts.

### const
###### Other Names: define
Defines an internal constant.
```
const @(const name) (value)

EXAMPLE:
const @birchMoveSeq up up right right
const @birch 0x00

move @birch @birchMoveSeq
```
Note the "@" before (const name). It can actually be %, $, #, @, or !, it's up to your preference. You must include one of these chars at the start of your const name, or the compiler will pitch a fit (this character must also must be included in all references to the const post-definition). (value) can be literally any arbitrary type of data (string, hex int, whatever). Const here works exactly as const does in JavaScript, or any other language that supports them. They simply replace the instances where they are referenced with their defined value via the JavaScript String.replace() method. Note that this does mean literally ANY reference to @(const name) will be replaced, even if it's unintentional, such as in the middle of a string literal, so be careful about using special chars if you're not trying to reference a const. Obviously, constants are not included in XSE output.

## (1c) Comments

FSE supports only single-line comments, indicated by the ; (semicolon) char. These can be on an empty line or after commands.
```
const @myConst I'm a string literal and not a comment ; ok now we're in a comment
```
Comments are completely ignored by the compiler, even to the extent that they are not ported to XSE output.



## (2) Environment Variables

Environment variables exist mostly for the sake of convenience (while still giving the user plenty of power over what their script does), and can be modified at any point in the script. The variable "autoObtain" for example, will automatically add the traditional fanfare noise as well as "you obtained X!" textbox that appears when receing a pokemon or item.

To set the value of an environment variable, use this:
```
envr (var name) (var value)

EXAMPLE:
envr autoObtain false
```

### autoLock
###### Default Value: true
###### Type: boolean
Adds "lock" and "faceplayer" calls to the beginning of the script (just after the header).

### autoObtain
###### Default Value: true
###### Type: boolean
Adds a fanfare and msgbox after an item or pokemon obtain event.

### autoRelease
###### Default Value: true
###### Type: boolean
Adds an XSE release call to the end of the script (just before end).

### setObtainFanfare
###### Default Value: 0x13E
###### Type: hex int
Sets the fanfare ID for autoObtain. If autoObtain is false, this does nothing.

### setObtainString
###### Default Value: You received a @POKEMON_NAME!
###### Type: string
Sets the string for autoObtain. Use @POKEMON_NAME to specify the pokemon name (not required). If autoObtain is false, this does nothing.

## (3) Command Documentation

Below is a list of all commands currently usable in FSE.

### applymovement (movement target) (...movement series...)
###### Other Names: move
Calls XSE applymovement, and adds a "waitmovement 0x0" call afterwards. (movement target) is a hex int representing the target of (...movement series...), and (...movement series...) is a list of space-delimited movement commands. See the SIDE NOTE below for information on how to format movement commands. Hex codes may still be used here if desired. See XSE documentation for more info on (movement target) values. To prevent the waitmovement call, see applymovementnowait below.
#### SIDE NOTE: The Movement System
The movement system in FSE can be confusing at first, but like everything here, it's supposed to be as convenient as possible. There are several different speeds of movement that gen 3 supports. If you look at the move table in tables.js, you'll notice that there are several copies of the basic movement directions (up, down, left, and right) that have speeds appended to them (veryslow (exclusive to FR/LG), slow, normal, fast, faster, fastest). So, instead of constantly having to say "upnormal", "downslow", etc, you can simply pre-define a speed, use the basic directions (up, down, left, and right), and the speed will be handled for you.

Here is an example of applymovement in action:
```
const @myMoveSequence up up down left right right right

setspeed normal
move 0xFF @myMoveSequence
```
Referencing the full (speed-included) name of a movement is also allowed. The default speed is normal. See setspeed below for more information.

### applymovementnowait (movement target) (...movement series...)
###### Other Names: movenowait
Calls XSE applymovement. See applymovement above for more details.

### msgbox (string) (mode)
###### Other Names: msg
Calls XSE msgbox. (string) is a string literal (or constant), representing the text you want to display, and (mode) is a hex integer representing the type of msgbox. See XSE msgbox documentation for more information on msgbox types.

### setflag
###### Other Names: sf
Calls XSE setflag.
```
setflag (flag pointer)
```
(flag pointer) is an in-game hex flag ID. Note that you can also replace (flag pointer) with an internal const reference, meaning you can access flags by name rather than by a hex number. I would highly recommend doing this, as it lets you keep up with what flags do what, as opposed to using only the hex IDs of the flags.

### setspeed
###### Other Names: setmovespeed
Sets internal movement speed. Values can be veryslow (FR/LG only), slow, normal, fast, faster, and fastest, though not all of these speeds are available for every command, and some commands don't have speeds at all. See the movetable in tables.js for more info.

### warp (map bank) (map number) (warp number)
Calls XSE warp. (map bank) is the map bank, (map number) is the map number, and (warp number) is the warp number. All of these are decimal ints.



## (4) Example Code

Below are a few examples (with XSE output for comparison) just to show off what FSE is capable of.












