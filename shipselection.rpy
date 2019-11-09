###########################################################################################
# SHIP SELECT
# All the available ships in the game.
###########################################################################################

# Ship Class
init 1 python:
    class Ship:
        def __init__(self, name, sprite, price): # Constructor
            self.name = name # Ship name
            self.sprite = sprite # Ship sprite
            self.price = price # Ship price
            self.desc = "Unknown ship." # Ship description
            self.maxhp = 25 # Ship max hp
            self.primary = None # Primary weapon
            self.secondary = None # Secondary weapon
            self.augment = None # Augment
            self.shieldgen = None # Shield
            self.engine = None # Engines

        def changeship(self):
            global shipclass, sprite, maxhp, hp
            shipclass = self
            sprite = self.sprite
            maxhp = self.maxhp
            hp = self.maxhp

        def equipall(self):
            self.primary.equip()
            self.secondary.equip()
            self.augment.equip()
            self.shieldgen.equip()
            self.engine.equip()

    # Halberd cruiser (default ship)
    halberd = Ship("Halberd-class cruiser", "halberd", 100)
    halberd.desc = "Standard light cruiser."
    halberd.maxhp = 25
    halberd.primary = pr_halberd
    halberd.secondary = se_artemis
    halberd.augment = au_stealth
    halberd.shieldgen = sh_buck1
    halberd.engine = en_wasp1

    # Longsword destroyer
    longsword = Ship("Longsword-class destroyer", "longsword", 100)
    longsword.desc = "Destroyer."
    longsword.maxhp = 20
    longsword.primary = pr_burst1
    longsword.secondary = se_artemis
    longsword.augment = au_stealth
    longsword.shieldgen = sh_buck2
    longsword.engine = en_wasp1

    # Broadsword frigate
    broadsword = Ship("Broadsword-class frigate", "broadsword", 100)
    broadsword.desc = "Frigate."
    broadsword.maxhp = 15
    broadsword.primary = pr_lcannon1
    broadsword.secondary = se_hcannon1
    broadsword.augment = au_stealth
    broadsword.shieldgen = sh_buck2
    broadsword.engine = en_wasp2

label shipselect:
    menu:
        "Select your starter ship."
        
        "Broadsword-class frigate":
            "Broadsword-class frigates are among the smallest class of warships available, trading hull integrity for speed and agility."
            menu:
                "Is this your option?"
                "Yes":
                    $ shipname = "Leopard"
                    $ broadsword.changeship()
                    $ broadsword.equipall()
                    return
                "No":
                    jump shipselect
        "Longsword-class destroyer":
            "Destroyers offer an equal balance of speed and durability, with the Longsword-class being the Federation's most common light warship."
            menu:
                "Is this your option?"
                "Yes":
                    $ shipname = "Fury"
                    $ longsword.changeship()
                    $ longsword.equipall()
                    return
                "No":
                    jump shipselect
        "Halberd-class cruiser":
            "While the Halberd-class light cruiser has been outdated and replaced by the newer Bardiche-class, many smaller navies continue to operate them due to their renowned durability."
            menu:
                "Is this your option?"
                "Yes":
                    $ shipname = "Kestrel"
                    $ halberd.changeship()
                    $ halberd.equipall()
                    return
                "No":
                    jump shipselect