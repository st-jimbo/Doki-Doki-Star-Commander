###########################################################################################
# WEAPONS
# This scrip defines attacks using the ship's weapons
# It also defines the available weapons and their stats.
###########################################################################################

# Enemy health mechanic. Should be called every time the enemy takes damage.
init python:
    def ehealth():
        if enemyhp <= 0:
            renpy.return_statement() # Jump to Victory sequence
# Weapon Class
    class Weapon:
        def __init__(self, name, price, type, label): # Constructor
            self.name = name # Item name
            self.desc = "Unknown item." # Item Description
            self.price = price # Price in CR
            self.type = type # Type of weapon (1 = Primary, 2 = Secondary, 3 = Augment)
            self.label = label # Label to jump to
            
        def equip(self): # Equip
            global shipprimary, shipsecondary, shipaugment
            if self.type == 1:
                shipprimary = self
            elif self.type == 2:
                shipsecondary = self
            elif self.type == 3:
                shipaugment = self
            
        def buy(self): # Purchase and equip
            global credits, shipprimary, shipsecondary, shipaugment
            credits -= self.price
            if self.type == 1:
                shipprimary = self
            elif self.type == 2:
                shipsecondary = self
            elif self.type == 3:
                shipaugment = self
            
# Player attack. Defines the actions the player can take for their turn.
label playerturn:
    menu:
        "[shipname]: [hp]/[maxhp] | [shields]/[maxshields] | [dodge]\% dodge | [ammo] ammo\n[enemy]: [enemyhp]/[enemymaxhp]\n{fast}"
        
        "Fire Primary\n([shipprimary.name])":
            call expression shipprimary.label
            if stealth == True: # If stealth is true...
                $ stealth = False # Turn off stealth
                "Our stealth field buys us enough time to attack again."
                jump playerturn # Allow another turn
            else:
                return
                
        "Fire Secondary\n([shipsecondary.name])":
            if ammo <= 0: # If ammo is empty...
                n "The weapon is out, captain!"
                jump playerturn # Redo turn
            else:
                $ ammo -= 1
                call expression shipsecondary.label
                if stealth == True: # If stealth is true...
                    $ stealth = False # Turn off stealth
                    "Our stealth field buys us enough time to attack again."
                    jump playerturn # Allow another turn
                else:
                    return
            
        "Use Augment\n([shipaugment.name])" if usedaugment == False:
            $ usedaugment = True
            call expression shipaugment.label
            jump playerturn
                
        "Examine Enemy Ship":
            mc "What are we fighting?"
            m "[enemydesc]"
            jump playerturn
            
# PRIMARY WEAPONS #

# Halberd Beam (halberd)
# Damage: 1-3
init python:
    pr_halberd = Weapon("Halberd Beam", 50, 1, "halberd")
    pr_halberd.desc = "A standard beam laser found on most cruisers.\n1-3 DMG"
label halberd:
    n "Opening fire!"
    play sound hbeam
    $ pause(1)
            
    $ rdmg = renpy.random.randint(1, 3)
    $ dmg = rdmg + bonusdmg
    $ enemyhp -= dmg
    $ pause(0.5)
    $ ehealth()
    
    if bonusdmg > 0:
        "The enemy ship takes a hit ([rdmg] + [bonusdmg] DMG)."
    else:
        "The enemy ship takes a hit ([dmg] DMG)."
    return
    
# Reliant-A Burster (burst1)
# Damage: 2-3
init python:
    pr_burst1 = Weapon("Reliant-A Burster", 60, 1, "burst1")
    pr_burst1.desc = "A common twin burst laser repeater.\n2-3 DMG"
label burst1:
    n "Opening fire!"
    play sound laser1
    $ pause(0.25)
    play sound laser1
    $ pause(0.75)
    play sound hull1
    $ pause(0.25)
    play sound hull1
    
    $ rdmg = renpy.random.randint(2, 3)
    $ dmg = rdmg + bonusdmg
    $ enemyhp -= dmg
    $ pause(0.5)
    $ ehealth()
    
    if bonusdmg > 0:
        "The enemy ship takes a hit ([rdmg] + [bonusdmg] DMG)."
    else:
        "The enemy ship takes a hit ([dmg] DMG)."
    return
    
# AC-2 Laser Cannon (lcannon1)
# Damage: 2
init python:
    pr_lcannon1 = Weapon("AC-2 Laser Cannon", 40, 1, "lcannon1")
    pr_lcannon1.desc = "Standard-issue laser cannon found on Federation destroyers.\n2 DMG"
label lcannon1:
    n "Opening fire!"
    play sound hlaser
    $ pause(1)
    play sound renpy.random.choice(rhull)    
    
    $ rdmg = renpy.random.randint(2, 2)
    $ dmg = rdmg + bonusdmg
    $ enemyhp -= dmg
    $ pause(0.5)
    $ ehealth()
    
    if bonusdmg > 0:
        "The enemy ship takes a hit ([rdmg] + [bonusdmg] DMG)."
    else:
        "The enemy ship takes a hit ([dmg] DMG)."
    return
    
# SECONDARY WEAPONS #

# Artemis Missiles (artemis)
# Damage: 2-4
init python:
    se_artemis = Weapon("Artemis Missiles", 60, 2, "artemis")
    se_artemis.desc = "Standard-issue high-explosive missiles.\n2-4 DMG"
label artemis:
    n "Opening fire!"

    show layer master: # Shake effect
        truecenter
        parallel:
            zoom 1.025
            easeout 0.20 zoom 1.0
        parallel:
            xpos 630
            easein_elastic 0.20 xpos 640
    play sound missile
    $ pause(1.25)
    play sound explosion1
        
    $ dmg = renpy.random.randint(2, 4)
    $ enemyhp -= dmg
    $ pause(0.5)
    $ ehealth()

    "The enemy ship takes a hit ([dmg] DMG)."
    return
    
# QF 4-inch Cannon (hcannon1)
# Damage: 4-5
init python:
    se_hcannon1 = Weapon("QF 4-inch Cannon", 75, 2, "hcannon1")
    se_hcannon1.desc = "Repurposed naval gun firing armor-piercing shells.\n4-5 DMG"
label hcannon1:
    n "Fire in the hole!"

    show layer master: # Shake effect
        truecenter
        parallel:
            zoom 1.025
            easeout 0.20 zoom 1.0
        parallel:
            xpos 630
            easein_elastic 0.20 xpos 640
    play sound hcannon
        
    $ dmg = renpy.random.randint(4, 5)
    $ enemyhp -= dmg
    $ pause(0.5)
    $ ehealth()

    "The enemy ship takes a hit ([dmg] DMG)."
    return
    
# AUGMENTS #

# Stealth Field (stealth)
# Allows the player to attack twice in a turn.
init python:
    au_stealth = Weapon("Stealth Field", 75, 3, "stealth")
    au_stealth.desc = "Allows the player to attack twice in a turn."
label stealth:
    $ stealth = True
    play sound beep
    $ pause(0.5)
    play sound cloak
    m "Stealth field activated, that should buy us enough time to fire a second volley."
    return
    