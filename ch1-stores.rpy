###########################################################################################
# CHAPTER 1 STORES
# Stores in the first sector.
###########################################################################################

# Store 1
label ch1store1:
    $ storename = "ch1store1" # Main store label
    menu:
        "[shipname] ([shipclass])\nHull: [hp]/[maxhp]\nBalance: [credits] CR{fast}"        
        "Ship Maintenance":
            jump expression storename + "m"
        "Weapons":
            jump expression storename + "w"
        "Equipment":
            jump expression storename + "e"
        "Exit":
            call screen dialog("If you have upgraded your shields or engines,\nmake sure to reset your power distribution settings.", ok_action=Return())
            "We prepare to leave the station."
            return
            
label ch1store1w:
    menu:
        "Primary Weapon: [shipprimary.name]\nSecondary Weapon: [shipsecondary.name]\nAugment: [shipaugment.name]{fast}"
        
        "[pr_halberd.name]\nPrimary | [pr_halberd.price] CR" if shipprimary.name != pr_halberd.name:
            menu:
                "[pr_halberd.desc]"
                "Purchase (Balance: [credits] CR)":
                    if (credits - pr_halberd.price) < 0:
                        call cantafford
                    else:
                        $ pr_halberd.buy()
                        play sound purchase
                    jump expression storename + "w"
                "Back":
                    jump expression storename + "w"
                    
        "[pr_lcannon1.name]\nPrimary | [pr_lcannon1.price] CR" if shipprimary.name != pr_lcannon1.name:
            menu:
                "[pr_lcannon1.desc]"
                "Purchase (Balance: [credits] CR)":
                    if (credits - pr_lcannon1.price) < 0:
                        call cantafford
                    else:
                        $ pr_lcannon1.buy()
                        play sound purchase
                    jump expression storename + "w"
                "Back":
                    jump expression storename + "w"
            
        "Back":
            jump expression storename
            
label ch1store1e:
    menu:
        "Shields: [shieldgen.name] | [maxshields] hitpoints\nEngines: [engine.name] | [dodge]\% dodge{fast}"
        
        "[sh_buck2.name]\nShield Gen | [sh_buck2.price] CR" if shieldgen.name != sh_buck2.name:
            menu:
                "[sh_buck2.desc]"
                "Purchase (Balance: [credits] CR)":
                    if (credits - sh_buck2.price) < 0:
                        call cantafford
                    else:
                        $ sh_buck2.buy()
                        play sound purchase
                    jump expression storename + "e"
                "Back":
                    jump expression storename + "e"
                    
        "[en_wasp2.name]\nEngines | [en_wasp2.price] CR" if engine.name != en_wasp2.name:
            menu:
                "[en_wasp2.desc]"
                "Purchase (Balance: [credits] CR)":
                    if (credits - en_wasp2.price) < 0:
                        call cantafford
                    else:
                        $ en_wasp2.buy()
                        play sound purchase
                    jump expression storename + "e"
                "Back":
                    jump expression storename + "e"
            
        "Back":
            jump expression storename
            
label ch1store1m:
    $ repairprice = 5 # Price to repair 1 hp
    $ fullrepair = (maxhp - hp) * repairprice
    $ ammoprice = 5 # Price for 1 ammo
    menu:
        "Hull: [hp]/[maxhp]\nAmmo: [ammo]\nBalance: [credits] CR{fast}"
        
        "Repair 1 HP ([repairprice] CR)" if hp < maxhp:
            if (credits - repairprice) < 0:
                call cantafford
            else:
                $ credits -= repairprice
                $ hp += 1
                play sound repair
            jump expression storename + "m"
            
        "Repair Full ([fullrepair] CR)" if hp < (maxhp - 1):
            if (credits - fullrepair) < 0:
                call cantafford
            else:
                $ credits -= fullrepair
                $ hp = maxhp
                play sound repair
            jump expression storename + "m"
            
        "Purchase ammo ([ammoprice] CR each)":
            if (credits - ammoprice) < 0:
                call cantafford
            else:
                $ credits -= ammoprice
                $ ammo += 1
                play sound purchase
            jump expression storename + "m"
            
        "Back":
            jump expression storename