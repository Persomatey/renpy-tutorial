define Chara = Character('Chara', color="#16eaf1")
define Albaz = Character('Albaz', color="#800000")

label start:
    "In the beginning, there was nothing..."
    "...but then the video game started."

label gymscene: 
    # Set up gym scene 
    scene bg gym # Also removes sprites and images 
    #show bg gym # Only replaces the bg img
    play music "audio/bgm_basketball.mp3" fadein 1.0 volume 0.5 

    # Gym routine 
    show zeil delighted 
    Chara "But, wait, who am I?"
    show zeil angry
    Chara "Ohhhhh"
    show extra normal at right 
    Albaz "Do I truly exit too?" 
    hide extra 
    Chara "Go away!"

    stop music fadeout 0.5 

label classroomscene: 
    # Set up classroom scene 
    scene bg classroom with fade
    play sound "audio/sfx_bell.mp3"

    # Classroom routine 
    show zeil delighted 
    Chara "Ello, govna"
    show extra normal at right 
    Albaz "Whoy ello there"

label choices: 
    default learned = False 
    Chara "Did you learn a thing or two?"

menu: 
    "Yes": 
        jump choices1_a 
    "...": 
        jump choices1_b 

label choices1_a: 
    $ learned = True 
    Chara "Great job!"
    jump choices1_common 

label choices1_b: 
    $ learned = False 
    Albaz "You have failed me."
    jump choices1_common 

label choices1_common: 
    Chara "...the results are..."

label flags: 
    if learned: 
        Chara "Good job learning something."
    else: 
        Chara "And now we are done."