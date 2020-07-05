# Official Documentation of FSE (Fast Script Editor)

Copyright 2020 @ ps4star


TABLE OF CONTENTS:

1. Important notes about FSE
<br>1a. Types
<br>1b. Comments
<br>1c. @start and label ending
2. fcall
3. FSE Commands
4. **XSE Commands (what you're probably looking for)**
5. Example Code

A note about the format of this document: placeholder values will appear in parentheses (like this). Any time you see this, ignore the parentheses. FSE currently does not support them in any way, so please don't include them in real FSE code, or it will probably not compile.





## (1) Important notes about FSE

If you're used to scripting in XSE, there are a few things you'll want to be aware of before using FSE.

### Do not use ORG statements with commands like msgbox and applymovement
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
In any case where a string is being used as a function argument, it can not contain the character " ". Instead, the signifier "&sp" can be used. These scenarios are generally rare, however, as function arguments are almost always label names or item or pokemon names. Example:
```
Hello,&spI&spam&spa&spstring&sp(look&spma,&spno&spquotes).
```
Special characters require an extra escape character before them to work properly. This means \\\\n rather than simply \n.

### Decimal Int
If you really want to, you can use decimal int IDs for items and pokemon (again, just use the built-in table). They are also used for certain commands, such as warp.

### Hex Int
Hex ints can be used as alternatives to the built-in tables, and in some cases are required (such as msgbox types). Formatted as 0x**.

### Floating-point Numbers
There is currently no support for floating-point numbers, and likely never will be, as they're not used in XSE as far as I'm aware. Attempting to create a floating-point number will either cause it to be interpreted as a string or floored by JavaScript parseInt() to an integer.



## (1b) Comments

FSE supports only single-line comments, indicated by the ; (semicolon) char. These can be on an empty line or after commands.
```
const @myConst I'm a string literal and not a comment ; ok now we're in a comment
```
Comments are completely ignored by the compiler, even to the extent that they are not ported to XSE output.



## (1c) @start and label ending

The @start org is automatically added to XSE output. This label does not need to be closed with an end statement - the compiler handles this automatically. Any user-defined labels do need to be closed with end, however. Also note that any labels MUST come after your @start code, or it won't be executed.



## (2) fcall

fcall is the most important command in all of FSE, and thus deserves its own section in this document. It calls what I refer to as an "external function." External functions are stored in the file scripts.js in JS object format. External functions act in much the same way constants do, but for code blocks as opposed to data. Unlike constants, however, external functions can take parameters. And yes, you can even reference OTHER external functions in the definition of an external function (see below for a guide on how external functions work).

### fcall (func name) (args...)
###### Other Names: func
Not to be confused with call. Since arguments are separated by " ", any string arguments containing spaces are necessarily forbidden. However, you can use the special "&sp" signifier to get around this. Like with all strings, use escape characters for linebreaks (\\n not \n).

For information on how external functions work, and how to create your own, see [external function guide](https://github.com/ps4star/FSE/blob/master/functionguide.md).



## (3) FSE Commands

This section contains all the internal, FSE-exclusive commands. These commands exist for user convenience and are not ported to XSE output.

### autobreak (boolean)
###### Other Names: setautobreak
###### Default Value: true
Determines whether or not to use the Automatic Breaking System. If set to false, it will not be used.

### const @(const name) (value)
###### Other Names: define
Defines an internal constant.
```
const @(const name) (value)

EXAMPLE:
const @birchMoveSeq up up right right
const @birch 0x00

move @birch @birchMoveSeq
```
Note the "@" before (const name). It can actually be %, $, #, @, or !, it's up to your preference. If you're going to use @, be careful of potential name collisions with org names. You must include one of these special chars at the start of your const name, or the compiler will pitch a fit (this character must also must be included in all references to the const post-definition). (value) can be literally any arbitrary type of data (string, hex int, whatever). Const here works exactly as const does in JavaScript, or any other language that supports them. They simply replace the instances where they are referenced with their defined value via the JavaScript String.replace() method. Note that this does mean literally ANY reference to @(const name) will be replaced, even if it's unintentional, such as in the middle of a string literal, so be careful about using special chars if you're not trying to reference a const. Obviously, constants are not included in XSE output.

### pageonbreak (boolean)
###### Default Value: false
Determines whether or not to create a new page (\p) upon a linebreak. If set to false, \l (new line) will be used instead.

### setbreaklimit (new limit)
###### Other Names: breaklimit
###### Default Value: 27
Sets internal text break limit to decimal int (new limit). This value is used to determine how many characters of text to read before looking for a \n or \l point. These linebreaks are only allowed to occur at spaces, thus the default value of 27 as opposed to the actual limit of 34.

### setspeed (speed)
###### Other Names: setmovespeed
###### Default Value: normal
Sets internal movement speed. (speed) is a string, and its values can be veryslow (FR/LG only), slow, normal, fast, faster, or fastest, though not all of these speeds are available for every command, and some commands don't have speeds at all. See the movetable in tables.js for more info.



## (4) XSE Commands

Below is a list of all standard XSE commands currently usable in FSE.

### applymovement (movement target) (movement series...)
###### Other Names: move
Calls XSE applymovement, and adds a "waitmovement 0x0" call afterwards. (movement target) is a hex int representing the target of (movement series...), and (movement series...) is a list of space-delimited movement commands. See the SIDE NOTE below for information on how to format movement commands. Hex codes may still be used here if desired. See XSE documentation for more info on (movement target) values. To prevent the waitmovement call, see applymovementnowait below.
#### SIDE NOTE: The Movement System
The movement system in FSE can be confusing at first, but like everything here, it's supposed to be as convenient as possible. There are several different speeds of movement that gen 3 supports. If you look at the move table in tables.js, you'll notice that there are several copies of the basic movement directions (up, down, left, and right) that have speeds appended to them (veryslow (exclusive to FR/LG), slow, normal, fast, faster, fastest). So, instead of constantly having to say "upnormal", "downslow", etc, you can simply pre-define a speed, use the basic directions (up, down, left, and right), and the speed will be handled for you. Also, if you're REALLY lazy, you can use the shorthand "u", "d", "l", and "r", which are "up", "down", "left", and "right" respectively.

Here is an example of applymovement in action:
```
const @myMoveSequence u u d l r r r

setspeed normal
move 0xFF @myMoveSequence @myMoveSequence @myMoveSequence ; Repeats the same move sequence 3 times.
```
Referencing the full (speed-included) name of a movement is also allowed. The default speed is normal. See setspeed in section 3 for more information.

### applymovementnowait (movement target) (movement series...)
###### Other Names: movenowait
Calls XSE applymovement. See applymovement above for more details.

### clearflag (flag pointer)
###### Other Names: cf, clear
Calls XSE clearflag. I would recommend making (flag pointer) a constant rather than a hex literal, especially if you're modifying multiple different flags in 1 script.

### faceplayer
###### Other Names: face
Calls XSE faceplayer.

### lf
###### Other Names: lockface, lockfaceplayer
Calls XSE lock and faceplayer.

### lock
###### Other Names: l
Calls XSE lock.

### msgbox (string) (mode)
###### Other Names: msg
Calls XSE msgbox. 
```
msgbox Let's go to the mall! 0x4
```
(string) is a string literal (or constant), representing the text to display. (mode) is a hex integer representing the type of msgbox. Adding linebreaks in the message string is allowed, but the compiler already has a system for auto-filling these breaks. Keep in mind that an #org statement is not allowed here. See XSE msgbox documentation for more information on msgbox types. See setbreaklimit and pageonbreak in section 3 for more information on the automatic breaking system.

### release
###### Other Names: rel
Calls XSE release.

### setflag
###### Other Names: sf
Calls XSE setflag.
```
setflag (flag pointer)
```
(flag pointer) is an in-game hex flag ID. Note that you can also replace (flag pointer) with an internal const reference, meaning you can access flags by name rather than by a hex number. I would highly recommend doing this, as it lets you keep up with what flags do what, as opposed to using only the hex IDs of the flags.

### warp (map bank) (map number) (warp number)
Calls XSE warp. (map bank) is the map bank, (map number) is the map number, and (warp number) is the warp number. All of these are decimal ints.



## (5) Example Code

Below are a few examples (with XSE output for comparison) just to show off what FSE is capable of.

My personal favorite command in the whole language: applymovement...<br>

FSE
```
setspeed fast
movenowait 0xFF down right down right
move 0x00 up left left left
```
XSE
```
#dynamic 0x197D000

#org @start

applymovement 0xFF @off0
applymovement 0x00 @off1
waitmovement 0x0

end

#org @off0
#raw 0x15
#raw 0x18
#raw 0x15
#raw 0x18
#raw 0xFE

#org @off1
#raw 0x16
#raw 0x17
#raw 0x17
#raw 0x17
#raw 0xFE
```







