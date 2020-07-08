###########################################################################################
# HELP
# Monika's an expert when it comes to space cruisers. Make sure to go to her if you have any questions.
###########################################################################################

label help:
    show monika 2a zorder 2 at t11
    mc "Hey Monika, I might need a bit of help running this ship..."
    m 1b "Gotcha! What do you need help with?"
    show monika 1a zorder 2 at t11
    jump helpmenu

label helpmenu:
    menu:
        "HUD":
            show monika 1a zorder 2 at t11
            mc "What's being displayed on the HUD?"
            m 4b "The HUD displays the vital statistics of the ship: hull, shields, ammo, dodge, and credit balance!"
            m 3l "The wrench icon displays the ship's current hull integrity. You do not want this to reach zero!"
            m 3a "The shield icon displays the status of the ship's shields. This is how many hits it can take before going offline."
            m 3b "The missile icon displays ammunition amount, which is required for secondary weapons."
            m 4k "Lastly, the fast ship icon displays dodge chance, which is the chance to completely avoid an attack!"
            m 1a "Was there anything else you needed help with?"
            jump helpmenu

        "Power Distribution":
            show monika 1a zorder 2 at t11
            mc "Do you know how power distribution works?"
            m 4a "Each system on this ship requires power, however you can choose which one gets more than others."
            m 4k "The system that receives maximum power will perform more efficiently!"
            m 4a "Shields will have increased shield strength, weapons will deal increased damage, while engines will have increased dodge chance."
            m 4k "Different modules have different bonuses!"
            m 4b "However, only one system can have maximum power at a time."
            m 1a "Was there anything else you needed help with?"
            jump helpmenu
        "Shields":
            show monika 1a zorder 2 at t11
            mc "How do shields work?"
            m 4a "Shields function as a barrier between the ship's hull and the cold, dark expanse of space."
            m 4b "Most attacks on the ship will deplete the shields first, so it is important to keep them up!"
            m 4k "Additionally, the shield will always absorb the entire attack before going down, regardless of how powerful!"
            m 4a "Unlike hull, shields will regenerate given enough time, typically in between battles."
            m 3n "You might find a way to recharge shields during a battle though..."
            m 1a "Was there anything else you needed help with?"
            jump helpmenu
        "Weapons":
            show monika 1a zorder 2 at t11
            mc "How does the weapon system work?"
            m 4a "The ship can carry two types of weapons, a primary weapon and a secondary weapon."
            m 4b "Primary weapons are usually lasers, beams, and autocannons that do not require ammo."
            m 4k "On the other hand, secondary weapons are usually missiles and heavy cannons that do a lot more damage..."
            m 4l "...but require a supply of ammunition!"
            m 4b "Fortunately, ammo is interchangeable, no matter if you're firing guided missiles or sabot shells."
            m 3a "There are also augments which allow the ship to perform special abilities, such as stealth!"
            m 1a "Was there anything else you needed help with?"
            jump helpmenu
        "Engines":
            show monika 1a zorder 2 at t11
            mc "How do engines work?"
            m 4a "Engines are what propel the ship through space!"
            m 4b "The better your engines, the faster and more responsive the ship handles."
            m 4k "Efficient engines are also able to potentially dodge attacks!"
            m 1a "Was there anything else you needed help with?"
            jump helpmenu
        "Exit":
            show monika 1a zorder 2 at t11
            mc "That's all for now."
            m 2b "Okay! Let me know if you need anymore help."
            show monika 2a zorder 2 at t11
            jump monikamenu