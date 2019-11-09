###########################################################################################
# GAMEOVER
# This chapter plays when ship health drops to 0.
###########################################################################################

label gameover:
    # previous music fadeout
    window hide(None)
    $ quick_menu = False
    stop music
    play sound shipexplode
    
    show vignette zorder 3 with dissolve:
        alpha 0.5
    
    show layer master: # Explosion effect
        truecenter
        parallel:
            zoom 1.025
            easeout 0.375 zoom 1.0
            zoom 1.025
            easeout 0.387 zoom 1.0
            zoom 1.05
            easeout 0.272 zoom 1.0
            zoom 1.05
            easeout 0.4 zoom 1.0
            zoom 1.075
            easeout 0.4 zoom 1.0
            
    $ pause(1.6)
    play music mend
    scene black
    $ pause(1)
    if shipname == "Bismarck" or shipname == "KMS Bismarck":
        "{i}At the bottom of the ocean, the depths of the abyss, they are bound by iron and blood.{/i}"
        "{i}The flagship of the navy, the terror of the seas, his guns have gone silent at last...{/i}"
    else:
        "One last explosion marks your fate as your ship is torn apart."
    show monika 1a zorder 2 at t11
    m "Better luck next time, [player]."
    call endgame
    $ renpy.full_restart()