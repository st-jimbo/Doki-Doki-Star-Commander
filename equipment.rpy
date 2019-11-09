###########################################################################################
# EQUIPMENT
# Definitions for all available ship equipment.
###########################################################################################

init python:
# Shields
    class Shield:
        def __init__(self, name, price, sp, bonus): # Constructor
            self.name = name # Item name
            self.desc = "Unknown item." # Item description
            self.price = price # Price in CR
            self.sp = sp # Shield points
            self.bonus = bonus # MAX bonus
            
        def equip(self): # Equip
            global shieldgen, maxshields, shields
            dounpower()
            shieldgen = self
            maxshields = self.sp
            shields = self.sp
            
        def buy(self): # Purchase and equip
            global credits, shieldgen, maxshields, shields
            dounpower()
            credits -= self.price
            shieldgen = self
            maxshields = self.sp
            shields = self.sp
# Engines
    class Engine:
        def __init__(self, name, price, dg, bonus): # Constructor
            self.name = name # Item name
            self.desc = "Unknown item." # Item description
            self.price = price # Price in CR
            self.dg = dg # Dodge chance
            self.bonus = bonus # MAX bonus
            
        def equip(self): # Equip
            global engine, dodge
            dounpower()
            engine = self
            dodge = self.dg
            
        def buy(self): # Purchase and equip
            global credits, engine, dodge
            dounpower()
            credits -= self.price
            engine = self
            dodge = self.dg

# SHIELD GENS #
# Format: Name, Price, Hitpoints, MAX bonus

# Buckler Mk.I (buck1)
# Hitpoints: 3 +1
    sh_buck1 = Shield("Buckler Mk.I", 10, 3, 1)
    sh_buck1.desc = "Tier 1 shield generator.\n3 hitpoints | +1 MAX bonus"

# Buckler Mk.II (buck2)
# Hitpoints: 4 +1
    sh_buck2 = Shield("Buckler Mk.II", 30, 4, 1)
    sh_buck2.desc = "Tier 2 shield generator.\n4 hitpoints | +1 MAX bonus"

# Bulwark Mk.IX (bulwark)
# Hitpoints: 10 +4
    sh_bulwark = Shield("Bulwark Mk.IX", 50, 10, 4)
    sh_bulwark.desc = "Tier 5 shield generator.\n10 hitpoints | +4 MAX bonus"

# ENGINES #
# Format: Name, Price, Dodge, MAX bonus

# Wasp Mk.I (wasp1)
# Dodge: 10 +5
    en_wasp1 = Engine("Wasp Mk.I", 10, 10, 5)
    en_wasp1.desc = "Tier 1 ship engines.\n10% dodge chance | +5% MAX bonus"

# Wasp Mk.II (wasp2)
# Dodge: 15 +5
    en_wasp2 = Engine("Wasp Mk.II", 20, 15, 5)
    en_wasp2.desc = "Tier 2 ship engines.\n15% dodge chance | +5% MAX bonus"

# Comet Mk.V (comet)
# Dodge: 30 +10
    en_comet = Engine("Comet Mk.V", 50, 30, 10)
    en_comet.desc = "Tier 5 ship engines.\n30% dodge chance | +10% MAX bonus"