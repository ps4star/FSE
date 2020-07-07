var allScripts = {
	
	"stdlib": {
	
		"obtain_poke" :

`fanfare 0x13E
msgbox You received a %ARG1! 0x4`,

		"name_poke" :
		
`msg Would you like to give a nickname to %ARG1? 0x5
compare 0x800D 0x1
if 0x1 call %ARG2`,

		"obtain_and_name" :
		
`fcall stdlib.obtain_poke %ARG1
fcall stdlib.name_poke %ARG1 %ARG2`,

		"nickname" :
		
`countpokemon
subvar 0x800D 0x1
copyvar 0x8004 0x800D
fadescreen 0x1
special 0x166
waitstate`,

		"set_seen":
		
`setvar 0x8004 %ARG1P
special 0x163`

	}

}



