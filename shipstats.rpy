###########################################################################################
# SHIP STATS
# This script defines the stats and equipment for the ship.
###########################################################################################

# Default ship variables
default shipname = "Kestrel"
default shipclass = halberd.desc
default sprite = halberd.sprite
default maxhp = 25
default hp = 25
default bonusdmg = 0

# Ship states
default stealth = False

# Currency
default ammo = 20
default credits = 50

# Default ship power distribution and max power bonus
default shieldpower = False
default weaponpower = False
default enginepower = False
default wpbonus = 1 # Bonus damage

# Default ship equipment
default shipprimary = pr_halberd
default shipsecondary = se_artemis
default shipaugment = au_stealth
default shieldgen = sh_buck1
default engine = en_wasp1

# Ship status
default maxshields = 3
default shields = 3
default dodge = 10

init python:
# Damage the player's ship. Damage shields first. If damage would drop health below 0, then call game over.
    def damage(dmg):
        global hp, shields
        if shields <= dmg and shields != 0: # If damage is greater than shields, set shields to 0.
            shields = 0
        elif shields == 0: # Damage hull if shields are 0
            hp -= dmg
            if hp <= 0:
                renpy.jump("gameover")
        else:
            shields -= dmg
            
# Same as damage(), but calls a special ending instead.
    def specialdamage(dmg):
        global hp, shields
        if shields <= dmg and shields != 0: # If damage is greater than shields, set shields to 0.
            shields = 0
        elif shields == 0: # Damage hull if shields are 0
            hp -= dmg
            if hp <= 0:
                renpy.jump("modendgameover")
        else:
            shields -= dmg
                
# Damage the player's hull bypassing shields. If damage would drop health below 0, then call game over.
    def damagehull(dmg):
        hp -= dmg
        if hp <= 0:
            renpy.jump("gameover")
        
# Power Distribution Mechanics
    def shpwr(): # Increase max shield
        global shields, maxshields
        shields += shieldgen.bonus
        maxshields += shieldgen.bonus
    def unshpwr():
        global shields, maxshields
        shields -= shieldgen.bonus
        maxshields -= shieldgen.bonus
        
    def wppwr(): # Increase weapon damage
        global bonusdmg
        bonusdmg += wpbonus
    def unwppwr():
        global bonusdmg
        bonusdmg -= wpbonus
        
    def enpwr(): # Increase dodge chance
        global dodge
        dodge += engine.bonus
    def unenpwr():
        global dodge
        dodge -= engine.bonus
        
# Changing Power Distribution
    def doshieldpower():
        global shieldpower, weaponpower, enginepower
        if weaponpower == True:
            unwppwr()
            weaponpower = False
        if enginepower == True:
            unenpwr()
            enginepower = False
        shpwr()
        shieldpower = True
            
    def doweaponpower():
        global shieldpower, weaponpower, enginepower
        if shieldpower == True:
            unshpwr()
            shieldpower = False
        if enginepower == True:
            unenpwr()
            enginepower = False
        wppwr()
        weaponpower = True
            
    def doenginepower():
        global shieldpower, weaponpower, enginepower
        if shieldpower == True:
            unshpwr()
            shieldpower = False
        if weaponpower == True:
            unwppwr()
            weaponpower = False
        enpwr()
        enginepower = True
        
    def dounpower():
        global shieldpower, weaponpower, enginepower
        if shieldpower == True:
            unshpwr()
            shieldpower = False
        if weaponpower == True:
            unwppwr()
            weaponpower = False
        if enginepower == True:
            unenpwr()
            enginepower = False
            
# Call if player cannot afford something.
label cantafford:
    "I don't have enough credits for that."
    return