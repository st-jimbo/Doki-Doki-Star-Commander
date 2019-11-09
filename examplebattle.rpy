###########################################################################################
# BATTLE EXAMPLE
# An example battle.
###########################################################################################

# Start the battle!
label examplebattle:
    $ battle = "examplebattle" # Name of battle label

    # Enemy ship stats
    $ enemy = "Unarmed drone" # Enemy ship name
    $ enemydesc = "It's a completely deactivated drone with no way of defending itself." # Enemy ship description
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
    "Monika flies the ship towards a deactivated drone ship."
    "It seems like it would make the perfect practice target."
    m "Captain [player], it's important that you know how to lead your crew during a combat situation."
    m "Let's practice on this deactivated drone ship!"
    call screen dialog("Ship-to-ship combat is turn based, once\n you make a move, the enemy does too.", ok_action=Return())
    call screen dialog("Before each turn, you are able to select which\nweapon you will use for the attack. The status of\nboth you and the enemy's ship will also be visible.", ok_action=Return())
    
    call expression battle + "2" # Battle
    
    ########
    
    play sound shipexplode # Victory
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
    m "Great work team! Now we know how battle mechanics play out, at least with completely harmless drone ships."
    return
    
# Battle in progress
label examplebattle2:
    # Player's Turn
    call playerturn
    $ ehealth() # Check if enemy dies
    
    # Enemy's Turn
    "The drone is unable to do anything."

    if shields == 0 and shieldsdown == False:
        $ shieldsdown = True
        s "[player], our shields are down!"
    jump expression battle + "2" # Battle # Rename this