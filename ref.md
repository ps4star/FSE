# Official Documentation of FSE (Fast Script Editor)

Copyright 2020 @ ps4star


TABLE OF CONTENTS:

1. Important notes about FSE
<br>1a. Types
<br>1b. Comments
<br>1c. @start and label ending
2. FSE Functions
<br>2a. fcall
<br>2b. External Functions
<br>2c. Internal Functions
<br>2d. Function Saving and Cache Commands
3. FSE Commands
4. XSE Commands (what you're probably looking for)
<br>4a. **(READ THIS BEFORE 4B AND 4C) Note About XSE Commands**
<br>4b. List of XSE Commands with Modified Syntax
<br>4c. List of XSE Commands with Alternative Names
5. Examples
6. Info/legal

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
In any case where a string is being used as a function argument, it can not contain the character " ". Instead, the signifier "&sp" can be used. These scenarios are generally rare, however, as function arguments are almost always label names or item or pokemon names. Also, you can use const (see section 3) to automatically convert spaces to this signifier, and then reference said const as a function argument to avoid having to write out every "&sp". Example:
```
const @lookMa Hello, I am a string (look ma, no quotes).

fcall function_that_takes_a_string @lookMa ; passes multi-space string as function argument
```
Special characters require an extra escape character before them to work properly. This means \\\\n rather than simply \n.

### Decimal Int
If you really want to, you can use decimal int IDs for items and pokemon (again, just use the built-in table). They are also used for certain commands, such as warp.

### Hex Int
Hex ints can be used as alternatives to the built-in tables, and in some cases are required (such as msgbox types). Formatted as 0x**.

### Floating-point Numbers
There is currently no support for floating-point numbers, and likely never will be, as they're not used in XSE as far as I'm aware. Attempting to create a floating-point number will either cause it to be interpreted as a string or floored by JavaScript parseInt() to an integer.



## (1b) Comments

FSE supports single-line comments, indicated by the ; (semicolon) char. These can be on an empty line or after commands.
```
const @myConst I'm a string literal and not a comment ; ok now we're in a comment
```
FSE also supports multi-line comments, indicated by &comstart and &comend. Both of these instructions must be on otherwise-empty lines.
```
&comstart
Look
A
Multi-
Line
Comment
&comend
```
Comments are completely ignored by the compiler, even to the extent that they are not ported to XSE output.



## (1c) @start and label ending

The @start org is automatically added to XSE output. This label does not need to be closed with an end statement - the compiler handles this automatically. Any user-defined labels do need to be closed with end, however. Also note that any labels MUST come after your @start code, or it won't be executed.



## (2) FSE Functions

FSE has two types of functions: internal and external. External functions are located in the scripts.js file (hence the name external - they're in a different file from the compiler). Internal functions are functions which are defined in FSE code. Internal functions can be saved as externals via the savefunc command (found in this section, see below). See below for more about functions and how to call them.



## (2a) fcall

fcall is the most important command in all of FSE. It calls a function (whether it's internal or external doesn't matter) and passes parameters into it as specified in the function definition.

### fcall (func name) (args...)
Not to be confused with call. Since arguments are separated by " ", any string arguments containing spaces are necessarily forbidden. However, you can use the special "&sp" signifier to get around this. Like with all strings, use escape characters for linebreaks (\\n not \n). Additionally, you can use a const to get around this "&sp" limitations, as consts automatically convert spaces to &sp.



## (2b) External Functions

External functions are loaded in as soon as you start FSE. Thus, they can be called at any point, and there is no need to define them explicitly.

For information on how external functions work, and how to create your own, see [external function guide](https://github.com/ps4star/FSE/blob/master/functionguide.md).



## (2c) Internal Functions

Internal functions are explicitly defined in-script, and cannot be called prior to their definition. All function (and cache)-related commands start with the "$" character.

A standard internal function definition:
```
$funcstart sendm
msg %ARG_1 0x4
$funcend

fcall sendm MyMessage ;Displays "MyMessage" in a text box.
```
Read below for more information on these function commands.

### $funcstart (func name)
Defines the function name as (func name) and begins a function definition.

### $funcend
Ends a function definition.



## (2d) Function Saving and Cache Commands

Internal functions are automatically "saved" to the JS localStorage cache, though this can be disabled if the user desires. Note that this form of storage is not the same as what external functions use, and if you really care about using a function for more than a couple of sessions, you should define it in scripts.js. Any time you clear your browser history, cookies, data, etc, you run a very high risk of deleting your function cache. Look up "localStorage" online for more info on how this works.

With that said, below is a list of function cache commands.
### $autosav (boolean)
###### Default Value: true
Determines whether or not to cache internal functions. Can be set at multiple points in the script. If a function is defined while this is false, it will not be written to the cache, otherwise it will. Note that this, like all other compiler variables with default values, will be reset to true every time the compiler is executed, even within the same session.

### $clearall
Clears the internal function cache. If you care about your cache, be weary of copying and pasting FSE code into the editor from other sources or websites, as there are no restrictions on this command.



## (3) FSE Commands

This section contains all the internal, FSE-exclusive commands. These commands exist for user convenience and are not ported to XSE output.

### autobreak (boolean)
###### Other Names: setautobreak
###### Default Value: true
Determines whether or not to use the Automatic Breaking System. If set to false, it will not be used.

### compile (data...)
Converts (data...) to XSE and outputs result to an alert box. Does not port (data...) to actual XSE output. Only useful for debugging.

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
###### Default Value: 30
Sets internal text break limit to decimal int (new limit). This value is used to determine how many characters of text to read before looking for a \n or \l point. These linebreaks are only allowed to occur at spaces, thus the default value of 30 as opposed to the actual limit of 34.

### setlabelname (new label name)
###### Default Value: offset
Sets the naming convention of auto-generated labels, such as those used for msgbox and applymovement.

### setspeed (speed)
###### Other Names: setmovespeed
###### Default Value: normal
Sets internal movement speed. (speed) is a string, and its values can be veryslow (FR/LG only), slow, normal, fast, faster, or fastest, though not all of these speeds are available for every command, and some commands don't have speeds at all. See the movetable in tables.js for more info.

### xse (raw xse...)
###### Other Names: raw
Copies (raw xse...) to XSE output. Does not de-reference constants.

### xsed (raw xse...)
Copies (raw xse...) to XSE output. De-references constants.


## (4) XSE Commands



## (4a) Note About XSE Commands

FSE has support for all XSE commands, but not in the way that you might think. If FSE does not "recognize" a command, it will assume it's XSE code, and will simply copy and paste it to XSE output, with the only modifications being that it will still scan for const references. This means only some XSE commands (those which are particularly inconvenient or have optimization potential, or those which have alternative names) are actually "recognized", while the rest are simply de-referenced and copied without any special attention given to them by the compiler.

For this reason, the below list is NOT a complete or comprehensive list of all commands in XSE, simply a list of all the ones that work differently (or have "modified syntax") in FSE than XSE. Note that 4c contains a different XSE command list. The commands in the 4c list do not need to be written differently, but simply have alternative (shortened) names (though all of these also retain their original XSE names, i.e. you're not forced to use any of these alternative names if you don't want to). For example, there is a command called "lf" which simply produces the XSE output "lock(linebreak)faceplayer". These are technically recognized by the compiler, but generally don't have any "modified syntax", thus they are in a separate list.



## (4b) List of XSE Commands with Modified Syntax

Below is a list of all standard XSE commands currently recognized by the compiler which are written differently in FSE compared to XSE.

### @(label name)
###### Other Names: label, lbl, @
Creates an XSE org with (label name). Note that "@" is specified as an "other name" despite already being the primary name. This is because it can be used both with a space and without a space ("@lblname" vs "@ lblname"). @ is the only name this applies to (i.e. the other names require a space and cannot be used without one). Any non-leading @s found in the label name will cause an error. Note that all labels must come after your @start code. Code found outside of any labels will throw a compiler error. All label references MUST start with @, otherwise invalid XSE code will be generated, as there is minimal error-checking for label references.

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

### bufferattack (attack name)
Calls XSE bufferattack. (attack name) can be a string representing the name of the move, a decimal int representing the move ID, or a hex int representing the move ID.

### bufferpokemon (pokemon name)
Calls XSE bufferpokemon. (pokemon name) can be a string representing the name of the pokemon, a decimal int representing the pokemon ID, or a hex int representing the pokemon ID.

### givepokemon (pokemon name) (pokemon level) (pokemon held item)
###### Other Names: pokemon
Calls XSE givepokemon. All 3 args can either be hex int IDs, decimal int IDs, or, for (pokemon name) and (pokemon held item) only, a string representing the name of the pokemon or held item.

### msgbox (string) (mode)
###### Other Names: msg
Calls XSE msgbox. 
```
msgbox Let's go to the mall! 0x4
```
(string) is a string literal (or constant), representing the text to display. (mode) is a hex integer representing the type of msgbox. Adding linebreaks in the message string is allowed, but the compiler already has a system for auto-filling these breaks. Keep in mind that an #org statement is not allowed here. See XSE msgbox documentation for more information on msgbox types. See setbreaklimit and pageonbreak in section 3 for more information on the automatic breaking system.



## (4c) List of XSE Commands with Alternative Names

### clearflag (flag pointer)
###### Other Names: cf, resetflag
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

### release
###### Other Names: rel
Calls XSE release.

### setflag (flag)
###### Other Names: sf
Calls XSE setflag. (flag) is a hex int representing the flag ID.

### warp (map bank) (map number) (warp number)
##### Other Names: warpto
Calls XSE warp. (map bank) is the map bank, (map number) is the map number, and (warp number) is the warp number. All of these are decimal ints.



## (5) Examples

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

Some function stuff.

FSE
```
const @ebonyName Ebony Dark'ness Dementia Raven Way ;HEY RAVEN DO U KNOW WHERE MY SWEATER I

$funcstart display_name
msg Hello, %ARG_1! 0x4
$funcend

fcall display_name @ebonyName

msg @ebonyName 0x4
```


## (6) Info/legal

Thanks for reading about FSE. It's something I've been working hard on over the past few weeks. As for legal stuff, feel free to distribute this as long as it's done non-commercially and credit is given to me (ps4star) for the files which I created. This means everything except the file ace.js and the ace folder - I did not create the ACE editor and any modification, distribution, etc. of that editor is subject to ACE's license.

You can find the exact license within this repo as LICENSE.txt.

















