###########################################################################################
# BATTLE EXAMPLE (HOSTILE)
# An example battle where the player can actually be killed.
###########################################################################################

# Start the battle!
label examplehostilebattle:
    $ battle = "examplehostilebattle" # Name of battle label

    # Enemy ship stats
    $ enemy = "RB-P105" # Enemy ship name
    $ enemyclass = "Type 10 patrol ship" # Enemy ship class
    $ enemydesc = "The enemy is a Rebel patrol ship, armed with a single laser cannon." # Enemy ship description
    $ enemymaxhp = 10 # Enemy max HP
    $ enemyhp = 10 # Enemy HP, should be same as max HP
    $ reward = 25 # How much credits should be given upon enemy defeat
    
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

    if shipname == "Bismarck" or shipname == "KMS Bismarck":
        "{i}Into formation, the hunt has begun.{/i}"
        "{i}Death and damnation, the fleet is coming...{/i}"
    else:
        "The signature of a lightly armed Rebel patrol ship appears on the ship radar."
        "It charges up its weapons with hostile intent."
    "Rebel Ship" "\"Did you think you could get away from us? You are only delaying the inevitable!\""
    m "We'll see about that."
    call screen dialog("Unlike the first encounter, this battle involves a\nhostile and lethal threat.", ok_action=Return())
    call screen dialog("Every hit will deplete your shields before your hull is damaged.\nAdditionally, there is a chance that you will dodge a hit.", ok_action=Return())
    call screen dialog("If the hull is critically damaged, your ship explodes\nand the Dokis die.", ok_action=Return())
    
    call expression battle + "2" # Battle
    
    ########
    
    play sound shipexplode # Victory
    hide screen enemystats
    $ pause(1.6)
    
    # Swap back to explore mode
    $ currentmode = "explore"
    $ currentpos = get_pos()
    stop music
    play music "<from " + str(currentpos) + " loop 0>mod_assets/music/bp_FTL_03_CivilEXPLORE.mp3"
    
    "The enemy ship explodes into a useful assortment of scrap (+[reward] CR)."
    $ credits += reward
    $ shields = maxshields # Recharge player's shields
    $ shieldsdown = False
    $ stealth = False
    if shipname == "Bismarck" or shipname == "KMS Bismarck":
        "{i}He was made to rule the waves across the seven seas!{/i}"
    else:
        "I prepare to leave the area before any more reinforcements arrive."
    return
    
# Battle in progress
label examplehostilebattle2:
    show screen enemystats

    # Player's Turn
    call playerturn
    $ ehealth() # Check if enemy dies
    
    # Enemy's Turn
    "The Rebel ship fires a laser shot."
    call enemyhlaser1

    if shields == 0 and shieldsdown == False:
        $ shieldsdown = True
        s "[player], our shields are down!"
    jump expression battle + "2" # Battle