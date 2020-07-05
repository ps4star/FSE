var allScripts = {
	"obtain-poke" :
`fanfare 0x13E
msgbox You received a %ARG_1! 0x4`,
	"name-poke" :
`msg Would you like to give a\\nnickname to %ARG_1? 0x5
compare 0x800D 0x1
if 0x1 call %ARG_2`,
	"obtain-name" :
`fcall obtain-poke %ARG_1
fcall name-poke %ARG_1 %ARG_2`,
	"nickname" :
`countpokemon
subvar 0x800D 0x1
copyvar 0x8004 0x800D
fadescreen 0x1
special 0x166
waitstate`



}