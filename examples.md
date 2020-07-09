# Example Scripts

Big database of FSE example scripts, all of these have compiler output as well. A great resource for getting into the language at first. The full documentation can be found within this repo as re.md.

### A simple msgbox
```
msg Hello World! 0x4
```
XSE:
```
#dynamic 0x800000

#org @main

msgbox @offset0 0x4

end

#org @offset0
= Hello World!
```

### Move and mover (reverse move)
```
const @birch 0x00 ;obviously this is just a hypothetical, birch isn't always ID 0x00
const @birchMove1 u u r r u u

setspeed normal

move @birch @birchMove1 ;moves birch at normal speed

setspeed fast

;mover just takes the movement sequence and converts it to the opposite directions
;so left becomes right, up becomes down, etc.
;this means you can just apply the same move sequence in reverse rather than defining a second one.

mover @birch @birchMove1 ;moves birch back where he started at a faster speed
```
XSE:
```
#dynamic 0x800000

#org @main

applymovement 0x00 @offset0
waitmovement 0x0
applymovement 0x00 @offset1
waitmovement 0x0

end

#org @offset0
#raw 0x09
#raw 0x09
#raw 0x0B
#raw 0x0B
#raw 0x09
#raw 0x09
#raw 0xFE

#org @offset1
#raw 0x15
#raw 0x15
#raw 0x17
#raw 0x17
#raw 0x15
#raw 0x15
#raw 0xFE
```

### movenowait
```
const @myMoveSeq up up left left left left

setspeed fast
movenowait 0x00 @myMoveSeq
mover 0x00 @myMoveSeq
```

### @main and label structure
```
using namespace stdlib

lf
; some @main code...
rel

; As soon as you define a label, @main ends. There is no need to put an end statement for this yourself.
; This means that the second you define a label, all instructions after that point must be inside
; of labels that you've defined yourself.

@name
;handle nickname
ret

;If I were to put a command like "msgbox" here for example, the compiler would still
;run successfully, but XSE would throw errors if you tried to compile it to the ROM.
```
No XSE output as there is little or no code to execute here.

### lock and faceplayer
```
lf ;calls both lock and faceplayer in a single command! (that's a lowercase L btw, not an i)
lock ;the classic commands still exist if you prefer
face ;short for faceplayer
rel ; short for release
faceplayer ;original XSE command
release ;original XSE command
```
No XSE output as there is little or no code to execute here.

### stdlib
```
using namespace stdlib

lf

givepokemon Charmander 10 oran_berry
fcall obtain_and_name Charmander @name ;asks user to name pokemon, if yes, calls @name

rel

@name ; you can also do "lbl name" or "label name" or "@ name", it's up to you
;there is currently no stdlib func for nicknaming in RSE. Use "fcall stdlib.nickname_frlg" for FRLG
ret ;since "fcall obtain_and_name" CALLS @name rather than jumps to it, a return is required instead of end
```
XSE:
```
#dynamic 0x800000

#org @main

lock
faceplayer
givepokemon 0x4 0xA 0x8B 0x0 0x0 0x0
fanfare 0x13E
msgbox @offset0 0x4
waitfanfare
closeonkeypress
msgbox @offset1 0x5
compare 0x800D 0x1
if 0x1 call @name
release

end

#org @name


return


#org @offset0
= You received a Charmander!

#org @offset1
= Would you like to give a nickname\nto Charmander?
```

### What "using namespace stdlib" does
```
fcall stdlib.obtain_and_name Charmander @name ;VALID
fcall obtain_and_name Charmander @name ;ERROR, no such function "obtain_and_name"

using namespace stdlib

fcall stdlib.obtain_and_name Charmander @name ;VALID
fcall obtain_and_name Charmander @name ;VALID
```
No XSE output as there is little or no code to execute.

### compare and if
```
compare LASTRESULT 0x0

if = call @equals
if > call @gt
if < call @lt

@equals
ret

@gt
ret

@lt
ret
```
XSE:
```
#dynamic 0x800000

#org @main

compare LASTRESULT 0x0
if 0x1 call @equals
if 0x2 call @gt
if 0x0 call @lt

end

#org @equals


return


#org @gt


return


#org @lt


return
```

### FSE constants and functions
```
const @myName Ebony Dark'ness Dementia Raven Way

$funcstart display_my_name
msgbox hi my name is %arg1 and I have long ebony black hair... 0x4
$funcend

fcall display_my_name @myName
```
XSE:
```
#dynamic 0x800000

#org @main

msgbox @offset0 0x4

end

#org @offset0
= hi my name is Ebony Dark'ness Dementia\nRaven Way and I have long ebony\lblack hair...
```

### Another Function Script (that's actually useful this time)
```
$funcstart set_seen
setvar 0x8004 %arg1P
special 0x163
$funcend

&comstart
Ok so I feel there is a lot of stuff I need to explain here (this is a multi-line comment btw).
So first of all, %arg1 just passes the first argument to the function in that position.
So if we had a function that takes 1 argument and simply writes it into a msgbox, we would do
msgbox %arg1 0x4
Simple, right?

Now let's say we want %arg1 to be converted to a hex pokemon ID. We need to use %arg1P. This takes strings like "mew" and converts them to their hex IDs. Using their actual hex IDs, or decimal IDs, is also allowed, as opposed to just the string names. %arg1I does this for items, %arg1A for attacks, %arg1H for decimal to hex conversion, you get the picture. So when the compiler is evaluating the below fcall, what it's actually doing is "setvar 0x8004 0x97" because mew's ID is 0x97, and we specified that we want argument 1 to be passed in at that point, and specified that it's a pokemon's name and not just any random string of letters.
&comend

fcall set_seen mew ;sets mew to seen in the pokedex
```
XSE:
```
#dynamic 0x800000

#org @main


setvar 0x8004 0x97
special 0x163

end
```

### loops
```
lstart 5
msg Msg Number: %loopiter 0x4 ;Msg Number: 0, Msg Number: 1, etc... Also, you can use %li instead of %loopiter if you don't want to type the whole thing out :).
lend
```
XSE:
```
#dynamic 0x800000

#org @main

msgbox @offset0 0x4
msgbox @offset1 0x4
msgbox @offset2 0x4
msgbox @offset3 0x4
msgbox @offset4 0x4

end

#org @offset0
= Msg Number: 0

#org @offset1
= Msg Number: 1

#org @offset2
= Msg Number: 2

#org @offset3
= Msg Number: 3

#org @offset4
= Msg Number: 4
```

### Looping with getln of constant
```
const @myList bulbasaur charmander squirtle

loop getln@myList ;loops through the list
msg indexat%loopiter@myList 0x4 ;displays all elements of list
lend
```
XSE:
```
#dynamic 0x800000

#org @main

msgbox @offset0 0x4
msgbox @offset1 0x4
msgbox @offset2 0x4

end

#org @offset0
= bulbasaur

#org @offset1
= charmander

#org @offset2
= squirtle
```

### compseq
```
compseq 0x8000 0x0 @option1 @option2 @option3 @option4 @option5 @option6 @canceled

@option1
;option 1 code
ret

@option2
;option 2 code
ret

@option3
;option 3 code
ret

@option4
;option 4 code
ret

@option5
;option 5 code
ret

@option6
;option 6 code
ret

@canceled
;code to run when user presses cancel on the menu
ret
```
XSE:
```
#dynamic 0x800000

#org @main

compare 0x8000 0x0
if 0x1 goto 0x0
compare 0x8000 0x1
if 0x1 goto @option1
compare 0x8000 0x2
if 0x1 goto @option2
compare 0x8000 0x3
if 0x1 goto @option3
compare 0x8000 0x4
if 0x1 goto @option4
compare 0x8000 0x5
if 0x1 goto @option5
compare 0x8000 0x6
if 0x1 goto @option6
compare 0x8000 0x7
if 0x7F goto @canceled

end

#org @option1


return


#org @option2


return


#org @option3


return


#org @option4


return


#org @option5


return


#org @option6


return


#org @canceled


return
```

### Expansion Statement with compseq
```
compseq 0x8000 0x0 @option1 @option2 @option3 @option4 @option5 @option6 @canceled

expstart 6 1 ;inits %loopiter at 1, loops 6 times
@option%loopiter ;adds %loopiter to end of option name (1, 2, 3...)

ret
expend

;the result produced from the above exp statement is the same as writing out all the @option labels
;so instead of writing out @option1, @option2 etc, just use exp statements like the one above.

@canceled
;code to run when user presses cancel on the menu
ret
```
XSE:
```
#dynamic 0x800000

#org @main

compare 0x8000 0x0
if 0x1 goto 0x0
compare 0x8000 0x1
if 0x1 goto @option1
compare 0x8000 0x2
if 0x1 goto @option2
compare 0x8000 0x3
if 0x1 goto @option3
compare 0x8000 0x4
if 0x1 goto @option4
compare 0x8000 0x5
if 0x1 goto @option5
compare 0x8000 0x6
if 0x1 goto @option6
compare 0x8000 0x7
if 0x7F goto @canceled

end

#org @option1


return


#org @option2


return


#org @option3


return


#org @option4


return


#org @option5


return


#org @option6


return


#org @canceled


return
```




















