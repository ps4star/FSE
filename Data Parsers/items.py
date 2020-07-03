data = """Master Ball 1
Ultra Ball 2
Great Ball 3
Poke Ball 4
Safari Ball 5
Net Ball 6
Dive Ball 7
Nest Ball 8
Repeat Ball 9
Timer Ball 10
Luxury Ball 11
Premier Ball 12
Potion 13
Antidote 14
Burn Heal 15
Ice Heal 16
Awakening 17
Parlyz Heal 18
Full Restore 19
Max Potion 20
Hyper Potion 21
Super Potion 22
Full Heal 23
Revive 24
Max Revive 25
Fresh Water 26
Soda Pop 27
Lemonade 28
Moomoo Milk 29
Energypowder 30
Energy Root 31
Heal Powder 32
Revival Herb 33
Ether 34
Max Ether 35
Elixir 36
Max Elixir 37
Lava Cookie 38
Blue Flute 39
Yellow Flute 40
Red Flute 41
Black Flute 42
White Flute 43
Berry Juice 44
Sacred Ash 45
Shoal Salt 46
Shoal Shell 47
Red Shard 48
Blue Shard 49
Yellow Shard 50
Green Shard 51
HP Up 63
Protein 64
Iron 65
Carbos 66
Calcium 67
Rare Candy 68
PP Up 69
Zinc 70
PP Max 71
Guard Spec. 73
Dire Hit 74
X Attack 75
X Defend 76
X Speed 77
X Accuracy 78
X Special 79
Poke Doll 80
Fluffy Tail 81
Super Repel 83
Max Repel 84
Escape Rope 85
Repel 86
Sun Stone 93
Moon Stone 94
Fire Stone 95
Thunderstone 96
Water Stone 97
Leaf Stone 98
Tinymushroom 103
Big Mushroom 104
Pearl 106
Big Pearl 107
Stardust 108
Star Piece 109
Nugget 110
Heart Scale 111
Orange Mail 121
Harbor Mail 122
Glitter Mail 123
Mech Mail 124
Wood Mail 125
Wave Mail 126
Bead Mail 127
Shadow Mail 128
Tropic Mail 129
Dream Mail 130
Fab Mail 131
Retro Mail 132
Cheri Berry 133
Chesto Berry 134
Pecha Berry 135
Rawst Berry 136
Aspear Berry 137
Leppa Berry 138
Oran Berry 139
Persim Berry 140
Lum Berry 141
Sitrus Berry 142
Figy Berry 143
Wiki Berry 144
Mago Berry 145
Aguav Berry 146
Iapapa Berry 147
Razz Berry 148
Bluk Berry 149
Nanab Berry 150
Wepear Berry 151
Pinap Berry 152
Pomeg Berry 153
Kelpsy Berry 154
Qualot Berry 155
Hondew Berry 156
Grepa Berry 157
Tamato Berry 158
Cornn Berry 159
Magost Berry 160
Rabuta Berry 161
Nomel Berry 162
Spelon Berry 163
Pamtre Berry 164
Watmel Berry 165
Durin Berry 166
Belue Berry 167
Liechi Berry 168
Ganlon Berry 169
Salac Berry 170
Petaya Berry 171
Apicot Berry 172
Lansat Berry 173
Starf Berry 174
Enigma Berry 175
Brightpowder 179
White Herb 180
Macho Brace 181
Exp. Share 182
Quick Claw 183
Soothe Bell 184
Mental Herb 185
Choice Band 186
King's Rock 187
Silverpowder 188
Amulet Coin 189
Cleanse Tag 190
Soul Dew 191
Deepseatooth 192
Deepseascale 193
Smoke Ball 194
Everstone 195
Focus Band 196
Lucky Egg 197
Scope Lens 198
Metal Coat 199
Leftovers 200
Dragon Scale 201
Light Ball 202
Soft Sand 203
Hard Stone 204
Miracle Seed 205
Blackglasses 206
Black Belt 207
Magnet 208
Mystic Water 209
Sharp Beak 210
Poison Barb 211
Nevermeltice 212
Spell Tag 213
Twistedspoon 214
Charcoal 215
Dragon Fang 216
Silk Scarf 217
Up-grade 218
Shell Bell 219
Sea Incense 220
Lax Incense 221
Lucky Punch 222
Metal Powder 223
Thick Club 224
Stick 225
Red Scarf 254
Blue Scarf 255
Pink Scarf 256
Green Scarf 257
Yellow Scarf 258
Mach Bike 259
Coin Case 260
Itemfinder 261
Old Rod 262
Good Rod 263
Super Rod 264
S.S. Ticket 265
Contest Pass 266
Wailmer Pail 268
Devon Goods 269
Soot Sack 270
Basement Key 271
Acro Bike 272
PokeBlock Case 273
Letter 274
Eon Ticket 275
Red Orb 276
Blue Orb 277
Scanner 278
Go-goggles 279
Meteorite 280
Rm. 1 Key 281
Rm. 2 Key 282
Rm. 4 Key 283
Rm. 6 Key 284
Storage Key 285
Root Fossil 286
Claw Fossil 287
Devon Scope 288
TM01 289
TM02 290
TM03 291
TM04 292
TM05 293
TM06 294
TM07 295
TM08 296
TM09 297
TM10 298
TM11 299
TM12 300
TM13 301
TM14 302
TM15 303
TM16 304
TM17 305
TM18 306
TM19 307
TM20 308
TM21 309
TM22 310
TM23 311
TM24 312
TM25 313
TM26 314
TM27 315
TM28 316
TM29 317
TM30 318
TM31 319
TM32 320
TM33 321
TM34 322
TM35 323
TM36 324
TM37 325
TM38 326
TM39 327
TM40 328
TM41 329
TM42 330
TM43 331
TM44 332
TM45 333
TM46 334
TM47 335
TM48 336
TM49 337
TM50 338
HM01 339
HM02 340
HM03 341
HM04 342
HM05 343
HM06 344
HM07 345
HM08 346
Oak's Parcel 349
Poke Flute 350
Secret Key 351
Bike Voucher 352
Gold Teeth 353
Old Amber 354
Card Key 355
Lift Key 356
Helix Fossil 357
Dome Fossil 358
Silph Scope 359
Bicycle 360
Town Map 361
VS Seeker 362
Fame Checker 363
TM Case 364
Berry Pouch 365
Teachy TV 366
Tri-pass 367
Rainbow Pass 368
Tea 369
Mysticticket 370
Auroraticket 371
Powder Jar 372
Ruby 373
Sapphire 374"""

lines = data.split("\n")
for a in range(0, len(lines)):
    sdelim = lines[a].split(" ")
    endID = sdelim.pop()
    sdelim = "".join(sdelim)
    sdelim += " " + str(endID)
    lines[a] = sdelim

output = ""
output += "{\n\t"
for a in range(0, len(lines)):
    arg = lines[a].split(" ")
    output += '"'+arg[0].lower()+'" : "'+arg[1]+'",\n\t'
output += "\n}"

file1 = open("itemstable.json", "w+")
file1.write(output)
file1.close()