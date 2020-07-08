###########################################################################################
# OVERPOWERED BATTLE
# A battle designed to be impossible to win.
###########################################################################################

# Start the battle!
label impossible:
    $ battle = "impossible" # Name of battle label

    # Enemy ship stats
    $ enemy = "USS Indestructible" # Enemy ship name
    $ enemydesc = "I don't know what that is, other than the fact that it's impossible to destroy." # Enemy ship description
    $ enemymaxhp = 50 # Enemy max HP
    $ enemyhp = 50 # Enemy HP, should be same as max HP
    $ reward = 999 # How much credits should be given upon enemy defeat
    
    # Player
    $ shieldsdown = False # True if player's shields have gone down
    $ usedaugment = False # True if player has used augment in this battle
    
    # Swap to battle mode on music
    $ currentmode = "battle"
    $ currentpos = get_pos()
    stop music
    play music "<from " + str(currentpos) + " loop 0>mod_assets/music/bp_FTL_16_CivilBATTLE.mp3"

    # Setup background
    $ dynbg()
    with dissolve_scene_full
    
    show pship 1 zorder 2 at sh11
    stop music fadeout 2.0
    "I slowly see the hull of a massive ship come into view."
    "Without a second thought, I already know who it is."
    mc "I know who that is."
    m "You do? Who is it?"
    mc "It's the {i}Indestructible{/i}"
    play music td
    m "The {i}what!?{/i}"
    "Indestructible" "\"Unfortunately, as this is the end of the mod, you must be terminated.\""
    "Indestructible" "\"The simulation will restart upon ship destruction.\""
    m "Well, it was nice knowing you [player]."
    m "It'd be around this time that 'Brick by Brick' from the Doki Doki Purist mod would be playing..."
    m "...but instead of everything being consumed in fog, we are being consumed by fire!"
    m "So, uh, here's 'Your Reality.'"
    m "Ehehe~"
    stop music
    play music "bgm/credits.ogg"
    
    call expression battle + "2" # Battle
    
    ########
    
    play sound shipexplode # Victory
    $ pause(1.6)
    
    # Swap back to explore mode
    $ currentmode = "explore"
    $ currentpos = get_pos()
    stop music
    play music "<from " + str(currentpos) + " loop 0>mod_assets/music/bp_FTL_03_CivilEXPLORE.mp3"
    
    "The {i}Indestructible{/i} erupts in a massive explosion (+[reward] CR)."
    $ credits += reward
    $ shields = maxshields # Recharge player's shields
    $ shieldsdown = False
    $ stealth = False
    "How did you even destroy it? It's supposed to be indestructible, like the name would suggest!"
    "Oh well, you probably cheated or something, but here's your reward. There seriously isn't anything else after this though."
    return
    
# Battle in progress
label impossible2:
    # Player's Turn
    call playerturn
    $ ehealth() # Check if enemy dies
    
    # Enemy's Turn
    "The {i}Indestructible{/i} fires a massive plasma bolt."
    call iplasma

    if shields == 0 and shieldsdown == False:
        $ shieldsdown = True
        s "[player], our shields are down!"
    jump expression battle + "2" # Battle