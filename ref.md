# Official Documentation of FSE (Fast Script Editor)

Copyright 2020 @ ps4star


TABLE OF CONTENTS:

1. Important notes about FSE
<br>1a. Types
<br>1b. Comments
<br>1c. @main and label ending
2. Functions
<br>2a. fcall
<br>2b. External Functions
<br>2c. Internal Functions
<br>2d. Special Function Arguments
3. Loops and Expansion Statements
4. FSE Commands
5. XSE Commands (what you're probably looking for)
<br>5a. **(READ THIS BEFORE 4B AND 4C) Note About XSE Commands**
<br>5b. List of XSE Commands with Modified Syntax
<br>5c. List of XSE Commands with Alternative Names
6. List of all Special % Strings
7. Info/legal

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

The internal tables can be located in the tables.js file of this repo if you'd like to see for yourself how to use them.

### Case-insensitivity
All command names, and const names are case-insensitive. Functions aren't, however.



## (1a) Types

### String
Since technically everything in FSE is initially processed as a JavaScript string, string literals do not require quotes, unlike most languages, but including them without the addition of escape characters **shouldn't** cause compilation problems. Example:
```
Hello, I am a string (look ma, no quotes).
```
In any case where a string is being used as a function argument, it can not contain the character " ". Instead, the signifier "&sp" can be used. These scenarios are generally rare, however, as function arguments are almost always label names or item or pokemon names. Also, you can use const (see section 5) to automatically convert spaces to this signifier, and then reference said const as a function argument to avoid having to write out every "&sp". Example:
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

### Tables
Tables can be defined as follows:
```
$table @my_table

key1 value1
key2 value2
key3 value3

$tabend
```
Accessing table elements:
```
;accesses element from table
msg key1@my_table 0x4 ;displays 'value1'
```



## (1b) Comments

FSE supports single-line comments, indicated by the ; (semicolon) char. These can be on an empty line or after commands.
```
const @myConst I'm a string literal and not a comment ; ok now we're in a comment
```
";" can be escaped for use in strings as "\\;" (I know, it's weird)
```
msg Hi Brendan\; Hi May 0x4 ;this is a comment, but the semicolon earlier isn't, since it was escaped with \
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



## (1c) @main and label ending

The @main org is automatically added to XSE output. This label does not need to be closed with an end statement - the compiler handles this automatically. Any user-defined labels do need to be closed with end, however. Also note that any labels MUST come after your @main code, or it won't be executed.



## (2) Functions

FSE has two types of functions: internal and external. External functions are located in the scripts.js file (hence the name external - they're in a different file from the compiler). Internal functions are functions which are defined in FSE code. See below for more about functions and how to call them.



## (2a) fcall

fcall is the most important command in all of FSE. It calls a function (whether it's internal or external doesn't matter) and passes parameters into it as specified in the function definition.

### fcall (func name) (args...)
Not to be confused with call. Since arguments are separated by " ", any string arguments containing spaces are necessarily forbidden. However, you can use the special "&sp" signifier to get around this. Like with all strings, use escape characters for linebreaks (\\n not \n). Additionally, you can use a const to get around this "&sp" limitation, as consts automatically convert spaces to &sp.



## (2b) External Functions

External functions are loaded in as soon as you start FSE. Thus, they can be called at any point, and there is no need to define them explicitly. External functions are stored in "libraries", with each library having its own name. These library names need to be referenced in any fcall references to the function. This can be bypassed with using namespace.

### using namespace (lib)
###### Other Names: namespace, writetop, loadlib, surface
Writes all library functions represented by string (lib) to top-level namespace. Does not delete (lib) itself from the namespace.

Example:
```
fcall stdlib.nickname_frlg ;valid
fcall nickname_frlg ;invalid, will error

namespace stdlib ;nickname is currently only available for FRLG until I figure out
;how to make it not crash in RSE. Sorry :(

fcall nickname_frlg ;valid
fcall stdlib.nickname_frlg ;still valid
```

For information on how external functions work, and how to create your own, see [external function guide](https://github.com/ps4star/FSE/blob/master/functionguide.md).



## (2c) Internal Functions

Internal functions are explicitly defined in-script, and cannot be called prior to their definition. All function-related commands start with the "$" character.

A standard internal function definition:
```
$funcstart sendm
msg %arg1 0x4
$funcend

fcall sendm MyMessage ;Displays "MyMessage" in a text box.
```
Read below for more information on these function commands.

### $funcstart (func name)
Defines the function name as (func name) and begins a function definition.

### $funcend
Ends a function definition.



## (2d) Special Function Arguments

Along with the standard "%argX", FSE supports explicit typing (to an extent) of function arguments. This is done by adding a "special character" to the end of an %argX statement to denote the type. Currently supported are:
- P for pokemon
- I for item
- A for battle move
- H for hex value

%argXP example
```javascript
...
"set-seen":
	
`setvar 0x8004 %arg1P
special 0x163`
...
```
The %arg1P here is automatically conformed into a hex int representing a pokemon ID. For example, if you pass "mew" into the set-seen function, it will convert the string to 0x97. If you pass 0x97, it will convert to 0x97. If you pass 151, it will convert to 0x97.

The other two types of special arguments are currently not used in any standard lib functions, but still work just the same.



## (3) Loops and Expansion Statements


### Loops
FSE loops are quite limited. You must specify a number of times to loop, and with the exception of functions, these cannot be expressions, only static numbers. Loops begin with "loop" or "lstart" and end with "loopend" or "lend". Use %loopiter to specify the loop iteration number. See below for more info on %loopiter and its variations.

A loop inside @main
```
lf

loop 5
msg Message Number: %loopiter 0x4 ;%loopiter is the current loop iteration number
lend

rel
```
#### Modifying %loopiter
%loopiter can be indirectly modified by adding optional arguments to the loop start. Argument 1 is always required, and is the number of times to loop. Argument 2 is the value to initialize %loopiter at, and argument 3 is the step to increase %loopiter by for each iteration. If these optional arguments are not included, their default values will be 0 and 1 respectively (starts at 0, increases by 1 for each iter).

Making %loopiter increase by 2 for each loop:
```
loop 5 0 2 ;starts at 0, up by 2 each iter
msg %loopiter 0x4 ;0, 2, 4, 6, 8
lend
```
Offsetting %loopiter by 3:
```
loop 5 3 ;starts at 3, up by 1 each iter
msg %loopiter 0x4 ;3, 4, 5, 6, 7
lend
```
#### %loopiter Variations
%loopiter currently only has 1 variation: %loopiterH. It simply conforms the data passed into it to a hex int. Fun fact: in pre-release versions of FSE (which no longer exist and were never released/archived in any way), there was a second one called %loopiterL@constName, which construed %loopiter as an index of list @constName and returned the element at the specified index. However, this is now deprecated since the introduction of constant properties, and is instead accomplished with indexat%loopiter@constName

### Expansion Statements
Expansion statements are where things get a little bit... meta. They work exactly the same way that loops do (they even share most of the exact same code in the compiler), and everything mentioned in the loops section also applies to them. The only difference is that they output to FSE input rather than XSE output. Also, if the compiler detects any expansion statements, the typical compilation process will be completely de-railed in order to process the expansions before actual compilation. Simply hit compile a second time after this process to truly compile.

Expansion statements are started with "expstart" or "!se" and ended with "expend" or "!ee"
```
!se 6 ;loops 6 times
@name%loopiter ;@name0, @name1, etc...
fcall nickname
ret
!ee
```
To use iter commands, add additional arguments to !se/expstart. The second (optional) is the starting iter value (positives only), and the third (optional) is the multiter value (and just a reminder, the first argument is required and represents the number of times to loop).
```
!se 4 3 ;loops 4 times, initializes %loopiter at 3
msg %loopiter 0x4 ;3, 4, 5, 6
!ee
```
Loop with increase of 2 per iteration with exp statement
```
!se 4 0 2 ;starts at 0, increases by 2 each loop. loops 4 times.
@name%loopiter ;generates labels @name0, @name2, @name4, and @name6
;some code
ret
!ee
```

A GIF of an expansion statement in action:<br>
![](https://i.ibb.co/r2ZFNy5/ezgif-com-video-to-gif.gif)



## (4) FSE Commands

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
Note the "@" before (const name). It can actually be %, $, #, @, or !, it's up to your preference. If you're going to use @, be careful of potential name collisions with org names. You must include one of these special chars at the start of your const name, or the compiler will pitch a fit (this character must also must be included in all references to the const post-definition). (value) can be literally any arbitrary type of data (string, hex int, whatever). Const here works exactly as const does in JavaScript, or any other language that supports them. They simply replace the instances where they are referenced with their defined value via the JavaScript String.replace() method. Note that this does mean literally ANY reference to @(const name) will be replaced, even if it's unintentional, such as in the middle of a string literal, so be careful about using special chars if you're not trying to reference a const. The only exception to this is command names.

#### List Constants
As you may know, indexat%argX@constName and indexat%loopiter@constName both take decimal integers, but more specifically, these integers represent list indices. If you define a constant which contains a string with multiple spaces, you can later have the compiler construe it as a "list/array" via indexat%argX@constName for funcs and indexat%loopiter@constName for loops. Thus, list constants do not actually exist in the same sense that constants in general do, it's just that all constants have the ability to be construed as such under certain circumstances if the user desires.

You probably have no idea what any of that means; here's an example.
```
const @myList twenty fourty&speight ;this list const has 2 elements. We use &sp to signify a space without
;breaking the rule of "space = new index"

lstart getln@myList ;loops through every item in @myList
msg indexat%loopiter@myList ;gets element of @myList corresponding to %loopiter
lend
```

#### Constant Properties
Whenever a constant is defined, additional constants with the same name, but with special prefixes (think of them like sister constants) are added to the const table as well. Constant properties are used to get the length of constants (getln@myConst), and, for list constants, the element stored at a specified index (indexat(index)@myConst).

Constant properties example
```
;getln@constName

;the value of getln differs depending on if string contains spaces (list constant) or not (standard string).
const @myString kek ;getln@myString = 3
const @myList kek1 kek2 ;getln@myList = 2

;getlnreal@constName

;always returns the string length rather than list length, even for list constants
const @myString kek ;getlnreal@myString = 3
const @myList kek1 kek2 ;getlnreal@myList = 9 (counts spaces)

;indexat(decimal int)@constName - this one requires a number, (decimal int), specifying the index to access, unlike getln
;which doesn't take any special pseudo-arguments like this.

const @myList kek1 kek2 ;indexat0@myList = kek1, indexat1@myList = kek2
```

### using namespace (lib)
###### Other Names: namespace, writetop, loadlib, surface
See section 2b (external functions).

### pageonbreak (boolean)
###### Default Value: false
Determines whether or not to create a new page (\p) upon a linebreak. If set to false, \l (new line) will be used instead.

### setbreaklimit (new limit)
###### Other Names: breaklimit
###### Default Value: 34
Sets internal text break limit to decimal int (new limit). This value is used to determine how many characters of text to read before looking for a \n or \l point. These linebreaks are only allowed to occur at spaces, and if the linebreak limit is exceeded at any point, the processor will look for the last space it encountered, and replace it with a break point.

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


## (5) XSE Commands



## (5a) Note About XSE Commands

FSE has support for all XSE commands, but not in the way that you might think. If FSE does not "recognize" a command, it will assume it's XSE code, and will simply copy and paste it to XSE output, with the only modifications being that it will still scan for const references. This means only some XSE commands (those which are particularly inconvenient or have optimization potential, or those which have alternative names) are actually "recognized", while the rest are simply de-referenced and copied without any special attention given to them by the compiler.

For this reason, the below list is NOT a complete or comprehensive list of all commands in XSE, simply a list of all the ones that work differently (or have "modified syntax") in FSE than XSE. Note that 4c contains a different XSE command list. The commands in the 4c list do not need to be written differently, but simply have alternative (shortened) names (though all of these also retain their original XSE names, i.e. you're not forced to use any of these alternative names if you don't want to). Some commands in the list also have additional XSE command calls automatically performed after them. "lf" for example calls XSE lock, then XSE faceplayer, both in 1 command. These are technically recognized by the compiler, but generally don't have any "modified syntax", thus they are in a separate list.



## (5b) List of XSE Commands with Modified Syntax

Below is a list of all standard XSE commands currently recognized by the compiler which are written differently in FSE compared to XSE.

### @(label name)
###### Other Names: label, lbl, @
Creates an XSE org with (label name). Note that "@" is specified as an "other name" despite already being the primary name. This is because it can be used both with a space and without a space ("@lblname" vs "@ lblname"). @ is the only name this applies to (i.e. the other names require a space and cannot be used without one). Any non-leading @s found in the label name will cause an error. Note that all labels must come after your @main code. Code found outside of any labels will throw a compiler error. All label references MUST start with @, otherwise invalid XSE code will be generated, as there is minimal error-checking for label references.

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
Referencing the full (speed-included) name of a movement is also allowed. The default speed is normal. See setspeed in section 4 for more information.

### applymovementnowait (movement target) (movement series...)
###### Other Names: movenowait
Calls XSE applymovement. See applymovement above for more details.

### applymovementreverse (movement target) (movement series...)
###### Other Names: mover, movereverse
Calls XSE applymovement, and adds a "waitmovement 0x0" call afterwards, but reverses (movement series...). See applymovement above for more details.

### applymovementnowaitreverse (movement target) (movement series...)
###### Other Names: movenowaitreverse
Calls XSE applymovement, but reverses (movement series...). See applymovement above for more details.

### bufferattack (buffer) (attack name)
Calls XSE bufferattack. (attack name) can be a string representing the name of the move, a decimal int representing the move ID, or a hex int representing the move ID.
#### SIDE NOTE
For bufferattack and the 3 buffer commands below, (buffer) can be a string in the format of "\[bufferx]" where x is a decimal int, or it can be a hex number (like 0x00). \[buffer1] corresponds to hex 0x00, \[buffer2] is 0x01, etc.

### bufferfirstpokemon (buffer)
Calls XSE bufferfirstpokemon.

### bufferitem (buffer) (item name)
Calls XSE bufferitem. (item name) can be a string representing the name of the item, a decimal int representing the item ID, or a hex int representing the item ID.

### bufferpokemon (buffer) (pokemon name)
Calls XSE bufferpokemon. (pokemon name) can be a string representing the name of the pokemon, a decimal int representing the pokemon ID, or a hex int representing the pokemon ID.

### compare (value to compare) (value to compare against)
###### Other Names: comp
Calls XSE compare. (value to compare) is a hex int representing an in-game variable, and (value to compare against) is a hex or decimal int representing the value to compare (value to compare) against. If you need to use a sequence of compare calls, see compseq below for a faster method of doing it.

### compseq (value to compare) (label name...)
###### Other Names: compareseq, compsequence, comparesequence
Repeatedly calls XSE compare (using (value to compare) and the value to compare against) and if 0x1 goto (label name). The value to compare against increases by 1 for each (label name...), and is initialized at 0x0. The final value to compare against in the sequence is set to 0x7F (the menu cancel option). This can be avoided by using the explicit form of this command: compseqexplicit.

Since this is easily the most confusing command in the entire language, here's an example with compiler output:

FSE
```
compseq 0x8000 0x0 @option1 @option2 @option3 @option4 @option5 @option6 @canceled
```
XSE (this was copied from [Sierra's MEGA-HUGE XSE Scripting Tutorial](https://www.pokecommunity.com/showthread.php?t=164276))
```
compare 0x8000 0x0
if 0x1 goto @option1
compare 0x8000 0x1
if 0x1 goto @option2
compare 0x8000 0x2
if 0x1 goto @option3
compare 0x8000 0x3
if 0x1 goto @option4
compare 0x8000 0x4
if 0x1 goto @option5
compare 0x8000 0x5
if 0x1 goto @option6
compare 0x8000 0x7F
if 0x1 goto @canceled
```

### compseqexplicit (value to compare) \[(value to compare against) (label name)...\]
###### Other Names: compseqe, compareseqexplicit, compsequenceexplicit, comparesequenceexplicit
Explicit form of compseq. Requires a (value to compare against) AND (label name...) for the compare/if loop rather than only (label name...).

Example:
```
compseqexplicit 0x8000 0x0 @option1 0x1 @option2 0x2 @option3 0x3 @option4 0x4 @option5 0x5 @option6 0x7F @canceled
```

### cry (pokemon)
Calls XSE cry (pokemon) 0x0.

### fadein
###### Other Names: fadeinb
Calls XSE fadescreen 0x0 (black to screen).

### fadeout
###### Other Names: fadeoutb
Calls XSE fadescreen 0x1 (screen to black).

### fadeinw
Calls XSE fadescreen 0x2 (white to screen).

### fadeoutw
Calls XSE fadescreen 0x3 (screen to white).

### giveitem (item name) (item quantity)
###### Other Names: item
Calls XSE giveitem. (item name) can be a hex ID, decimal ID, or string (such as "potion"). (item quantity) can be any kind of integer (hex or decimal).

### givepokemon (pokemon name) (pokemon level) (pokemon held item)
###### Other Names: pokemon
Calls XSE givepokemon. All 3 args can either be hex int IDs, decimal int IDs, or, for (pokemon name) and (pokemon held item) only, a string representing the name of the pokemon or held item.

### gymbattle 

### msgbox (string) (mode)
###### Other Names: msg
Calls XSE msgbox. 
```
msgbox Let's go to the mall! 0x4
```
(string) is a string literal (or constant), representing the text to display. (mode) is a hex integer or string (starting with "MSG_") representing the type of msgbox. Adding linebreaks in the message string is allowed, but the compiler already has a system for auto-filling these breaks. Keep in mind that an #org statement is not allowed here. See XSE msgbox documentation for more information on msgbox types. See setbreaklimit and pageonbreak in section 4 for more information on the automatic breaking system.

### pause (time)
Time can be a decimal int representing the milliseconds to pause, or raw hex data (according to Sierra's tutorial, a pause of 0x20 ~= 1 second in real time. This is also the metric used to convert milliseconds to raw hex data for when (time) is a decimal int).

### wildbattle (pokemon) (level) (item)
Calls XSE wildbattle. (pokemon) is conformed to a hex int pokemon ID (can be string representing the pokemon name, hex int, or decimal int). (level) is conformed to a hex int representing the level of the pokemon. (item) is conformed to a hex int item ID (can be string representing the item name, hex int, or decimal int).



## (5c) List of XSE Commands with Alternative Names

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

### preparemsg (pointer)
###### Other Names: prepmsg
Calls XSE preparemsg with specified (pointer), and adds a waitmsg call afterwards. To prevent the waitmsg call, see preparemsgnowait below.

### preparemsgnowait (poitner)
###### Other Names: prepmsgnowait
Calls XSE preparemsg with specified (pointer).

### release
###### Other Names: rel
Calls XSE release.

### setflag (flag)
###### Other Names: sf
Calls XSE setflag. (flag) is a hex int representing the flag ID.

### warp (map bank) (map number) (warp number)
##### Other Names: warpto
Calls XSE warp. (map bank) is the map bank, (map number) is the map number, and (warp number) is the warp number. All of these are decimal ints.



## (6) List of all Special % Strings

% strings have been mentioned throughout this reference, but for the sake of simplicity, here's a list of all of them (they are all case-insensitive):
```
;Any time "X" is used, it represents an argument number (starts at 1).

%argX  ;Function argument. Use only in func definitions.
%argXP  ;Function argument. Specifies that it's a pokemon name. Use only in func definitions.
%argXA  ;Function argument. Specifies that it's an in-battle move name. Use only in func definitions.
%argXI  ;Function argument. Specifies that it's an item name. Use only in func definitions.

%argXH  ;Function argument. Specifies that it's a hex int. Conforms decimal ints to hex ints. Use only in func definitions.

%li ;Short for %loopiter. No differences in behavior.
%loopiter  ;Current loop iteration. Use only in loops.
%loopiterH  ;Current loop iteration conformed to a hex int. Use only in loops.

%pl  ;Player name.
%ri  ;Rival name.
```



## (7) Info/legal

Thanks for reading about FSE. It's something I've been working hard on over the past few weeks. As for legal stuff, feel free to distribute this as long as it's done non-commercially and credit is given to me (ps4star) for the files which I created. This means everything except the file ace.js and the ace folder - I did not create the ACE editor and any modification, distribution, etc. of that editor is subject to ACE's license.

You can find the exact license within this repo as LICENSE.md.

















