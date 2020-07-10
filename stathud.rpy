###########################################################################################
# STAT HUD
# HUD that shows player/enemy ship stats
###########################################################################################

screen playerstats:
    add "mod_assets/gui/playerstats.png"
    text "[hp]/[maxhp]" xpos 58 ypos 65
    text "[ammo]" xpos 58 ypos 100
    text "[shields]/[maxshields]" xpos 204 ypos 65
    text "[dodge]%" xpos 204 ypos 100
    text "[credits] CR" xpos 27 ypos 143
    text "[shipname]" xpos 15 ypos 10
    text "[shipclass.name]" xpos 15 ypos 36  size 18

screen enemystats:
    add "mod_assets/gui/enemystats.png" xpos 1007
    text "[enemyhp]/[enemymaxhp]" xpos 1270 ypos 56 xalign 1.0
    text "[enemy]" xpos 1270 ypos 7 xalign 1.0
    text "[enemyclass]" xpos 1270 ypos 32  size 16 xalign 1.0