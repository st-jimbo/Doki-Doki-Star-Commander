###########################################################################################
# INTRO
# The introductory chapter.
###########################################################################################
label intro:
    # previous music fadeout
    stop music fadeout 2.0
    
    # setup scene with background and music
    scene black
    with dissolve_scene_full
    
    # Debug purposes only
    call shipselect
    menu:
        "Would you like to skip the intro? Be adviced that the intro sequence is a VERY rough sketch."        
        "Yes":            
            "With the Sol system besieged, it appears there is no safe place to go that is devoid of Rebel influence..."
            "...unless, you look to the stars."
            return
        "No":
            jump ch0
    
label ch0:
    stop music fadeout 2.0
    "Some time passes..."
    scene bg club_day
    with dissolve_scene_full
    play music t3

    show monika 5 zorder 2 at t11
    m "Hi again, [player]!"
    mc "Sup, Monika."
    m "Glad to see you didn't run away on us. Hahaha!"
    mc "Nah, don't worry."
    mc "I usually keep my promises. Usually."
    # m 1b "By the way, the name of the ship is the [shipname], which is a [shipclass], with [hp] hull." # Debug
    # mc "What?" # Debug
    show monika zorder 1 at thide
    hide monika
    "Well, I'm back at the Literature Club."
    "Since I was the last to come in, everyone else is already hanging out."
    show sayori 4x zorder 2 at l31
    s "Heeeeyy [player]!"
    mc "Yo, Sayori."
    show yuri 1a zorder 2 at t32
    show sayori 1a zorder 2 at t31
    y "Thanks for keeping your promise, [player]."
    y "I hope this isn't too overwhelming of a commitment for you."
    y 1u "Making you dive headfirst into literature when you're not accustomed to it..."
    show natsuki 4e zorder 2 at t33
    n "Oh, come on! Like he deserves any slack."
    n "Sayori told me you didn't even want to join any clubs this year."
    n "And last year, too!"
    n 4c "I don't know if you plan to just come here and hang out, or what..."
    n "But if you don't take us seriously, then you wo--"
    
    # AND THIS IS WHERE ALL HELL BREAKS LOOSE
    stop music
    show sayori 1m zorder 2 at h31
    show yuri 1p zorder 2 at h32
    show natsuki scream zorder 2 at h33
    "Natsuki is suddenly interrupted by the blaring voice of the school PA system."
    "PA" "{i}Attention students! This is not a drill!{/i}"
    "PA" "{i}Remain calm as Federation forces are en route, I repeat Fe-{/i}"
    "PA" "{i}BZZZT{/i}"
    play music civilb
    "An air raid siren immediately starts going off."
    "I look at the expressions on the girls and all of three them appear terrified."
    s "What!? What is happening?!"
    show natsuki scream zorder 2 at h33
    n "WE'RE GOING TO DIE!!"
    n "How do they expect us to 'remain calm' when a fucking siren is going off?!"
    show natsuki zorder 2 at thide
    show yuri zorder 2 at thide
    show sayori zorder 2 at thide
    hide natsuki
    hide yuri
    hide sayori
    "While the girls are panicking, I pull out my phone and look up what the hell is going on."
    "My heart is pounding as I read the alert message that appeared on my lockscreen."
    "Alert" "HOSTILE FORCES INBOUND. SEEK IMMEDIATE SHELTER. THIS IS NOT A DRILL."
    "I swipe past the alert and immediately load up social media."
    "From the frantic messages I can read, it looks like the worst has finally happened."
    "The Rebel forces have finally begun their assault on the final bastion of the Federation."
    show natsuki scream zorder 2 at t33
    show yuri 1p zorder 2 at t32
    show sayori 1m zorder 2 at t31
    "I look back up at the girls."
    mc "We're being invaded. By the Rebels. It's likely the end of the Federation as we know it."
    mc "I've read about these guys before and it does not seem like they take too kindly to Federation citizens like ourselves."
    show natsuki at lhide
    hide natsuki
    show yuri zorder 2 at t22
    show sayori zorder 2 at t21
    "Natsuki screams as she runs off into the corner of the room."
    show sayori zorder 2 at h21
    s "Oh my god we {i}are{/i} going to die!"
    y 2o "I-If they are going to invade the city, maybe we should evacuate."
    show yuri 1f zorder 2 at t33
    show sayori 1c zorder 2 at t32
    show monika 4b zorder 2 at t31
    m "And that is exactly what we are going to do!"
    m 4l "Thankfully, I had the foresight to prepare for this."
    m 1n "First and foremost, we need to get the hell out of here."
    m 4b "Sayori and Yuri, get whatever supplies seems useful from this room."
    show yuri zorder 2 at lhide
    show sayori zorder 2 at lhide
    hide yuri
    hide sayori
    show monika zorder 2 at t11
    m 4b "[player], I'm going to need you to get Natsuki from the corner. We can't leave her behind for obvious reasons."
    mc "Got it."
    show monika zorder 2 at thide
    hide monika
    "I spot Natsuki curled up in the corner of the room. I rush over to her and tap her on the shoulder."
    show natsuki 1h zorder 2 at t11
    mc "C'mon Natsuki, we've got to go. Monika has a plan to get us out of here."
    n 1f "She better know what she's doing!"
    n 2e "And I'm not leaving here without my manga collection!"
    show natsuki at lhide
    hide natsuki
    "Natsuki rushes towards the closet and retrieves her manga collection."
    "I guess she's willing to die before she loses her manga."
    "She has her priorities straight, that's for sure."
    "As everyone hurriedly prepares for the evacuation, I glance out the window and spot a Rebel cruiser not too high in the sky."
    show monika 1d zorder 2 at t41
    show sayori 1e zorder 2 at t42
    show yuri 1n zorder 2 at t43
    show natsuki 1p zorder 2 at t44
    "My heart skips a beat as I spot the cruiser fire a barrage of missiles."
    play sound missile
    $ pause(0.33)
    play sound missile
    $ pause(0.33)
    play sound missile
    $ pause(1.0)
    show monika zorder 2 at h41
    show sayori 1p zorder 2 at h42
    show yuri zorder 2 at h43
    show natsuki 1v zorder 2 at h44
    play sound explosion1
    show layer master: # Explosion effect
        truecenter
        parallel:
            zoom 1.25
            easeout 1 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    $ pause(2.3)
    play sound fire loop
    show monika zorder 2 at s21
    show yuri 1p zorder 2 at s22
    show sayori 1p zorder 2 at lhide
    show natsuki 1v zorder 2 at lhide
    hide sayori
    hide natsuki
    "Sayo & Nat" "\"AAAHHHHHHH!!\""
    "A missile strikes the school! The force of the explosion causes the windows to shatter."
    "A large piece of shrapnel punches a hole through the clubroom wall and ignites a fire."
    "Yuri, Monika, and I quickly duck for cover."
    "Thankfully no one was hurt, but that was a damn close one."
    "Through the shattered windows I can see a classroom has been completely obliterated by the missile."
    mc "We need to get out of here. {i}Now!{/i}"
    y 1o "Y-yeah, I don't want to stick here any longer."
    m 3b "Everyone, follow me and be quick! I don't want anyone to be vaporized by a stray laser shot!"
    show monika zorder 2 at lhide
    hide monika
    "Monika runs out of the clubroom."
    "We follow not too far behind."
    
    stop sound
    scene black
    with wipeleft_scene
    play sound stairs
    "We follow Monika up a flight of stairs."
    mc "S-Sayori, do you know where she's leading us?"
    s "I have no clue, but I'm trusting her!"
    n "I don't wanna die! I haven't even finished this series yet!"
    m "Come on, we're almost there!"
    "At the top of the stairs is a door to the school rooftop. Monika opens it and walks through, and I do the same."
    
    scene bg roof
    with wipeleft_scene
    show monika 1a zorder 2 at t11
    mc "Monika, your plan better work out."
    m 1l "Don't worry, [player]. I have this all under control."
    show monika 1a zorder 2 at t41
    show sayori 1b zorder 2 at t42
    show yuri 1o zorder 2 at t43
    show natsuki 1k zorder 2 at t44
    "Soon, the rest of the gang arrives. Looks like we are the only ones up here."
    
    scene bg sky2 
    with wipeleft
    "I look at the sky and it's filled with both Rebel and Federation ships duking it out with lasers, cannons, and missiles."
    "It's like the Battle of Britain of the future."
    "I spot the Rebel cruiser that had fired the missile earlier going down in flames, having been shot by a planet-side anti-ship battery."
    
    scene bg roof
    with wipeleft
    show monika 1b zorder 2 at i41
    show sayori 1b zorder 2 at i42
    show yuri 1o zorder 2 at i43
    show natsuki 1k zorder 2 at i44
    m 1b "Stand back and watch this."
    "Monika pulls out a device from her pocket and activates it."
    play sound beep
    $ pause(0.50)
    play sound decloak
    show sayori 1b zorder 2 at h42
    show yuri 1f zorder 2 at h43
    show natsuki 1c zorder 2 at h44
    "Is that... a [shipclass]? It just seemingly materialized out of nothing!"
    "How the hell did Monika manage to acquire one of these?"
    m 3b "Alright everybody, hop in! There's no time to spare!"
    "We all climb into the ship through the side entry hatch."
    
    scene bg sky1 
    with wipeleft
    "A Rebel ship notices us attempting to take off and opens fire."
    play sound hlaser
    $ pause(0.25)
    play sound hlaser
    $ pause(0.75)
    play sound hull1
    $ pause(0.25)
    play sound hull1
    "The shots miss and hit the school rooftop instead."
    m "Shit! Hold on!"
    play sound hlaser
    $ pause(0.25)
    play sound hlaser
    $ pause(0.75)
    play sound hull1
    $ pause(0.25)
    play sound shield1
    $ pause(0.75)
    play sound cloak
    "Monika re-activates the cloaking system and applies full power to the throttle."
    stop music fadeout 1.0
    play sound takeoff
    $ pause(2.5)
    scene white # Flash white
    with dissolve
    $ pause(2.5)
    scene bg sky3 # Kestrel launched
    with dissolve
    $ pause(1)
    "Before I know it, we're in space."
    
    # Space
    
    stop music fadeout 2.0
    scene bg shipmain
    with wipeleft_scene
    play music m1
    
    show sayori 1b zorder 2 at t31
    show yuri 2f zorder 2 at t32
    show natsuki 5g zorder 2 at t33
    "All of us made it in one piece."
    "Everyone appears to be in a mixture of shock, relief, and exhaustion."
    show sayori 1b zorder 2 at f31
    s 1h "Well, goodbye Earth. I guess we really are in space now."
    s "I'm gonna miss it back down there."
    show sayori 1e zorder 2 at t31
    show yuri 3v zorder 2 at f32
    y "I'm not sure I'm prepared to start a new life up in space..."
    y "I-I think I'm just gonna collapse on this seat over here."
    show yuri zorder 2 at thide
    hide yuri
    "Yuri collapses on one of the ship seats."
    show sayori 1e zorder 2 at t31
    show natsuki 5g zorder 2 at f33
    n 5c "As long as I have my manga with me, I'm good."
    show natsuki 5g zorder 2 at t33
    stop music fadeout 2.0
    mc "Speaking of which..."
    "I peer out the ship window and find that the Earth..."
    "{i}...is completely missing!{/i}"
    mc "Is it just me or is the Earth {i}completely missing from view{/i}?"
    play music t7
    show sayori 1m zorder 2 at h31
    show natsuki 1p zorder 2 at h33
    "Sayo & Nat" "\"WHAT!?\""
    "Sayori and Natsuki appear as shocked as I am."
    show monika 1m zorder 2 at t32
    "Monika sheepishly walks in from the cockpit."
    "Something tells me something went terribly wrong."
    show sayori 1b zorder 2 at t31
    show monika 2n zorder 2 at f32
    m "Okay, everyone..."
    m "...there may have been a bit of a problem when I got us out of there."
    show monika 2o zorder 2 at t32
    show natsuki 5f zorder 2 at f33
    n "A {i}bit{/i} of a problem?"
    show natsuki 5g zorder 2 at t33
    "Monika nods."
    show monika 2n zorder 2 at f32
    m "Our FTL drive malfunctioned while we used hyperdrive, sending us waaaay off course."
    m 1l "Instead of placing us next to the moon..."
    m 1l "...we were placed hundreds of light years away!"
    show monika 1r zorder 2 at t32
    show natsuki 1p zorder 2 at h33
    show sayori 1m zorder 2 at h31
    "Everyone is in disbelief."
    mc "Well, we're in deep shit now."
    show natsuki 5r zorder 2 at f33
    show sayori 1b zorder 2 at t31
    n "Monika, you better think of something to get us back home."
    n "At least, when everything's cooled down obviously."
    show natsuki 5i zorder 2 at t33
    show sayori 2c zorder 2 at f31
    s "I'm sure she can think of something! Right?"
    stop music fadeout 2.0
    "There's a silence before Sayori and Natsuki sit down next to Yuri."
    show sayori zorder 2 at thide
    show natsuki zorder 2 at thide
    hide sayori
    hide natsuki
    "I'm not losing hope just yet."
    show monika 1i zorder 2 at t11
    mc "Monika..."
    show monika 1e zorder 2 at t11
    "Monika turns towards me and begins to smile. A shimmer of hope appears."
    play music t8
    m "I think I know what we can do."
    m "But first, I haven't even gotten around to naming this ship."
    m 1b "Want to come up with a name for me, [player]?"
    m 5a "Ehehe~"
    mc "Uhhh, how about the..."
    # Ask the player to name the ship!
    $ shipname = ""
    while not shipname:
        $ shipname = renpy.input('Name of Ship', default='Kestrel', length=20).strip(' \t\n\r')
    m 2b "Okay!"
    m 4k "Everyone, welcome to the [shipname]!"
    if shipname == "Kestrel":
        m 1k "Sticking to the defaults I see, [player]?"
    elif shipname == "Bismarck" or shipname == "KMS Bismarck":
        mc "Pride of a nation..."
        mc "...a beast made of steel..."
        m 1b "Good choice [player]!"
    elif shipname == "Hood" or shipname == "HMS Hood":
        mc "The Mighty Hood..."
        m 1b "Good choice [player]!"
    elif shipname == "Samuel B Roberts" or shipname == "USS Samuel B Roberts":
        mc "The destroyer escort that fought like a battleship..."
        m 1b "Good choice [player]!"
    elif shipname == "Laffey" or "USS Laffey":
        mc "The ship that would not die..."
        m 1b "Good choice [player]!"
    else:
        m 1b "Good choice [player]!"
    m 1b "By the way, I need to tell you something. Follow me."
    show monika zorder 2 at thide
    hide monika
    "I follow Monika to the cockpit of the ship."
    
    scene bg shipcockpit
    with wipeleft_scene
    show monika 1l zorder 2 at t11
    m "Oh, I almost forgot to take us off stealth."
    play sound beep
    $ pause(0.50)
    play sound decloak
    m 1b "There you go! At this location, we shouldn't have anyone finding us anyways."
    m 2n "Anyways, with that out of the way..."
    m 2b "[player], you're now the captain of the [shipname]!"
    m 1k "It only seems right since you named the ship after all."
    "Wait, so just five minutes within entering this ship, she decides to relinquish captain to {i}me?!{/i}"
    show monika 1d zorder 2 at t11
    mc "What? I'm the captain of the ship now?"
    mc "I can hardly manage my own sleep schedule, let alone an entire frickin' space cruiser!"
    m 1b "Don't worry, most of the ship's systems are automated!"
    m 1l "{i}Most{/i} of them..."
    m 2b "You can leave me to do the flying, the other girls can manage the main systems of the ship..."
    m 1b "Shields, weapons, and engines!"
    m 1k "As you're the captain, all you have to do is to tell us what to do!"
    show monika 1d zorder 2 at t11
    mc "I don't think I'm that good at leadership, I thought that would be a role more suitable for you, Monika."
    mc "I mean, you are the president of the Literature Club after all."
    m 2n "Well, the Literature Club kind of... doesn't exist anymore."
    m "You know, being obliterated alongside the rest of the city in the attack."
    m 1b "But don't say you're bad at leadership, [player]!"
    m "I'm sure you are better than you think! Especially with how much Sayori has talked about you with me."
    m 5a "Ehehe~"
    mc "Can't say I'm surprised."
    m 2b "I can be your second-in-command, then! I'll help you whenever necessary!"
    m 1b "Anyways, she's all yours captain!"
    mc "Thanks, Monika. I'll try my best."
    m 5a "I knew I could count on you!"
    "So a space cruiser crewed by four schoolgirls and a schoolboy. I wonder how long we'll last until we get blasted out of the sky by space pirates or something."
    "Monika and I walk back towards the rest of the girls."
    
    stop music fadeout 2.0
    scene bg shipmain
    with wipeleft_scene
    show monika 1b zorder 3 at t32
    play music t3
    m "Okay, everyone! I hope you're all getting settled in now."
    m 1l "I know it might be a bit intimidating to be up in space all of a sudden, but think of it like a flying clubroom!"
    m 1b "We're going to be just fine, especially with our new captain, [player]!"
    show sayori 4x zorder 2 at t31
    show monika 1a zorder 3 at t32
    s "Woah, you're the captain now [player]?"
    mc "It appears so."
    show sayori 1a zorder 2 at t31
    show natsuki 4e zorder 2 at t33
    n "[player], you better not get us killed out there."
    n 4w "I don't want to get abducted by aliens or sucked into a black hole or something."
    show natsuki 4i zorder 2 at t43
    show monika 1a zorder 3 at t42
    show sayori 1a zorder 2 at t41
    show yuri 3b zorder 2 at t44
    y "I'm sure [player] will try his best to avoid such a situation."
    show yuri 1a zorder 2 at t44
    show natsuki 3e zorder 2 at f43
    n "He better!"
    show natsuki 4i zorder 2 at t43
    show monika 1b zorder 3 at f42
    m "Don't worry Natsuki. If I didn't trust him I wouldn't have chosen him to be captain."
    m 4b "Anyways, everyone here is going to have an important role to fulfill on this ship."
    m 4b "Although most systems on this ship are automated, the main systems still needs someone to control them..."
    m 4k "So I'm going to assign each one of you to a role!"
    show monika 2e zorder 3 at t42
    show sayori 1n zorder 2 at t41
    show natsuki 2o zorder 2 at t43
    show yuri 1f zorder 2 at t44
    "Right as Monika finished speaking I could see the look of surprise on everyone's faces."
    "Everyone is as shocked as I was."
    show natsuki 2e zorder 2 at f43
    n "Monika, we haven't even left high school and you're expecting {i}us{/i} to be able to run a frickin' spaceship!?"
    show monika 1g zorder 3 at t42
    n 4w "Don't you think that's a little bit too ambitious?"
    show natsuki 2o zorder 2 at t43
    show yuri 2q zorder 2 at f44
    y "I-I agree, I believe such roles would require at least some training."
    y 3v "Especially concerning something as vital as the systems of a spaceship..."
    show yuri 1f zorder 2 at t44
    show monika 1l zorder 3 at f42
    m "Well..."
    m "It shouldn't be too difficult to grasp the basics."
    m 1b "I mean if I could learn how to fly this thing in a day, then you guys shouldn't have any problems!"
    show monika 1a zorder 3 at t42
    show natsuki 2c zorder 2 at t43
    show sayori 2c zorder 2 at f41
    s "Do you really think we can do it Monika? It seems a bit overwhelming."
    show monika 2a zorder 3 at f42
    show sayori 1a zorder 2 at t41
    m 1b "Of course!"
    m 2b "Seriously everyone, it'll be easy!"
    show sayori 1a zorder 2 at t41
    show monika 1a zorder 3 at t42
    show natsuki 2a zorder 2 at t43
    show yuri 1a zorder 2 at t44
    "It seems like everyone has begun to lighten up."
    show sayori zorder 2 at thide
    show monika 4k zorder 3 at t11
    show natsuki zorder 2 at thide
    show yuri zorder 2 at thide
    hide sayori
    hide natsuki
    hide yuri
    m "Anyways, it's time to assign each one of you to a role!"
    show monika 4b zorder 3 at t21
    show sayori 1a zorder 2 at t22
    m "Sayori, you can operate the shields..."
    show sayori zorder 2 at thide
    hide sayori
    show natsuki 1a zorder 2 at t22
    m "Natsuki, you can man the weapons..."
    show natsuki zorder 2 at thide
    hide natsuki
    show yuri 1a zorder 2 at t22
    m "..and Yuri, you can control the engines!"
    show yuri zorder 2 at thide
    hide yuri
    show monika 1a zorder 3 at t11
    "Monika turns towards me."
    m 1b "Of course, [player], you're the captain!"
    m 2a "Oh, and I almost forgot."
    "Monika pulls out a crate from the corner of the room and opens it."
    "Inside is a collection of energy-based firearms."
    m 2b "Each one of you is going to need a weapon to defend yourselves with."
    m 2l "Space can be a dangerous place after all!"
    show monika 2a zorder 3 at t11 
    "Sayori and Yuri grab a pistol each, while Natsuki equips an energy shotgun. Monika picks up an SMG while I equip a laser carbine."    
    show monika 1a zorder 3 at t11 
    mc "I won't let any of you down. We're gonna complete this mission and make it out of here."
    mc "Wait, Monika. Do we even have a mission?"
    m 1l "..."
    m 1l "We should have one as soon as I hear back from the Federation!"
    show monika 1a zorder 3 at t11
    mc "Gotcha."
    
    scene bg space1
    with wipeleft_scene
    if shipname == "Bismarck" or shipname == "KMS Bismarck":
        "{i}From the mist, a shape, a ship is taking form...{/i}"
        "{i}And the silence of the seas are about to drift into a storm...{/i}"
        "{i}Sign of power, show of force! Raise the anchor, battleship's plotting its course.{/i}"
    else:
        "And so begins the story of the ship [shipname] and her crew."
        "We really are going to do this."
    stop music fadeout 2.0
    
    return