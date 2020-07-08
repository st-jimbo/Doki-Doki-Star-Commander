###########################################################################################
# ENEMY ATTACKS
# This script defines enemy attacks.
###########################################################################################

# Tier 1 Heavy Laser (1 DMG)
label enemyhlaser1:
    play sound hlaser
    $ roll = renpy.random.randint(1, 100) # Roll if the player dodges or not
    $ pause(1)
    
    if roll <= dodge:
        play sound miss
        "The enemy misses!"
        return
    else:
        if shields > 0:
            play sound renpy.random.choice(rshield)
        else:
            show layer master: # Shake effect
                truecenter
                parallel:
                    zoom 1.025
                    easeout 0.35 zoom 1.0
                parallel:
                    xpos 620
                    easein_elastic 0.35 xpos 640
            play sound renpy.random.choice(rhull)
        $ damage(1)
        "Our ship takes a hit (1 DMG)."
        return
        
# Impossible Plasma (8 DMG)
label iplasma:
    play sound hlaser
    $ roll = renpy.random.randint(1, 100) # Roll if the player dodges or not
    $ pause(1)
    
    if roll <= dodge:
        play sound miss
        "The enemy misses!"
        return
    else:
        if shields > 0:
            play sound renpy.random.choice(rshield)
        else:
            show layer master: # Shake effect
                truecenter
                parallel:
                    zoom 1.025
                    easeout 0.35 zoom 1.0
                parallel:
                    xpos 620
                    easein_elastic 0.35 xpos 640
            play sound renpy.random.choice(rhull)
        $ specialdamage(8)
        "Our ship takes a crippling hit (8 DMG)."
        return