###########################################################################################
# STAT HUD
# HUD that shows player/enemy ship stats
###########################################################################################

screen playerstats:
    add "mod_assets/gui/playerstats.png"
    text "[hp]/[maxhp]" xpos 58 ypos 65
    text "[ammo]" xpos 58 ypos 100
    text "[shields]/[maxshields]" xpos 204 ypos 65
    text "[dodge]" xpos 204 ypos 100
    text "[shipname]" xpos 15 ypos 12
    text "[shipclass]" xpos 15 ypos 34