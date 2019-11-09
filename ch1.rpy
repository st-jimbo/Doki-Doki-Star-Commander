###########################################################################################
# Chapter 1
# The first sector
###########################################################################################

label ch1s1: 
    $ background = "bg space1"
    $ currentmode = "explore"
    $ dynbg()
    with dissolve_scene_full
    
    stop music fadeout 2.0
    play music civile
    
    show pship 1 zorder 2 at sh11
    "While I get adjusted to my surroundings, I take a seat in the captain's chair."
    "I'll be sure to ask Monika if I need any help managing the ship."
    m "[player], I've received a message from the Federation."
    m "It's... pretty dire. Let me show you."
    
    call showpoem (poem_fedintro, music=False, revert_music=False)
    
    mc "Shit, that doesn't sound good."
    mc "Looks like we'll make our way there."
    call shipmenu
    
    m "[player], mind if I fly towards that deactivated drone on the map?"
    m "We could destroy it for additional scrap!"
    mc "Sure."
    call examplebattle
   
    "With that done, we prepare to jump to the next system."
    "Yuri spools up the FTL drive."
    $ pause(0.25)
    play sound ftljump
    $ pause(0.75)
    jump ch1s2
    
label ch1s2:
    $ background = "bg space2"
    $ dynbg()
    with wipeleft_scene
    
    play sound arrive
    show pship 1 zorder 2 at sh11    
    "With the earth now out of sight, it's evident that we truly are in deep space now."
    call shipmenu
    m "Uhh, [player], I think the radar's picking something up."
    call examplehostilebattle
    
    "With the [shipname]'s first true battle over, all of us debrief in the ship's common area."
    
    stop music fadeout 2.0
    scene bg shipmain
    with wipeleft_scene
    play music t3
    show monika 3k zorder 2 at t11
    m "Good job team! It wasn't that bad, was it?"
    show monika 1a zorder 2 at t41
    show yuri 2q zorder 2 at t42
    y "That was... adrenaline-pumping, to say the least."
    show monika 1a zorder 2 at t41
    show yuri 1i zorder 2 at t42
    show sayori 2x zorder 2 at t43
    s "Well, we survived one, which means we can survive many more!"
    show sayori 1a zorder 2 at t43
    show natsuki 2c zorder 2 at t44
    n "That was pretty badass, to be honest."
    n 1d "I got to blow shit up!"
    show natsuki 2a zorder 2 at t44 
    mc "I wouldn't say I'm a natural at leadership, but at that moment it just... came to me."
    mc "...like I was able to read that other ship's actions and counteract them."
    show monika 1b zorder 2 at f41
    show yuri 1a zorder 2 at t42
    m "I told you, [player]! You were just underestimating yourself!"
    show monika 1a zorder 2 at t41
    show sayori 3q zorder 2 at f43
    s "I'm glad we have you as the captain, [player]!"
    show sayori 1a zorder 2 at t43
    show natsuki 2y zorder 2 at f44
    n "You definitely showed that ship who's boss back there."
    show natsuki 2a zorder 2 at t44
    show yuri 1d zorder 2 at f42
    y "Your skills as a captain are definitely exceptional, [player]."
    show yuri 1a zorder 2 at t42
    "I guess I'm definitely better at commanding a starship than writing poetry."
    if shipname == "Bismarck" or shipname == "KMS Bismarck":
        mc "Two thousand men and fifty thousand tons of steel set the course for the Atlantic with the Allies on their heel."
        mc "Firepower, firefight! Battle stations, keep the targets steady in sight!"
    else:
        mc "Heh, thanks everyone."
    mc "Anyways, that was just one of the many encounters we will likely face, so let's not get too excited just yet."
    show sayori zorder 2 at thide
    show natsuki zorder 2 at thide
    show yuri zorder 2 at thide
    hide sayori
    hide natsuki
    hide yuri
    show monika zorder 2 at t11
    mc "Monika, do you know where we could get some more equipment for the ship?"
    m 3b "I was just looking at such a place on the map!"
    m 1k "I've put it in the ship's navigation system, just let me know when you're ready!"
    mc "Nice, thanks."
    
    stop music
    play music civile
    call ship
    
    mc "Alright, let's go."
    "Yuri spools up the FTL drive."
    $ pause(0.25)
    play sound ftljump
    $ pause(0.75)
    jump ch1s3
    
label ch1s3:
    $ background = "bg nebula1"
    $ dynbg()
    with wipeleft_scene
    stop music fadeout 2.0
    play music t4
    
    play sound arrive
    show pship 1 zorder 2 at sh11
    "Monika flies the ship towards a decently-sized trading station."
    "The station is teeming with ships and shuttles conducting all sorts of business."
    m "This station {i}shouldn't{/i} mind which side you're on."
    m "I mean, credits are all the same regardless!"
    call screen dialog("Now is the opportunity to spend your hard-earned credits\non ship upgrades and repairs.", ok_action=Return())
    call screen dialog("As your progress through deep space increases, so does\nthe strength of the enemy. Therefore, it is important\nthat you upgrade your ship appropriately.", ok_action=Return())
    hide pship 1
    with wipeleft
    show station1 1 zorder 2 at sh11
    call ch1store1
    
    stop music fadeout 2.0
    play music civile
    hide station1
    with wipeleft
    show pship 1 zorder 2 at sh11
    "With that done, it's time to check up on the ship and the crew."
    call shipmenu
    
    jump modend