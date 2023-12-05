#Dante Ryckman - DR
#Claudio Costa - CC
#Adam Huang - AH

import pygame, sys # DR - importing pygame

pygame.init() # DR - initializes all pygame modules

width = 1280
height = 720
screen = pygame.display.set_mode((width,height))
# DR - line 5-7 are creating the screen for our game

# CC - assigning values to the different rooms in the game so we can display images and texts accordingly
start = 0           
goose_choice1 = 1
goose_choice2 = 2
goose_choice3 = 3
goose_choice4 = 4
pre_building_choice = 5
building_choice1 = 6
building_choice2 = 7
building_choice3 = 8
building_choice4 = 9
pre_adam_choice = 10
adam_choice1 = 11
adam_choice2 = 12
pre_E7_choice1 = 13
pre_E7_choice2 = 14
E7_choice1 = 15
E7_choice2 = 16
E7_choice3 = 17
E7_choice4 = 18
pre_claudio_choice = 19
claudio_choice1 = 20
claudio_choice2 = 21
pre_dante_choice = 22
dante_choice1 = 23
dante_choice2 = 24
dante_choice3 = 25
pre_guard_choice = 26
guard_choice1 = 27
guard_choice2 = 28
pre_distract_choice = 29
distract_choice1 = 30
distract_choice2 = 31
distract_choice3 = 32
pre_escape_choice = 33
escape_choice1 = 34
escape_choice2 = 35
escape_choice3 = 36
death_choice = 37
win_choice = 38
rat_death_choice = 39
goose_death_choice = 40

# CC - Function to make fonts easier
def get_font(size): 
    """
    Get a Pygame font with the specified size.

    Parameters:
    - size (int): The size of the font to be created.

    Returns:
    - pygame.font.Font: A Pygame font object with the specified size.
    """
    
    return pygame.font.SysFont('times new roman', size)

# CC - gets a font with a specified size, using a font file located in the 'Steal-the-Tool-main/assets/' directory
text_font = get_font(20)

def play():
    """
    The main gameplay function where the player navigates through the storyline
    by making choices and experiencing different outcomes.

    This function manages the game's state transitions, displaying images and text
    based on the player's choices. The player progresses through various scenarios and
    interacting with NPCs.

    The game continues until the player reaches a win, death, or another outcome,
    at which point they are directed back to the main menu.

    Attributes:
    - current_state: An integer representing the current state of the game.
    - goose_death: A boolean flag indicating whether the player's first choice led to goose death in the end.

    Controls:
    - Keyboard input: The player uses the keyboard to make choices by pressing specific keys.
    - Escape key: Returns the player to the main menu.

    Returns:
    None
    """
    
    current_state = start # AH - Starts the game off in the start room
    goose_death = False # AH - A boolean that if switched to True, will make the player lose even if he actually technically won the game
    while True:
        y = 0 # AH - Defines y as 0 originally, but is only relevant later on in the code

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() # AH - Quit the game if the window close button is clicked
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu() # AH - If escape is clicked, the game returns to the main menu
                if current_state == start: # AH - game starts, images and texts will be shown on the screen. This continues on for many many lines.
                    if event.key == pygame.K_1: # AH - If the 1 key is clicked, the room changes accordingly
                        current_state = goose_choice1
                    elif event.key == pygame.K_2: # AH - If the 2 key is clicked, the room changes accordingly
                        current_state = goose_choice2
                    elif event.key == pygame.K_3: # AH - If the 3 key is clicked, the room changes accordingly
                        current_state = goose_choice3
                    elif event.key == pygame.K_4: # AH - If the 4 key is clicked, the room changes accordingly
                        current_state = goose_choice4
                elif current_state == goose_choice1:
                    current_state = win_choice # AH - First win option (easy)
                elif current_state == goose_choice2:
                    current_state = pre_building_choice # AH - pre choices are used as a way to give the options to the user and then the actual choices without the pre preceding the rest of the name continues the story
                elif current_state == goose_choice3:
                    current_state = pre_building_choice
                elif current_state == goose_choice4: # AH - Our first choice that will affect how the game will end. This choice will give you a different ending when you actually beat the game.
                    goose_death = True # AH - Goose death changed to True if you bully the goose
                    current_state = pre_building_choice 
                elif current_state == pre_building_choice:
                    if event.key == pygame.K_1: 
                        current_state = building_choice1
                    elif event.key == pygame.K_2: 
                        current_state = building_choice2
                    elif event.key == pygame.K_3: 
                        current_state = building_choice3
                    elif event.key == pygame.K_4: 
                        current_state = building_choice4
                elif current_state == building_choice1:
                    current_state = pre_adam_choice 
                elif current_state == pre_adam_choice: # AH - first time an npc(aka me) is introduced, choice 1 with the npc will restart you, second choice will lead you to another option that you could have chosen earlier.
                    if event.key == pygame.K_1: 
                        current_state = adam_choice1
                    elif event.key == pygame.K_2:
                        current_state = adam_choice2
                elif current_state == adam_choice1:
                    current_state = death_choice
                elif current_state == adam_choice2:
                    current_state = pre_E7_choice1
                elif current_state == building_choice2:
                    current_state = rat_death_choice  
                elif current_state == building_choice3:
                    current_state = pre_E7_choice1
                elif current_state == building_choice4:
                    current_state = death_choice 
                elif current_state == pre_E7_choice1:
                    if event.key == pygame.K_1: 
                        current_state = E7_choice1
                    elif event.key == pygame.K_2: 
                        current_state = E7_choice2
                    elif event.key == pygame.K_3: 
                        current_state = E7_choice3
                elif current_state == E7_choice1:
                    current_state = pre_claudio_choice 
                elif current_state == pre_claudio_choice: # CC - Claudio choices (one will kill you, and the other won't change anything)
                    if event.key == pygame.K_1: 
                        current_state = claudio_choice1
                    elif event.key == pygame.K_2: 
                        current_state = claudio_choice2
                elif current_state == claudio_choice1:
                    current_state = death_choice
                elif current_state == claudio_choice2:
                    current_state = pre_E7_choice1
                elif current_state == E7_choice2:
                    current_state = pre_dante_choice
                elif current_state == pre_dante_choice: # DR - Dante choices (one will allow you to progress the game, the others will kill you)
                    if event.key == pygame.K_1: 
                        current_state = dante_choice1
                    elif event.key == pygame.K_2: 
                        current_state = dante_choice2
                    elif event.key == pygame.K_3: 
                        current_state = dante_choice3
                elif current_state == dante_choice1:
                    current_state = pre_E7_choice2
                elif current_state == pre_E7_choice2: # CC - pre_E7_choice2 is practically the same as the other one, but it has one extra room (the broken elevator), which will allow the player to progress. If they do not go to the broken elevator room and instead go a route that doesn't include taking the ladder from Dante, they will either die or go back to pre_E7_choice1
                    if event.key == pygame.K_1: 
                        current_state = E7_choice1
                    elif event.key == pygame.K_2: 
                        current_state = E7_choice2
                    elif event.key == pygame.K_3: 
                        current_state = E7_choice3
                    elif event.key == pygame.K_4:
                        current_state = E7_choice4
                elif current_state == dante_choice2:
                    current_state = death_choice
                elif current_state == dante_choice3:
                    current_state = rat_death_choice
                elif current_state == E7_choice3:
                    current_state = death_choice
                elif current_state == E7_choice4:
                    current_state = pre_guard_choice
                elif current_state == pre_guard_choice:
                    if event.key == pygame.K_1: 
                        current_state = guard_choice1
                    elif event.key == pygame.K_2: 
                        current_state = guard_choice2
                elif current_state == guard_choice1:
                    current_state = pre_distract_choice
                elif current_state == guard_choice2:
                    current_state = death_choice
                elif current_state == pre_distract_choice:
                    if event.key == pygame.K_1: 
                        current_state = distract_choice1
                    elif event.key == pygame.K_2: 
                        current_state = distract_choice2
                    elif event.key == pygame.K_3: 
                        current_state = distract_choice3
                elif current_state == distract_choice1:
                    current_state = pre_escape_choice
                elif current_state == distract_choice2:
                    current_state = pre_escape_choice
                elif current_state == distract_choice3:
                    current_state = death_choice
                elif current_state == pre_escape_choice:
                    if event.key == pygame.K_1: 
                        current_state = escape_choice1
                    elif event.key == pygame.K_2: 
                        current_state = escape_choice2
                    elif event.key == pygame.K_3: 
                        current_state = escape_choice3
                elif current_state == escape_choice1:
                    current_state = death_choice
                elif current_state == escape_choice2:
                    current_state = death_choice
                elif current_state == escape_choice3:
                    if goose_death == False:  # CC - If goose death is still False and the player manages to finish the game, they actually get to win
                        current_state = win_choice
                    elif goose_death == True: # CC - If goose death is True, they still die at the end and don't win
                        current_state = goose_death_choice
                elif current_state == goose_death_choice:
                    current_state = death_choice
                elif current_state == win_choice:
                    main_menu() # CC - Returns to the menu if the player wins
                elif current_state == death_choice:
                    main_menu() # CC - Returns to the menu if the player dies
                elif current_state == rat_death_choice:
                    main_menu() # CC - Returns to the menu if the player dies of rat death

        # DR - Check the current state of the game and display corresponding text and images
        if current_state == start:
            # DR - Fill the screen with a black screen
            screen.fill('black')
            # DR - Displays an image onto the screen. The (53, 0) is where the image will be printed onto the screen (53 pixels from the left and 0 pixels from the top)
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/campus.png'),(53,0))
            # DR - Overlay text on the screen based on the current state and user choices
            text = ['You are a UofT student who has come to the University of Waterloo campus for one thing.', 'You want to steal the TOOL!!!!', 'You can\'t help but notice that the campus is much nicer than that of UofT.', 'You came to Waterloo to steal the tool because you feel that if UofT had the TOOL, the school will finally have the best engineering program in Canada.', 'Before you begin your search, a goose approaches you. What should you do?', '1. Give the goose $20', '2. Give goose a treat', '3. Ignore goose', '4. Frighten goose', '(choose by pressing number associated with option)']
            pygame.draw.rect(screen,'dark gray',[0,515,width,205]) # DR - Draws a rectangle which is where the text will be written
            for line in text: # DR - For every string in the text list
                written_text = text_font.render(line, True, 'white') # DR - Renders the text 
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y)) # DR - Where the text will be printed in the rectangle (10 pixels from the left of the screen and then just high enough that the text wont be printed out of the rectangle using the length of the text list)
                screen.blit(written_text,text_rect) # DR - Writes the text in the rectangle. The for loop allows the text to be printed on different lines instead of on just one big line
                y+=19 # DR - prints with a 19 pixel vertical offset (The rest have 20 pixel offsets, but this one has more text than the others)
                
     # DR - The same code is used for almost all of the rooms with the only difference being the text and the image that is printed as well as text_rect which will use midleft and a slightly different y value
        
        if current_state == goose_choice1:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/goose_victory.png'),(362,0))
            text = ['The goose appreciated the gesture so much it decided to become a real life Deus ex Machina.', 'It flew away and you hear incredibly loud explosions before you spot a shadow in the sky.', 'The goose returns with what appears to be the TOOL in its wings!!', 'You thank the goose and return to Toronto to gift the school with a most precious prize','','Press space to proceed']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(midleft = (10,height-20*len(text)+y-(205/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == goose_choice2:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/goose_treat.png'),(369,0))
            text = ['The goose appreciates the treat and jumps around with glee.', 'Your heart fills with a warmth you have never experienced before at UofT', 'You walk away feeling whole, a feeling you have not experienced in a long time. You feel like your journey to find the', 'Tool will be a lot more sucessful','','Press space to proceed']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == goose_choice3:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/ignore_goose.png'),(380,0))
            text = ['You choose to ignore the goose because you don\'t have the time for stupid goose.', 'Before arriving on campus, you forgot to do a google search to find where the TOOL is being held. You pull out', 'your phone to check but realise you have no signal. Instead of finding any nearby wifi sources, you attempt to guess where it is off pure intuition alone', 'You have a strong feeling the TOOL is being held in 1 of 4 buildings','','Press space to proceed']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == goose_choice4:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/goose_scare.png'),(380,0))
            text = ['The goose is visibly distraught and begins running away towards its fellow geese.', 'You feel satisfied with yourself as you are an evildoer who attends an inferior university. As you walk away you glance out of', 'the corner of your eye the goose seemingly huddled together discussing something. You think nothing of it and walk away.','','Press space to proceed']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == pre_building_choice:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/campus.png'),(53,0))
            text = ['Where would you like to search?','1. RCH','2. SLC Tim Horton\'s','3. E7','4. Library','(please press the corresponding number on your keyboard)']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == building_choice1:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/RCH.png'),(78,0))
            text = ['You decide to walk into a shabby, bunker-like building. You explore through the rooms as you don\'t have the slightest', 'clue where the TOOL could be held. Many of the rooms are empty']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == building_choice2:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/SLC.png'),(232,0))
            text = ['You walk into the Student Life Centre.', 'There are many students studying and hanging out, you realize how much better life at Waterloo is compared to UofT and wish you\'d came to Waterloo instead.', 'You mindlessly wonder SLC regretting your choice of attending UofT until you approach Tim Hortons...']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == building_choice3:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/E7.png'),(180,0))
            text = ['You decide to walk into E7 because it is the biggest and newest building on campus. Your breath is','taken away by the sight of the inner building. (In the back of your mind you think that this building','is better than ANY building at UofT) The sight is so beautiful that you almost forget why you are here.','You still don’t know where the TOOL is being held, and this building is massive.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == building_choice4:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/library_death.png'),(372,0))
            text = ['You walk into the Dana-Porter library. You see a plethora of books piled on incredibly tall shelves. You think','that one of these books may hold the information as to where the TOOL is being held. You decide to take','a book off the self, but unfortunately for you, that was a low-bearing book. It was keeping the','whole shelf from falling down. Suddenly, books start to fall towards you. You make a break for the exit,','but you\'re too late. A massive book called\'where the TOOL is being held\' finds it\'s way onto your head.','One could say the TOOL ended up finding you']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == pre_adam_choice:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/shadow_sleeping.png'),(352,0))
            text = ['You continue to explore the RCH building, until you finally stumble upon a room with a person inside it.','You enter room 301 of the RCH building, and see a mysterious shadowy figure.', 'He appears to have slept through his classes and no one bothered to wake him up to inform him that class was over.','The figure awakens and seems to see right through you, as he notices that you are not a UWaterloo student', '-Adam:"Hey!, you don\'t belong here you filthy UofT rat. You\'re probably here to steal the tool aren\'t you."', '"Well you\'re in luck, I just happened to be running low on funds, and for a cheap price of 20 dollars I\'ll let you go and I\'ll even let"', '"you know which building the TOOL is in."', '1 to ignore Adam', '2 to give Adam 20 dollars']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == adam_choice1:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/chased_shadow.png'),(367,0))
            text = ['Adam is upset at you for not paying him 20 dollars. He desperately needed the 20 dollars as', 'he ran out of meal plan 2 weeks ago, and "can\'t afford to stop the bulk".', 'Adam brutally beats you and you awaken with a terrible headache back where you first arrived at UWaterloo']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == adam_choice2:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/shadow_$20.png'),(363,0))
            text = ['\"good choice scrub\" says Adam, \"The TOOL is probably in E7 or something,', 'now get out of here before I decide 20 dollars is not enough\"', 'You walk out of RCH 301 feeling like you were just the victim of a highway robbery. You head', 'to E7 anyways as you don\'t know where else to go anyways']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == pre_E7_choice1:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/E7.png'),(180,0))
            text = ['Where will you begin your search for the TOOL?','1. Ideas Clinic','2. Study Lounge','3. Robotics Lab']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == E7_choice1:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/claudio_soap.png'),(366,0))
            text = ['You wonder around E7 looking for possible places the tool could be, you stumble across', 'the Ideas Clinic and see that there is a student named Claudio inside working on his soap and walk inside.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == E7_choice2:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/dante.png'),(363,0))
            text = ['You decide to check the study lounge for the TOOL. You think they may have it on display to give the','Engineering students some power by being in it\s presence. You search for about 10 minutes before seeing','a student named Dante sitting in a chair, working on a project called \“Steal the Tool\”. You approach','him and begin to make conversation about Waterloo things to try and gain his trust. Eventually, he','offers you an item from the table in front of him as a kind gesture. You think these items are a bit','weird to be a kind gesture, but you realize these items have potential to be useful for you.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == E7_choice3:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/robot_death.png'),(359,0))
            text = ['You\'re exploring the halls of E7 when you hear loud noises coming from the robotics lab, having piqued your interest,', 'you decide to walk into the robotics lab to check out the source of the noise. You open the doors', 'of the robotics lab and find the source of the noise to be a large humanoid robot, you stand in shock', 'as you\'ve never seen anything so impressive at UofT. The robot looks at you and runs a scan of your face,', 'the robot searches through its database and finds that you are not a waterloo student but rather a UofT student', 'and quickly dispatches of you with a right hook followed by a left upper cut. You suffer a severe concussion and get sent back to UofT']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == pre_E7_choice2:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/in_E7.png'),(179,0))
            text = ['Where do you want to search?','1. Soap lab','2. Study lounge','3. Robotics lab','4. Broken elevator']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == E7_choice4:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/broken_elevator.png'),(374,0))
            text = ['You decide to climb the broken elevator shaft. It takes you to a secret floor which is hidden from','staircases. In this room, you see the TOOL guards. You see the TOOL in a big glass case, surrounded','by multiple guards. You came this far, so you need to go through with stealing the TOOL. No backing out.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == pre_claudio_choice:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/claudio.png'),(369,0))
            text = ['You greet Claudio and make conversation hoping to gain some information on the tool.', 'After what feels like 4 hours of Claudio rambling on about how hard his courses are', 'you cut to the chase and ask him about the whereabouts of the tool', 'Claudio- "oh you want to know where the tool is? Well its at the V1 green, just go there cause you can\'t miss it."', '1 to go to V1 green', '2 to say bye to Claudio and return to E7']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == claudio_choice1:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/quidditch_death.png'),(367,0))
            text = ['Thinking that your hours spent listening to Claudio\'s ramble paid off, you gleefully skip to the V1 Green to search for the TOOL', 'As you search through the grass for the TOOL you are interrupted by the quidditch team asking you to leave so they can practice.', 'You brush them off and tell them quidditch is stupid and not a real sport. Infuriated by your comment, the quidditch team', 'performs a cringy ritual turning you into a goose. You can feel the intelligence and concious thought exiting your brain and your', 'memories being erased due to your new small avian brain not being able to process the information.', 'You are now doomed to forever roam the V1 Green and eat grass all day.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == claudio_choice2:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/leaving_room.png'),(369,0))
            text = ['You realize that you wasted your time with Claudio and that there is no way that the TOOL would be at the V1 Green', 'You feel frustrated and return to E7.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == pre_dante_choice:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/dante.png'),(363,0))
            text = ['What will you take from the table?','1. A ladder','2. A spider that can turn you into spiderman','3. A Tim Horton\'s gift card']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == dante_choice1:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/ladder.png'),(366,0))
            text = ['You decide to take the ladder from Dante. Although this is the largest of the items, you think this','item could potentially be the most useful of the three. You finish searching the lounge and find','nothing. You decide to go back to the main room and try searching a new room with your','newfound piece of equipment.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == dante_choice2:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/spider.png'),(369,0))
            text = ['You decide to take the spiderman spider and let it bite you to gain the powers of spiderman, but wait, this isn\'t the MCU.', 'You look back at Dante and ask him what kind of spider is this?', 'Dante replies "its just a black widow that I painted to look like its the spiderman spider, why do you ask?', 'as Dante finishes speaking you realized your naivety and accept your imminent death.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == dante_choice3:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/tim_hortons.png'),(369,0))
            text = ['You realize how tired you are after an entire day of searching for the TOOL.', 'You decide to head to Tim Hortons at SLC to grab a coffee with your brand new gift card.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == pre_guard_choice:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/guards.png'),(366,0))
            text = ['You need to get past the guards.', '1 to distract the guards', '2 to rush past the guards']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == guard_choice1:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/distraction.png'),(380,0))
            text = ['You realize your physical abilities are less than optimal at the moment,', 'and the best choice of action would be to distract the guards and sneak past them.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == guard_choice2:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/guard_death.png'),(368,0))
            text = ['You rush the guards in an attempt to push past them and make a break for the tool.', 'However you over estimated your athletic abilities and get beaten up by the guards.', 'You are badly injured and have to go back to Uoft.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == pre_distract_choice:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/distraction.png'),(380,0))
            text = ['You need to find a way to distract the guards. How will you go about doing that?','1. Airdrop the guards funny memes','2. Lie and yell \"SALE AT WSTORE!\"','3. Chemical Warfare(fart spray)']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == distract_choice1:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/airdrop.png'),(369,0))
            text = ['You decide the best choice of action would be to airdrop a meme to the TOOL guards. You search your','phone for the best, funniest, most distracting meme you can possibly find. You send the meme off to','the guards, and surprisingly, they all look at their phones. The meme you sent was so funny, it caused','all the guards to simultaneously pee their pants. They all run to the bathroom to clean themselves,','leaving the TOOL completely unguarded.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == distract_choice2:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/sale.png'),(366,0))
            text = ['You decide the best choice of action would be to yell \”SALE AT WSTORE\” to the TOOL guards. You stand','up from your hiding spot and yell the magic words. All of a sudden, all the TOOL guards flee for the','wstore because they simply could not resist the sales on the quality merchandise sold at the wstore.','The TOOL is now completely unguarded.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == distract_choice3:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/chem_warfare.png'),(367,0))
            text = ['You initiate chemical warfare on the guards, and it is highly effective.', 'The guards are knocked out almost instantly by the foul stench and your path to the TOOL is clear.', 'However you underestimated the power of the fart spray and also choke out beside the guards.', 'As you regain consciousness you see the guards looking down on you menacingly.', 'You get beaten up and are hospitalized for weeks.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == pre_escape_choice:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/rooftop.png'),(367,0))
            text = ['You successfully steal the tool and run onto the roof, you need to think of a way to get down.', '1 to hang glide off the roof', '2 to zipline down on the powerlines using the TOOL', '3 to go back down the way you came up']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == escape_choice1:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/hang_glider_death.png'),(367,0))
            text = ['You take a couple steps back to get a running start to jump off the roof.', 'As you leap off the side of E7 you deploy your hang...', 'Wait...', 'You don\'t have a hang glider.', 'Let\'s just say you had a bad time...']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == escape_choice2:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/zipline_death.png'),(360,0))
            text = ['You see a powerline and hook onto it with the TOOL, when your life flashes before your eyes.', 'During those few miliseconds before your body is fried by the high voltage electricity, you realize your stupidity', 'of putting an oversized pipe wrench made out of \"METAL\" onto a high voltage powerline.', 'I\'m not gonna describe what 44000 volts does to a person but I\'m sure you know what happened to you.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == escape_choice3:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/wrench_stollen_success.png'),(344,0))
            text = ['You realize that to hang glide down, well, you would need a hang glider, and zip lining down a power line', 'with a metal TOOL, is not the smartest decision.', 'So you simply walk back down the stairs and out of the front door with the TOOL in hand.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == death_choice:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/you_died.png'),(0,0)) # DR - Only prints the image as this room does not require any text
        elif current_state == rat_death_choice:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/rat_death.png'),(359,0))
            text = ['You hear loud squeaks coming from the Tim Hortons.', 'The squeaks grow louder and louder as you walk over to investigate the strange noises, when you notice something,', 'no...', 'rather many dark creatures scurrying around your feet. When you finally realize the true nature of the creatures it is already too late.', 'The hundreds if not thousands of rats swarm all over you as you feel their small feet all over your body', 'You lose consciousness.']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10,height-20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        elif current_state == win_choice:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/win.png'),(265,0)) # DR - Only prints the image as this room does not require any text
        elif current_state == goose_death_choice:
            screen.fill('black')
            screen.blit(pygame.image.load('Steal-the-Tool-main/assets/goose_death.png'),(374,0))
            text = ['You walk out of E7 with the TOOL inhand, waiting for the next bus back to UofT. When out of no where you', 'hear loud honks getting louder and louder. You turn around and see dozens of geese lead by the goose you scared when you first arrived.', 'The geese are armed with an assortment of weapons ranging from knuckle dusters to baseball bats.', 'You stand flabberghasted as your brain cannot process how these geese are holding human weapons with their wings.', 'You attemp to fight back but your attempt was futile.','you are then beaten to oblivion by the geese and charged with a 5000 dollar fine for attempting to harm Canadian Geeseef']
            pygame.draw.rect(screen,'dark gray',[0,520,width,200])
            for line in text:
                written_text = text_font.render(line, True, 'white')
                text_rect = written_text.get_rect(topleft = (10, height - 20*len(text)+y-(200/len(text))))
                screen.blit(written_text,text_rect)
                y+=20
        pygame.display.flip() # DR - Updates the entire display surface to the screen

def main_menu():
    """
    Display the main menu screen and handle user input.

    The function continuously displays the main menu screen, including the game title
    and instructions to start the game. It waits for user input and responds to the
    Space key to initiate the game or the Escape key to quit the game.

    Returns:
    None
    """
    while True:
        run = True

        # CC - Display the background image on the screen
        screen.blit(pygame.image.load('Steal-the-Tool-main/assets/Background.png'),(0,0))

        # CC - Ah Render the game title text
        menu_text = get_font(100).render('STEAL THE TOOL', True, 'black')
        menu_rect = menu_text.get_rect(center = (width/2,height-600))

        # CC - Render the instructions text
        instructions_text = get_font(50).render('Press Space to Start', True, 'black')
        instructions_rect = instructions_text.get_rect(center = (width/2,height-120))

        # CC - Display the rendered text on the screen
        screen.blit(menu_text, menu_rect)
        screen.blit(instructions_text, instructions_rect)

        while run == True:
            # AH - Handle events (user input)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False # AH - Quit the game if the window close button is clicked
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        play() # AH - Call the play function if the Space key is pressed
                    if event.key == pygame.K_ESCAPE:
                        run = False # AH - Quit the game if the Escape key is pressed
            pygame.display.update() # AH - Update the display to show the changes
        pygame.quit()
        sys.exit()
main_menu() #Starts the game in the main menu
