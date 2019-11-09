###########################################################################################
# HUB
# The hub chapter, where the player can speak to each crew member.
###########################################################################################

# Hub
label hub:
    scene bg shipmain
    with wipeleft
    # Select who to speak to
    menu:
        "Which crew member should I speak to?"
        
        "Monika (Piloting)":
            jump monika            
        "Sayori (Shields)":
            jump sayori            
        "Natsuki (Weapons)":
            jump natsuki            
        "Yuri (Engines)":
            jump yuri            
        "Exit":
            jump ship
        
# Monika (Piloting)
label monika:
    scene bg shipcockpit
    with wipeleft
    
    show monika 1a zorder 2 at t11
    m "Hi Captain [player]!"
    mc "Sup, Monika."
    m 1k "All systems are nominal."
    m 2b "Was there something you needed?"
    show monika 2a zorder 2 at t11
    jump monikamenu
    
label monikamenu:
    menu:
        "Ship Status":
            show monika 2a zorder 2 at t11
            mc "What's the current ship status?"
            m 2b "The name of the ship is the [shipname], which is a [shipclass.name]."
            m 2b "Hull integrity is at [hp]/[maxhp]. Ship balance is [credits] CR."
            m 2a "Did you need something else?"
            jump monikamenu
        "Power Distribution":
            show monika 2a zorder 2 at t11
            mc "How's the power being distributed between each system?"
            if shieldpower == True:
                m 2b "Shields are at MAX power, while weapons and engines are at normal power."
            elif weaponpower == True:
                m 2b "Weapons are at MAX power, while shields and engines are at normal power."
            elif enginepower == True:
                m 2b "Engines are at MAX power, while shields and weapons are at normal power."
            else:
                m 2d "No systems are at maximum power."
            m 4k "Remember, only one system can have maximum power at a time!"
            m 2a "Did you need something else?"
            jump monikamenu 
        "Rename Ship":
            show monika 2a zorder 2 at t11
            mc "I'd like to rename the ship."
            m 1b "Gotcha! What would you like to rename it to?"
            show monika 1a zorder 2 at t11
            $ shipname = ""
            while not shipname:
                $ shipname = renpy.input('Name of Ship', length=20).strip(' \t\n\r')
            m 2b "Okay! The ship is now called the [shipname]!"
            if shipname == "Monika" or shipname == "USS Monika" or shipname == "HMS Monika" or shipname == "IJN Monika" or shipname == "Just Monika":
                m 1a "I really like that name [player]."
                show monika 5 zorder 2 at h11
                m "Ehehe~"
            m 2a "Did you need something else?"
            jump monikamenu
        "Help":
            jump help
            m 1a "Did you need something else?"
            jump monikamenu
        "Exit":
            show monika 2a zorder 2 at t11
            mc "That's all for now."
            m 2b "Okay!"
            jump hub
    
# Sayori (Shields)
label sayori:
    scene bg shipmain
    with wipeleft
    
    show sayori 4r zorder 2 at t11
    s "Hiii!"
    show sayori 1a zorder 2 at t11
    mc "Hey, Sayori."
    s 3q "Shields are running just fine!"
    s 1x "Anything you want me to do, [player]?"
    show sayori 1a zorder 2 at t11
    jump sayorimenu
    
label sayorimenu:
    menu:
        "Current Equipment":
            show sayori 1a zorder 2 at t11
            mc "What shield generator do we currently have installed?"
            s 2c "We are using the [shieldgen.name] with [shieldgen.sp] hitpoints."
            s 1a "Did you need anything else?"
            jump sayorimenu
        "Increase Shield Power (+[shieldgen.bonus] SP)":
            show sayori 1a zorder 2 at t11
            mc "Can you allocate more power towards shields?"
            if shieldpower == True: # If already at full power
                s 1c "Shields are already at full power, captain!"
            else:
                s 2x "Alright!"
                $ doshieldpower()
            s 1a "Did you need anything else?"
            jump sayorimenu
        "Exit":
            show sayori 1a zorder 2 at t11
            mc "That's all for now."
            s 1x "Alright [player]."
            jump hub
    
# Natsuki (Weapons)
label natsuki:
    scene bg shipmain
    with wipeleft
    
    show natsuki 1a zorder 2 at t11
    n "Sup [player]."
    mc "Yo, Natsuki."
    n 2y "Weapons are locked and loaded."
    n 2d "Tell me when we get to blow shit up, alright?"
    n 4d "Anyways, what's up?"
    show natsuki 4a zorder 2 at t11
    jump natsukimenu
    
label natsukimenu:
    menu:
        "Current Equipment":
            show natsuki 4a zorder 2 at t11
            mc "What are the current ship weapons?"
            n 2d "The current weapons are the [shipprimary.name] and [shipsecondary.name]. The current augment is [shipaugment.name]."
            n 4a "Anything else?"
            jump natsukimenu
        "Increase Weapon Power (+[wpbonus] Primary DMG)":
            show natsuki 4a zorder 2 at t11
            mc "Can you allocate more power towards weapons?"
            if weaponpower == True: # If already at full power
                n 2c "Everything's already on weapons, [player]."
            else:
                n 2d "Roger that."
                $ doweaponpower()
            n 4a "Anything else?"
            jump natsukimenu 
        "Exit":
            show natsuki 4a zorder 2 at t11
            mc "That's all for now."
            n 2d "Okay then."
            jump hub
    
# Yuri (Engines)
label yuri:
    scene bg shipmain
    with wipeleft
    
    show yuri 1a zorder 2 at t11
    y "Greetings, [player]."
    mc "Hi, Yuri."
    y 2b "Engines are running and operational."
    y "Did you need something?"
    show yuri 1a zorder 2 at t11
    jump yurimenu
    
label yurimenu:
    menu:
        "Current Equipment":
            show yuri 1a zorder 2 at t11
            mc "What type of engines do we currently have installed?"
            y 2f "The installed engines are the [engine.name], which provide a [engine.dg]\% chance to dodge attacks."
            y 1a "What else can I do for you?"
            jump yurimenu
        "Increase Engine Power (+[engine.bonus]\% dodge)":
            show yuri 1a zorder 2 at t11
            mc "Can you allocate more power towards engines?"
            if enginepower == True: # If already at full power
                y 3f "Engines are already running at maximum capacity, [player]."
            else:
                y 1d "Sure thing."
                $ doenginepower()
            y 1a "What else can I do for you?"
            jump yurimenu
        "Exit":
            show yuri 1a zorder 2 at t11
            mc "That's all for now."
            y 1b "Okay."
            jump hub