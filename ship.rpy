###########################################################################################
# SHIP OVERVIEW
# A ship overview where the player can select an action.
###########################################################################################

# Initialize ship background
label ship:
    # Setup background
    $ dynbg()
    with wipeleft
    jump shipmenu
    
# Ship menu
label shipmenu:
    show pship 1 zorder 2 at sh11
    menu:
        "[shipname] ([shipclass.name])\nHull: [hp]/[maxhp]\nBalance: [credits] CR{fast}"
        
        "Speak With Crew":
            jump hub
            
        "Ship Stats":
            jump shipstats
            
        "Go":
            return
            
# Ship stats and equipment
label shipstats:
    menu:
        "[maxshields] shield hitpoints\n[dodge]\% dodge chance\n[ammo] ammo{fast}"
        
        "Weapons":
            menu viewweapons:
                "Select a weapon to view its stats.{fast}"
                "[shipprimary.name]\n(Primary)":
                    "[shipprimary.desc]"
                    jump viewweapons
                "[shipsecondary.name]\n(Secondary)":
                    "[shipsecondary.desc]"
                    jump viewweapons
                "[shipaugment.name]\n(Augment)":
                    "[shipaugment.desc]"
                    jump viewweapons
                "Back":
                    jump shipstats
            
        "Equipment":
            menu viewequipment:
                "Select a module to view its stats.{fast}"
                "[shieldgen.name]\n(Shield Generator)":
                    "[shieldgen.desc]"
                    jump viewequipment
                "[engine.name]\n(Ship Engines)":
                    "[engine.desc]"
                    jump viewequipment
                "Back":
                    jump shipstats
            jump shipstats
            
        "Power Distributor":
            if shieldpower == True:
                "Shields: MAX\nWeapons: Normal\nEngines: Normal{fast}"
            elif weaponpower == True:
                "Shields: Normal\nWeapons: MAX\nEngines: Normal{fast}"
            elif enginepower == True:
                "Shields: Normal\nWeapons: Normal\nEngines: MAX{fast}"
            else:
                "Shields: Normal\nWeapons: Normal\nEngines: Normal{fast}"
            "While shields are at MAX power: +[shieldgen.bonus] SP\nWhile weapons are at MAX power: +[wpbonus] Primary DMG\nWhile engines are at MAX power: +[engine.bonus]\% dodge{fast}"
            jump shipstats
        
        "Back":
            jump shipmenu