###########################################################################################
# DEMO END
# The end of the demo which results in guaranteed destruction of the player's ship
###########################################################################################  
    
label modend:
    "We come across a ludicrously overpowered ship."
    call impossible
    
    show monika 1g zorder 2 at t11
    m "[player]..."
    m "I'm not sure how you won that but..."
    m "The fog is setting in!"
    mc "HE WAS MADE TO RULE THE WAVES ACROSS THE SEVEN SEAS!"
    call endgame
    $ renpy.full_restart()
    
label modendgameover:
    $ quick_menu = False
    stop music
    play music t10
    
    show layer master:
        dizzy(1, 1.0)
    show vignette zorder 3 with dissolve:
        alpha 0.5
    $ pause(0.5)
    play sound fire loop
    "The killing shot tears through our hull as if it were made of tissue paper."
    "Everything appears to go into slow motion as the ship erupts into fire and explosions."
    "As flames consume the ship, systems go out, and oxygen is vented into the darkest of space..."
    
    show kestrel zorder 2 at thide
    hide kestrel
    show monika 1g zorder 2 at t11
    "...I take a look to my right and see Monika."
    m "...I guess this is it then."
    mc "Yep."
    m "Looks like the 'fog' is setting in now..."
    mc "I will see you in the next life."
    m "Dude, you totally just stole that line from Exit Music, didn't you?"
    mc "Uhhh, maybe. Heh."
    mc "Well, I'll see you again when I start a new game anyways."
    m 1a "Oh shit, you right."
    
    play sound explosion1
    scene black
    $ pause(1)
    if shipname == "Bismarck" or shipname == "KMS Bismarck":
        "{i}At the bottom of the ocean, the depths of the abyss, they are bound by iron and blood.{/i}"
        "{i}The flagship of the navy, the terror of the seas, his guns have gone silent at last...{/i}"
    else:
        "One last explosion marks your fate as your ship is torn apart."
    show monika 1a zorder 2 at t11
    m "It was an honor serving with you, Captain [player]."
    call endgame
    $ renpy.full_restart()