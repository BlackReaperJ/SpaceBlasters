#Makes a SpaceBlasters Games
import pygame
import random
from operator import itemgetter

pygame.init()#Initialize the modules in pygame

white = (255,255,255)#Have to create ur colours in python
light_black = (25,25,25)
black = (0,0,0)
light_black = (30,30,30)
grey = (50,50,50)
red = (200,0,0)#red,green,blue
dark_red = (174,0,0)
light_red = (255,0,0)
blue = (0,0,255)#red,green,blue
light_blue = (0,162,232)
lighter_dark_blue = (0,149,213)
light_dark_blue = (0,119,170)
violet = (53,0,106)
dark_violet = (46,0,91)
yellow = (200,200,0)
light_yellow = (255,255,0)
green = (34,177,76)
light_green = (0,255,0)
silver = (80,80,80)

pi = 3.141592653 #For arcs

display_width = 700
display_height = 700

gameDisplay = pygame.display.set_mode((display_width,display_height))#Create a frame 800 by 600
pygame.display.set_caption("Space Blasters")

button_width = 150
button_height = 75

clock = pygame.time.Clock()
FPS = 30

small_font = pygame.font.SysFont("comicsansms",25)#Type of font, Font size 25
med_font = pygame.font.SysFont("comicsansms",40)#pygame.font.Font to use custom fonts .ttf
medbig_font = pygame.font.SysFont("comicsansms",45)
large_font = pygame.font.SysFont("comicsansms",80)

#Creation of Stars
num_stars = 60
stars = []# A list of lists

for i in range(num_stars):
     location = []
     location.append(random.randrange(0.02 * display_width,0.98* display_width))
     location.append(random.randrange(0.02 * display_height, 0.98*display_height))
     stars.append(location)

#Draws the stars in the background
def game_stars():
    for loc in stars:
        loc[1] = (loc[1] + 1) % display_height
        pygame.draw.circle(gameDisplay,white,(loc[0],loc[1]),2)

#Creates the size of the text
def text_objects(text,color,size):#Use to center text
    if size == "small":
        text_surface = small_font.render(text, True, color)
    elif size == "medium":
        text_surface = med_font.render(text, True, color)
    elif size == "large":
        text_surface = large_font.render(text, True, color)
    return text_surface, text_surface.get_rect()#Returns the surface and rectangle of the surface

#Centers text on the button
def text_to_button(msg,color, button_x, button_y, button_width, button_height, size = "small"):
    text_surf, text_rect = text_objects(msg,color,size)
    #Formula to find formula oof center of button
    text_rect.center = button_x +(button_width /2), button_y + (button_height /2)
    gameDisplay.blit(text_surf, text_rect)

#Prints msg on screen
#y_displace for moving text up and down
def message_to_screen(msg,color, y_displace = 0, size = "small"):
    text_surf, text_rect = text_objects(msg,color, size)
    text_rect.center = (display_width/2), (display_height /2) + y_displace#Centers the text
    gameDisplay.blit(text_surf, text_rect)

#Creates a Button
def button(text, x, y, width, height, inactive_color, active_color, action= None, score = 0, names = ""):
    #3rd param(xLoc,yLoc,width,height)
    cur = pygame.mouse.get_pos()# gets x,y of mouse location in a tuple
    click = pygame.mouse.get_pressed()#Gets clicks of the mouse
    #print(click) #(left_click, wheel, right_click) in tuple
    if(cur[0] >= x and cur[0] <= (x+width) and cur[1] >= y and cur[1] <= (y+height)):
        pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":#Runs the button events
                pygame.quit()
                quit()
            elif action == "controls":
                game_controls()
            elif action == "submit":
                high_scores(score, names)
            elif action == "play":
                game_loop()
            elif action == "main":
                game_intro()
            elif action == "ready":
                return False
    else:
        pygame.draw.rect(gameDisplay,inactive_color,(x,y,width,height))

    text_to_button(text,black,x,y,width,height)
    return(True)

#Pause the game
def pause():
    paused = True

    message_to_screen("Paused",white,-100,size = "large")
    message_to_screen("Press C to continue or Q to quit!",white,25,size = "small")
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)

def high_scores(score = 0, name = " "):
    for i in range(2):
        clock.tick(15)

    game_score = True
    highscores = []

    while True:
        try:
            fr = open('HighScores.txt','r')#'r', read file
            text = fr.read()
            words = text.split()

            line = []
            i = 0
            for word in words:
                if i % 2 == 1:
                    line.append(int(word))
                    highscores.append(line)
                    line = []
                else:
                    line.append(word)
                i+=1
            fr.close()
            break
        except FileNotFoundError:
            highscores = [['Ace',250000],['Julius',200000],['Kirito',150000],['JPunisher',100000],['God',75000],
                          ['Jack',50000],['GreasyDeafGuy',25000],['Mrs.Schuli',10000],['Jason',7500],['Player1',5000]]
            break

    if len(highscores) != 10:
        highscores = [['Ace',250000],['Julius',200000],['Kirito',150000],['JPunisher',100000],['God',75000],
                      ['Jack',50000],['GreasyDeafGuy',25000],['Mrs.Schuli',10000],['Jason',7500],['Player1',5000]]

    highscores.append([name,score])
    #itemgetter orders the list
    highscores = sorted(highscores,key = itemgetter(1),reverse = True)

    fw = open("HighScores.txt", 'w')#open(), 1st param file name, 2nd param write,read
    for i in range(10):
        fw.write(highscores[i][0] + "                  " + str(highscores[i][1])+"\n")

    fw.close()

    while game_score:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        game_stars()
        message_to_screen("HighScores",blue,y_displace =-300,size = "large")

        for i in range(10):
            text = med_font.render(str(i+1) + ". " + highscores[i][0] , True, red)
            if i ==9:
              gameDisplay.blit(text,[32,i * 50 + 90])
            else:
                gameDisplay.blit(text,[50,i * 50 + 90])
            text = med_font.render(str(highscores[i][1]), True, red)
            gameDisplay.blit(text,[500,i * 50 + 90])

        button_width = 150
        button_height = 75

        #Make Buttons, pygame does not have buttons
        button("Play", 12, 600, button_width, button_height,green, light_green, action = "play")
        button("Main", 187, 600, button_width, button_height, yellow, light_yellow, action = "main")
        button("Controls", 362, 600, button_width, button_height, blue, light_blue,action = "controls")
        button("Quit", 537, 600, button_width, button_height, red, light_red,action = "quit")

        pygame.display.update()
        clock.tick(10)


#Creates a game_controls title page for the game
def game_controls():
    for i in range(2):
        clock.tick(15)

    game_cont = True
    while game_cont:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        game_stars()
        message_to_screen("Controls",light_red,y_displace =-275,size = "large")
        message_to_screen("Move SpaceShip: Arrow Keys",blue,-180,"medium")
        message_to_screen("Fire: Spacebar",blue,-120,"medium")
        message_to_screen("Pause: P",blue,-60,"medium")
        message_to_screen("Kill Enemies to Increase Score!",blue,0,"medium")
        message_to_screen("Hp Restored After Each Level",blue,60,"medium")
        message_to_screen("Beat level 6 to win the game",blue,120,"medium")

        button_width = 150
        button_height = 75

        #Make Buttons, pygame does not have buttons
        button("Play", 12, 600, button_width, button_height,green, light_green, action = "play")
        button("Main", 187, 600, button_width, button_height, yellow, light_yellow, action = "main")
        button("High Scores", 362, 600, button_width, button_height, blue, light_blue,action = "submit")
        button("Quit", 537, 600, button_width, button_height, red, light_red,action = "quit")

        pygame.display.update()
        clock.tick(10)

#The main menu for the game
def game_intro():
    for i in range(2):
        clock.tick(15)


    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        game_stars()
        message_to_screen("Space Blasters",blue,y_displace =-275,size = "large")

        #Make Buttons, pygame does not have buttons
        button("Play", display_width/2 - 0.5* button_width, 225, button_width, button_height,green, light_green, action = "play")
        button("Controls", display_width/2 - 0.5* button_width, 335, button_width, button_height, yellow, light_yellow, action = "controls")
        button("High Scores", display_width/2 - 0.5* button_width, 445, button_width, button_height, blue, light_blue,action = "submit")
        button("Quit", display_width/2 - 0.5* button_width, 555, button_width, button_height, red, light_red,action = "quit")

        pygame.display.update()
        clock.tick(15)#Frames per second, great graphics low fps, meh graphics high mid fps

#Win the Game Screen
def you_win(scores):
    game_win = True
    name = ""
    type = ""
    num = 1
    symbols = "!@#$%^&*():<>:?\/.,~\"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while game_win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_BACKSPACE and len(name) > 0:
                    name = name[:-1]
                elif event.key == pygame.K_SPACE:
                    name = name + " "
                elif pygame.key.name(event.key) in symbols:
                    name = name + pygame.key.name(event.key)

        num = num +1
        if num % 20 >= 10:
            type = "|"
        else:
            type = ""

        gameDisplay.fill(black)
        game_stars()
        message_to_screen("You Have Won!!",red,y_displace =-100,size = "large")
        message_to_screen("Your total score is: " + str(scores),blue,0,"medium")
        message_to_screen("Enter your name:"+ str(name) + type, blue, 60, "medium")

        #Make Buttons, pygame does not have buttons
        button("Play Again", 12, 600, button_width, button_height,green, light_green, action = "play")
        button("Main", 187, 600, button_width, button_height, yellow, light_yellow, action = "main")
        button("Submit Score", 362, 600, button_width, button_height, blue, light_blue,action = "submit", score = scores, names = name)
        button("Quit", 537, 600, button_width, button_height, red, light_red,action = "quit")

        pygame.display.update()
        clock.tick(20)

#Game Over screen of the game
def gameover(scores):
    game_over = True
    name = ""
    type = ""
    num = 1
    symbols = "!@#$%^&*():<>:?\/.,~\"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_BACKSPACE and len(name) > 0:
                    name = name[:-1]
                elif event.key == pygame.K_SPACE:
                    name = name + " "
                elif pygame.key.name(event.key) in symbols:
                    name = name + pygame.key.name(event.key)

        num = num +1
        if num % 20 >= 10:
            type = "|"
        else:
            type = ""

        gameDisplay.fill(black)
        game_stars()
        message_to_screen("Game Over!!",red,y_displace =-100,size = "large")
        message_to_screen("Your total score is: " + str(scores),blue,0,"medium")
        message_to_screen("Enter your name:"+ str(name) + type, blue, 60, "medium")

        #Make Buttons, pygame does not have buttons
        button("Play Again", 12, 600, button_width, button_height,green, light_green, action = "play")
        button("Main", 187, 600, button_width, button_height, yellow, light_yellow, action = "main")
        button("Submit Score", 362, 600, button_width, button_height, blue, light_blue,action = "submit",score = scores, names = name)
        button("Quit", 537, 600, button_width, button_height, red, light_red,action = "quit")

        pygame.display.update()
        clock.tick(20)#Frames per second, great graphics low fps, meh graphics high mid fps

#Creates the players space_ship
def space_ship(x,y):
    #Draws the body
    #1ST cor: head  3rd line: tail
    player = pygame.draw.polygon(gameDisplay,silver,((x+7,y-50),(x+1,y-37),(x-5,y-30),(x-5,y-28),(x+3,y-30),(x+3,y-20),
                                           (x-3,y-20),(x-23,y-2),(x-23,y+5),(x-10,y+5),(x-5,y),(x-3,y+5),(x+3,y+6),
                                           (x+7,y+13),(x+10,y+6),(x+15,y+5),(x+18,y),(x+23,y+5),(x+35,y+5),
                                           (x+35,y-3),(x+15,y-20),(x+10,y-20),(x+10,y-30),(x+18,y-28),(x+18,y-30),
                                           (x+12,y-38)))

    pygame.draw.polygon(gameDisplay,red,((x-6,y-9),(x-23,y+5),(x-10,y+5),(x-5,y)))#Left Wing
    pygame.draw.polygon(gameDisplay,red,((x+19,y-9),(x+35,y+5),(x+23,y+5),(x+18,y)))#Right Wing
    pygame.draw.circle(gameDisplay,grey,(int(x+7),int(y-34)),3)

    return player

#If the players ship collides with the enemies ship
def player_collision(player,enemies, player_hp,score):
    for loc in enemies[0]:#Collision for easy_enemies
        if player.colliderect(int(loc[0]-enemy_easy_height/1.5),int(loc[1]-enemy_easy_height/1.5),int(enemy_easy_height*1.5),int(enemy_easy_height*1.5)):
            player_hp = player_hp - 1
            score = score - 100
            enemies[0].remove(loc)

    for loc in enemies[1]:#Collision for norm_enemies
        if player.colliderect(int(loc[0]-enemy_norm_width/2.5),int(loc[1]-enemy_norm_height/2.5),int(enemy_norm_width*0.8),int(enemy_norm_height*0.6)):
            player_hp = player_hp - 1
            score = score - 100
            enemies[1].remove(loc)

    for loc in enemies[2]:#Collision for hard_enemies
        if player.colliderect(int(loc[0]-enemy_easy_height/1.5),int(loc[1]-enemy_easy_height/1.5),int(enemy_easy_height*1.5),int(enemy_easy_height*1.5)):
            player_hp = player_hp - 1
            score = score - 100
            enemies[2].remove(loc)

    for loc in enemies[3]:#Collision for hard_enemies
        if player.colliderect(int(loc[0]-enemy_beam_width*0.42),int(loc[1]-enemy_beam_height*0.42),int(enemy_beam_width*0.9),int(enemy_beam_height*0.9)):
            player_hp = player_hp - 1
            score = score - 100
            enemies[3].remove(loc)

    return enemies, player_hp,score

#Creates the easy enemies for the game
def easy_enemies(x,y,lives = 2):
    x = int(x)
    y = int(y)
    part = int(enemy_hard_height /2)#32 -> 16

    #Main Body
    pygame.draw.polygon(gameDisplay,light_dark_blue,((x-int(part *0.25),y+part),(x-int(part *0.5),y+part),(x-int(part *0.5),y-int(part *0.5)),(x+int(part *0.5),y-int(part *0.5)),(x+int(part *0.5),y+part),
                                                (x+int(part *0.25),y+part),(x+int(part *0.25),y-int(part*0.25)),(x-int(part *0.25),y-int(part*0.25))))

    #Top Left Tip
    pygame.draw.rect(gameDisplay,light_dark_blue,(x-int(part*0.3125),y - int(part*0.9375), int(part*0.25),int(part * 0.4375)))

    #Top Right Tip
    pygame.draw.rect(gameDisplay,light_dark_blue,(x+int(part*0.125),y - int(part*0.9375), int(part*0.25),int(part * 0.4375)))

    #Center top gray
    pygame.draw.rect(gameDisplay,light_black,(x-int(part*0.0625),y - int(part*0.25), int(part*0.1875),int(part * 0.0625)))

    #Center Left Gray
    pygame.draw.rect(gameDisplay,light_black,(x-int(part*0.1875),y - int(part*0.125), int(part*0.0625),int(part * 0.1875)))

    #Center Right Gray
    pygame.draw.rect(gameDisplay,light_black,(x+int(part*0.1875),y - int(part*0.125), int(part*0.0625),int(part * 0.1875)))

    #Center Head
    pygame.draw.rect(gameDisplay,light_black,(x-int(part*0.0625),y + int(part*0.125), int(part*0.1875),int(part * 0.4375)))


    if lives == 2:
        #Center
        pygame.draw.rect(gameDisplay,dark_red ,(x-int(part*0.125),y - int(part*0.1875), int(part*0.3125),int(part * 0.3125)))

        #Left Wing
        pygame.draw.polygon(gameDisplay,red,((x-int(part *0.555),y-int(part *0.5)),(x-int(part *0.6875),y-int(part *0.625)),(x-int(part *0.825),y-int(part *0.625)),(x- part,y-int(part *0.3125)),
                        (x- part,y+int(part *0.3125)),(x-int(part *0.75),y+int(part *0.875)),(x-int(part *0.6875),y+int(part *0.875)),(x-int(part *0.555),y+int(part *0.6875))))
        #Right Wing
        pygame.draw.polygon(gameDisplay,red,((x+int(part *0.56),y-int(part *0.5)),(x+int(part *0.6875),y-int(part *0.625)),(x+int(part *0.825),y-int(part *0.625)),(x+ part,y-int(part *0.3125)),
                        (x+ part,y+int(part *0.3125)),(x+int(part *0.75),y+int(part *0.875)),(x+int(part *0.6875),y+int(part *0.875)),(x+int(part *0.56),y+int(part *0.6875))))

    else:
        pygame.draw.rect(gameDisplay,blue ,(x-int(part*0.125),y - int(part*0.1875), int(part*0.3125),int(part * 0.3125)))
        pygame.draw.polygon(gameDisplay,blue,((x-int(part *0.555),y-int(part *0.5)),(x-int(part *0.6875),y-int(part *0.625)),(x-int(part *0.825),y-int(part *0.625)),(x- part,y-int(part *0.3125)),
                        (x- part,y+int(part *0.3125)),(x-int(part *0.75),y+int(part *0.875)),(x-int(part *0.6875),y+int(part *0.875)),(x-int(part *0.555),y+int(part *0.6875))))
        pygame.draw.polygon(gameDisplay,blue,((x+int(part *0.56),y-int(part *0.5)),(x+int(part *0.6875),y-int(part *0.625)),(x+int(part *0.825),y-int(part *0.625)),(x+ part,y-int(part *0.3125)),
                        (x+ part,y+int(part *0.3125)),(x+int(part *0.75),y+int(part *0.875)),(x+int(part *0.6875),y+int(part *0.875)),(x+int(part *0.56),y+int(part *0.6875))))


#Creates the normal enemies for the game
def normal_enemies(x,y,lives = 1):
    x = int(x)
    y = int(y)
    part_x = int(enemy_norm_width /2)#26 -> 13
    part_y = int(enemy_norm_height /2)#32 -> 16

    #Main Body
    pygame.draw.polygon(gameDisplay,silver,((x-2,y-part_y),(x+2,y-part_y),(x+int(part_x*0.384),y-int(part_y/2)),(x+int(part_x*0.6),y-part_y),
                        (x+ part_x,y - int(part_y/4 * 3)),(x+int(part_x*0.75),y + int(part_y * 0.3125)),(x+int(part_x*0.65),y + int(part_y * 0.3125)),(x+int(part_x*0.65),y - int(part_y * 0.525)),
                        (x+int(part_x*0.307),y + 2),(x+int(part_x*0.23),y + int(part_y * 0.8125)),(x+2,y + part_y),(x-2,y + part_y),#Tip
                        (x-int(part_x*0.23),y + int(part_y * 0.8125)),(x-int(part_x*0.307),y + 2),(x-int(part_x*0.65),y - int(part_y * 0.525)),(x-int(part_x*0.65),y + int(part_y * 0.3125)),(x-int(part_x*0.75),y + int(part_y * 0.3125)),
                        (x- part_x,y - int(part_y/4 * 3)),(x-int(part_x*0.6),y-part_y),(x-int(part_x*0.384),y-int(part_y/2))))

    #Right Flame
    pygame.draw.polygon(gameDisplay,blue,((x+int(part_x*0.615),y-int(part_y*0.38)),(x+int(part_x*0.615),y+int(part_y*0.0625)),(x+int(part_x*0.538),y+int(part_y*0.25)),
                        (x+int(part_x*0.3846),y+int(part_y*0.4375)),(x+int(part_x*0.3086),y+int(part_y*0.0625))))

    #Left Flane
    pygame.draw.polygon(gameDisplay,blue,((x-int(part_x*0.615),y-int(part_y*0.38)),(x-int(part_x*0.615),y+int(part_y*0.0625)),(x-int(part_x*0.538),y+int(part_y*0.25)),
                        (x-int(part_x*0.3846),y+int(part_y*0.4375)),(x-int(part_x*0.3086),y+int(part_y*0.0625))))

    #pod
    pygame.draw.circle(gameDisplay,light_blue,(x,y+int(part_y*0.7575)),int(part_x/7))

#Creates the hard enemies for the game
def hard_enemies(x,y, lives = 2):
    x = int(x)
    y = int(y)

    pygame.draw.circle(gameDisplay,violet,(x,y),enemy_easy_height)
    pygame.draw.circle(gameDisplay,black,(x,y),int(enemy_easy_height/1.5))
    pygame.draw.rect(gameDisplay,dark_violet,(int(x-enemy_easy_height/1.5),int(y-enemy_easy_height*0.15),int(enemy_easy_height/2.8),int(enemy_easy_height/2.8)))#Left square
    pygame.draw.rect(gameDisplay,dark_violet,(int(x+enemy_easy_height/3.1),int(y-enemy_easy_height*0.15),int(enemy_easy_height/2.8),int(enemy_easy_height/2.8)))#Eight square
    pygame.draw.rect(gameDisplay,dark_violet,(int(x-enemy_easy_height*0.15),int(y+enemy_easy_height/3.1),int(enemy_easy_height/2.8),int(enemy_easy_height/2.8)))#Bottom square
    pygame.draw.rect(gameDisplay,dark_violet,(int(x-enemy_easy_height*0.15),int(y-enemy_easy_height/1.5),int(enemy_easy_height/2.8),int(enemy_easy_height/2.8)))#Top Sqaure

    if lives == 1:
        pygame.draw.circle(gameDisplay,blue,(x,y),int(enemy_easy_height/2.5))
    else:
        pygame.draw.circle(gameDisplay,red,(x,y),int(enemy_easy_height/2.5))

def beam_enemies(x,y,lives = 3,fire_time = 0):
    x = int(x)
    y = int(y)
    partx = int(enemy_beam_width /2)#16->8
    party = int(enemy_beam_height /2)#32->16

    #Left Engine Flames
    pygame.draw.polygon(gameDisplay,blue,((x-int(partx*0.5),y-int(party*0.625)),(x-int(partx*0.375),y-int(party*0.75)),(x-int(partx*0.375),y-int(party*0.8125)),
                        (x-int(partx*0.5),y-int(party*0.9375)),(x-int(partx*0.625),y-int(party*0.8125)),(x-int(partx*0.625),y-int(party*0.75))))

    #Right Engine Flames
    pygame.draw.polygon(gameDisplay,blue,((x+int(partx*0.5),y-int(party*0.625)),(x+int(partx*0.375),y-int(party*0.75)),(x+int(partx*0.375),y-int(party*0.8125)),
                        (x+int(partx*0.5),y-int(party*0.9375)),(x+int(partx*0.625),y-int(party*0.8125)),(x+int(partx*0.625),y-int(party*0.75))))

    pygame.draw.polygon(gameDisplay,violet,((x-int(partx*0.125),y+int(party*0.125)),(x-int(partx*0.625),(y+int(party*0.4375))),(x,int(y+party)),(x+int(partx*0.125),int(y+party)),(x+int(partx*0.625),(y+int(party*0.4375))),(x+int(partx*0.125),y+int(party*0.125)),
                                            (x+int(partx*0.25),y+int(party*0.125)),(x+int(partx*0.5),y+int(party*0.1875)),(x+int(partx*0.75),y+int(party*0.0625)),(x+int(partx*0.875),y-int(party*0.0625)),(x+int(partx*0.875),y-int(party*0.4375)),(x+int(partx*0.75),y-int(party*0.5625)),#Top Right Red
                                            (x+int(partx*0.375),y-int(party*0.5625)),(x+int(partx*0.5),y-int(party*0.6875)),(x+int(partx*0.25),y-int(party*0.6875)),(x+int(partx*0.25),y-int(party*0.875)),(x+int(partx*0.125),y-int(party*0.9375)),#reflection
                                            (x-int(partx*0.125),y-int(party*0.9375)),(x-int(partx*0.25),y-int(party*0.875)),(x-int(partx*0.25),y-int(party*0.6875)),(x-int(partx*0.5),y-int(party*0.6875)),(x-int(partx*0.375),y-int(party*0.5625)),(x-int(partx*0.75),y-int(party*0.5625)),
                                            (x-int(partx*0.875),y-int(party*0.4375)),(x-int(partx*0.875),y-int(party*0.0625)),(x-int(partx*0.75),y+int(party*0.0625)),(x-int(partx*0.5),y+int(party*0.1875)),(x-int(partx*0.25),y+int(party*0.125))))
    #Arrow
    pygame.draw.polygon(gameDisplay,light_black,((x-int(partx*0.125),y+int(party*0.125)),(x-int(partx*0.625),(y+int(party*0.4375))),(x,int(y+party)),(x+int(partx*0.125),int(y+party)),(x+int(partx*0.625),(y+int(party*0.4375))),(x+int(partx*0.125),y+int(party*0.125))))

    pygame.draw.rect(gameDisplay,light_black,((x-int(partx*0.125),y-int(party*0.75),int(partx*0.375),int(party*0.75))))

    beam_color = dark_red
    if lives == 2:
        beam_color = light_blue
    elif lives == 1:
        beam_color = blue

    #Left Right Red Lines
    pygame.draw.line(gameDisplay, beam_color, (x+int(partx*0.125),y), (x+int(partx*0.375),y+int(party*0.1875)), int(party*0.125))
    pygame.draw.line(gameDisplay, beam_color, (x-int(partx*0.125),y), (x-int(partx*0.375),y+int(party*0.1875)), int(party*0.125))

    #Beam Firing
    if fire_time >= 1:
        pygame.draw.line(gameDisplay, beam_color, (x+int(partx*0.125),y), (x+int(partx*0.625),y+int(party*0.4325)), int(party*0.125))
        pygame.draw.line(gameDisplay, beam_color, (x-int(partx*0.125),y), (x-int(partx*0.625),y+int(party*0.4325)), int(party*0.125))

    if fire_time == 2:
        pygame.draw.line(gameDisplay, beam_color, (x+int(partx*0.625),y+int(party*0.4325)), (x+int(partx*0.375),y+int(party*0.75)), int(party*0.125))
        pygame.draw.line(gameDisplay, beam_color, (x-int(partx*0.625),y+int(party*0.4325)), (x-int(partx*0.375),y+int(party*0.75)), int(party*0.125))

    if fire_time == 3:
        pygame.draw.line(gameDisplay, beam_color, (x+int(partx*0.625),y+int(party*0.4325)), (x+int(partx*0),y+int(party)), int(party*0.125))
        pygame.draw.line(gameDisplay, beam_color, (x-int(partx*0.625),y+int(party*0.4325)), (x-int(partx*0),y+int(party)), int(party*0.125))

def create_boss(boss_enemy,lives = 100,fire_time = 0):
    x = int(boss_enemy[0])
    y = int(boss_enemy[1])
    partx = int(enemy_boss_width /2)#16->8
    party = int(enemy_boss_height /2)#32->16

    #Main Body
    pygame.draw.polygon(gameDisplay,light_black,((x-int(partx*2.375),y+int(party*0.125)),(x-int(partx*2.625),y+int(party*0.125)),(x-int(partx*3.125),(y+int(party*0.4375))),(x-int(partx*2.5),int(y+party)),(x-int(partx*2.375),int(y+party)),(x-int(partx*1.875),(y+int(party*0.4375))),#Left Arrow
                                                (x-int(partx*0.875),y+int(party*0.5625)),(x,y+int(party*0.9375)),(x+int(partx*0.875),y+int(party*0.5625)),
                                                (x+int(partx*1.875),(y+int(party*0.4375))),(x+int(partx*2.5),int(y+party)),(x+int(partx*2.625),int(y+party)),(x+int(partx*3.125),(y+int(party*0.4375))),(x+int(partx*2.625),y+int(party*0.125)),(x+int(partx*2.375),y+int(party*0.125))))

    #Middle Arrow
    #pygame.draw.polygon(gameDisplay,light_blue,((x-int(partx*0.125),y+int(party*0.125)),(x-int(partx*0.625),(y+int(party*0.4375))),(x,int(y+party)),(x+int(partx*0.125),int(y+party)),(x+int(partx*0.625),(y+int(party*0.4375))),(x+int(partx*0.125),y+int(party*0.125))))
    #Left Arrow
    pygame.draw.polygon(gameDisplay,light_black,((x-int(partx*2.625),y+int(party*0.125)),(x-int(partx*3.125),(y+int(party*0.4375))),(x-int(partx*2.5),int(y+party)),(x-int(partx*2.375),int(y+party)),(x-int(partx*1.875),(y+int(party*0.4375))),(x-int(partx*2.375),y+int(party*0.125))))
    #Right Arrow
    pygame.draw.polygon(gameDisplay,light_black,((x+int(partx*2.375),y+int(party*0.125)),(x+int(partx*1.875),(y+int(party*0.4375))),(x+int(partx*2.5),int(y+party)),(x+int(partx*2.625),int(y+party)),(x+int(partx*3.125),(y+int(party*0.4375))),(x+int(partx*2.625),y+int(party*0.125))))

    #Left Eye
    pygame.draw.polygon(gameDisplay,dark_red,((x-int(partx*0.375),y+int(party*0.625)),(x-int(partx*0.25),y+int(party*0.75)),(x-int(partx*0.25),y+int(party*0.8125)),
                        (x-int(partx*0.375),y+int(party*0.9375)),(x-int(partx*0.5),y+int(party*0.8125)),(x-int(partx*0.5),y+int(party*0.75))))

    #Right Eye
    pygame.draw.polygon(gameDisplay,dark_red,((x+int(partx*0.375),y+int(party*0.625)),(x+int(partx*0.25),y+int(party*0.75)),(x+int(partx*0.25),y+int(party*0.8125)),
                        (x+int(partx*0.375),y+int(party*0.9375)),(x+int(partx*0.5),y+int(party*0.8125)),(x+int(partx*0.5),y+int(party*0.75))))

    #Left Laser Head
    pygame.draw.rect(gameDisplay,light_black,(x-int(partx*1.375),y + int(party*0.125), int(partx*0.1875),int(party * 0.625)))
    pygame.draw.rect(gameDisplay,light_black,(x+int(partx*1.375),y + int(party*0.125), int(partx*0.1875),int(party * 0.625)))

#Moves Boss and Displays Life of Boss
def boss_stuff(boss_enemy,x):
    if x < boss_enemy[0]:
        boss_enemy[0] = boss_enemy[0] -2
    elif x > boss_enemy[0]:
        boss_enemy[0] = boss_enemy[0] + 2

    if boss_enemy[2] >= 50:
        pygame.draw.rect(gameDisplay,green,(650,15,15,int(boss_enemy[2]*3.65)))
    elif boss_enemy[2] >= 25:
        pygame.draw.rect(gameDisplay,yellow,(650,15,15,int(boss_enemy[2]*3.65)))
    else:
        pygame.draw.rect(gameDisplay,dark_red,(650,15,15,int(boss_enemy[2]*3.65)))

#Draws the players laser shots
def fire(list):
    for loc in list:
        pygame.draw.rect(gameDisplay,blue,(loc[0]+ int(laser_width/2),loc[1]-50-laser_height,laser_width,laser_height))

#Players Laser Collision for enemy laser and enemies
def player_fire_collision(list_fire,enemies,score,enemy_list_fire,boss,boss_enemy):
    for fire in list_fire:#Player laser and Enemy Laser collision
        laser = pygame.draw.rect(gameDisplay,blue,(fire[0]+ int(laser_width/2),fire[1]-50-laser_height,laser_width,laser_height))
        for enemy_fire in enemy_list_fire:
            if laser.colliderect(enemy_fire[0],enemy_fire[1],laser_width,laser_height):
                list_fire.remove(fire)
                enemy_list_fire.remove(enemy_fire)
                break

    for fire in list_fire:#Player laser and Easy Enemy collision
        laser = pygame.draw.rect(gameDisplay,blue,(fire[0]+ int(laser_width/2),fire[1]-50-laser_height,laser_width,laser_height))
        i = len(enemies[0])
        for loc in enemies[0]:#Easy Enemies
            enemy = pygame.draw.circle(gameDisplay,black,(loc[0],loc[1]),enemy_easy_height)
            if enemy.colliderect(laser):
                list_fire.remove(fire)
                loc[2] = loc[2] - 1
                score =  score + 100
                if loc[2] <= 0:
                    enemies[0].remove(loc)
                break#need to break if a laser overlaps with 2 enemies at the same location

        if i > len(enemies[0]):
            continue

        i = len(enemies[1])
        for loc in enemies[1]:#Norm Enemies
            part_x = int(enemy_norm_width /2)
            part_y = int(enemy_norm_height/2)
            enemy = pygame.draw.polygon(gameDisplay,silver,((loc[0]-2,loc[1]-part_y),(loc[0]+2,loc[1]-part_y),(loc[0]+int(part_x*0.384),loc[1]-int(part_y/2)),(loc[0]+int(part_x*0.6),loc[1]-part_y),
                        (loc[0]+ part_x,loc[1] - int(part_y/4 * 3)),(loc[0]+int(part_x*0.75),loc[1] + int(part_y * 0.3125)),(loc[0]+int(part_x*0.65),loc[1] + int(part_y * 0.3125)),(loc[0]+int(part_x*0.65),loc[1] - int(part_y * 0.525)),
                        (loc[0]+int(part_x*0.307),loc[1] + 2),(loc[0]+int(part_x*0.23),loc[1] + int(part_y * 0.8125)),(loc[0]+2,loc[1] + part_y),(loc[0]-2,loc[1] + part_y),#Tip
                        (loc[0]-int(part_x*0.23),loc[1] + int(part_y * 0.8125)),(loc[0]-int(part_x*0.307),loc[1] + 2),(loc[0]-int(part_x*0.65),loc[1] - int(part_y * 0.525)),(loc[0]-int(part_x*0.65),loc[1] + int(part_y * 0.3125)),
                        (loc[0]-int(part_x*0.75),loc[1] + int(part_y * 0.3125)),(loc[0]- part_x,loc[1] - int(part_y/4 * 3)),(loc[0]-int(part_x*0.6),loc[1]-part_y),(loc[0]-int(part_x*0.384),loc[1]-int(part_y/2))))
            if enemy.colliderect(laser):
                list_fire.remove(fire)
                loc[2] = loc[2] - 1
                score =  score + 100
                if loc[2] <= 0:
                    enemies[1].remove(loc)
                break

        if i > len(enemies[1]):
            continue

        i = len(enemies[2])
        for loc in enemies[2]:#Hard Enemies
            enemy = pygame.draw.circle(gameDisplay,black,(int(loc[0]),int(loc[1])),int(enemy_hard_height/2))
            if enemy.colliderect(laser):
                list_fire.remove(fire)
                loc[2] = loc[2] - 1
                score =  score + 100
                if loc[2] <= 0:
                    enemies[2].remove(loc)
                break

        if i > len(enemies[2]):
            continue

        i = len(enemies[3])
        for loc in enemies[3]:
            partx = int(enemy_beam_width /2)
            party = int(enemy_beam_height/2)
            enemy = pygame.draw.polygon(gameDisplay,violet,((loc[0]-int(partx*0.125),loc[1]+int(party*0.125)),(loc[0]-int(partx*0.625),(loc[1]+int(party*0.4375))),(loc[0],int(loc[1]+party)),(loc[0]+int(partx*0.125),int(loc[1]+party)),(loc[0]+int(partx*0.625),(loc[1]+int(party*0.4375))),(loc[0]+int(partx*0.125),loc[1]+int(party*0.125)),
                                            (loc[0]+int(partx*0.25),loc[1]+int(party*0.125)),(loc[0]+int(partx*0.5),loc[1]+int(party*0.1875)),(loc[0]+int(partx*0.75),loc[1]+int(party*0.0625)),(loc[0]+int(partx*0.875),loc[1]-int(party*0.0625)),(loc[0]+int(partx*0.875),loc[1]-int(party*0.4375)),(loc[0]+int(partx*0.75),loc[1]-int(party*0.5625)),#Top Right Red
                                            (loc[0]+int(partx*0.375),loc[1]-int(party*0.5625)),(loc[0]+int(partx*0.5),loc[1]-int(party*0.6875)),(loc[0]+int(partx*0.25),loc[1]-int(party*0.6875)),(loc[0]+int(partx*0.25),loc[1]-int(party*0.875)),(loc[0]+int(partx*0.125),loc[1]-int(party*0.9375)),#reflection
                                            (loc[0]-int(partx*0.125),loc[1]-int(party*0.9375)),(loc[0]-int(partx*0.25),loc[1]-int(party*0.875)),(loc[0]-int(partx*0.25),loc[1]-int(party*0.6875)),(loc[0]-int(partx*0.5),loc[1]-int(party*0.6875)),(loc[0]-int(partx*0.375),loc[1]-int(party*0.5625)),(loc[0]-int(partx*0.75),loc[1]-int(party*0.5625)),
                                            (loc[0]-int(partx*0.875),loc[1]-int(party*0.4375)),(loc[0]-int(partx*0.875),loc[1]-int(party*0.0625)),(loc[0]-int(partx*0.75),loc[1]+int(party*0.0625)),(loc[0]-int(partx*0.5),loc[1]+int(party*0.1875)),(loc[0]-int(partx*0.25),loc[1]+int(party*0.125))))
            if enemy.colliderect(laser):
                list_fire.remove(fire)
                loc[2] = loc[2] - 1
                score =  score + 100
                if loc[2] <= 0:
                    enemies[3].remove(loc)
                break

        if i > len(enemies[3]):
            continue

        if boss == True:

            print(boss_enemy)
            x = int(boss_enemy[0])
            y = int(boss_enemy[1])
            partx = int(enemy_boss_width/2)
            party = int(enemy_boss_height/2)
            enemy = pygame.draw.polygon(gameDisplay,light_black,((x-int(partx*2.375),y+int(party*0.125)),(x-int(partx*2.625),y+int(party*0.125)),(x-int(partx*3.125),(y+int(party*0.4375))),(x-int(partx*2.5),int(y+party)),(x-int(partx*2.375),int(y+party)),(x-int(partx*1.875),(y+int(party*0.4375))),#Left Arrow
                                                (x-int(partx*0.875),y+int(party*0.5625)),(x,y+int(party*0.9375)),(x+int(partx*0.875),y+int(party*0.5625)),
                                                (x+int(partx*1.875),(y+int(party*0.4375))),(x+int(partx*2.5),int(y+party)),(x+int(partx*2.625),int(y+party)),(x+int(partx*3.125),(y+int(party*0.4375))),(x+int(partx*2.625),y+int(party*0.125)),(x+int(partx*2.375),y+int(party*0.125))))
            if enemy.colliderect(laser):
                list_fire.remove(fire)
                boss_enemy[2] = boss_enemy[2] - 1
                score =  score + 100
                if boss_enemy[2] <= 0:
                    you_win(score)
                break

    return score

#Draws the enemies lasers
def enemy_fires(enemy):
    for loc in enemy:
        pygame.draw.rect(gameDisplay,red,(loc[0],loc[1],laser_width,laser_height))

#Enemy laser collision for the player
def enemy_fire_collision(x,y,enemy_list_fire,player_hp):
    for fire in enemy_list_fire:
        laser = pygame.draw.rect(gameDisplay,red,(fire[0],fire[1],laser_width,laser_height))
        tip = pygame.draw.polygon(gameDisplay,light_black,((x+7,y-50),(x+1,y-37),(x-5,y-30),(x-5,y-28),(x+3,y-30),(x+10,y-30),(x+18,y-28),(x+18,y-30),(x+12,y-38)))
        body = pygame.draw.rect(gameDisplay,light_black,((x-3),(y-20),20,26))
        left_wing = pygame.draw.rect(gameDisplay,light_black,((x-22),(y-3),20,9))
        left_wing_up = pygame.draw.rect(gameDisplay,light_black,((x-14),(y-10),14,7))
        right_wing = pygame.draw.rect(gameDisplay,light_black,((x+15),(y-3),20,9))
        right_wing_up = pygame.draw.rect(gameDisplay,light_black,((x+14),(y-10),14,7))

        if tip.colliderect(laser) or body.colliderect(laser) or right_wing.colliderect(laser) or right_wing_up.colliderect(laser) or left_wing.colliderect(laser) or left_wing_up.colliderect(laser):
            player_hp = player_hp - 1
            enemy_list_fire.remove(fire)

    return player_hp

#Draws the beam lasers and destorys player lasers and ship
def beam_fires(x,y,beam_enemy,list_fire,player_hp,boss,boss_enemy,boss_beam):

    tip = pygame.draw.polygon(gameDisplay,light_black,((x+7,y-50),(x+1,y-37),(x-5,y-30),(x-5,y-28),(x+3,y-30),(x+10,y-30),(x+18,y-28),(x+18,y-30),(x+12,y-38)))
    body = pygame.draw.rect(gameDisplay,light_black,((x-3),(y-20),20,26))
    left_wing = pygame.draw.rect(gameDisplay,light_black,((x-22),(y-3),20,9))
    left_wing_up = pygame.draw.rect(gameDisplay,light_black,((x-14),(y-10),14,7))
    right_wing = pygame.draw.rect(gameDisplay,light_black,((x+15),(y-3),20,9))
    right_wing_up = pygame.draw.rect(gameDisplay,light_black,((x+14),(y-10),14,7))

    for loc in beam_enemy:
        if loc[3] == 3:
            beam = pygame.draw.rect(gameDisplay,light_yellow,(loc[0] - int(beam_width * 0.5),loc[1]+int(enemy_beam_height*0.5),beam_width,int(loc[4] * beam_height)))
            loc[4] = loc[4] + 1

            if loc[1] + int(loc[4] * beam_height) > display_height:
                loc[3] = 0
                loc[4] = 1

            if tip.colliderect(beam) or body.colliderect(beam) or left_wing.colliderect(beam) or left_wing_up.colliderect(beam) or right_wing.colliderect(beam) or right_wing_up.colliderect(beam):
                player_hp = player_hp - 1
                loc[3] = 0
                loc[4] = 1

            for fire in list_fire:
                laser = pygame.draw.rect(gameDisplay,blue,(fire[0]+ int(laser_width/2),fire[1]-50-laser_height,laser_width,laser_height))
                if laser.colliderect(beam):
                    list_fire.remove(fire)

    if boss == True:
        if boss_beam[0][0] == 3:
            beam = pygame.draw.rect(gameDisplay,light_yellow,(boss_enemy[0] - int(beam_width * 0.5),boss_enemy[1]+int(enemy_beam_height*0.5),beam_width,int(boss_beam[0][1] * beam_height)))
            boss_beam[0][1] = boss_beam[0][1] + 1

            if boss_enemy[1] + int(boss_beam[0][1] * beam_height) > display_height:
                boss_beam[0][0] = 0
                boss_beam[0][1] = 1

            if tip.colliderect(beam) or body.colliderect(beam) or left_wing.colliderect(beam) or left_wing_up.colliderect(beam) or right_wing.colliderect(beam) or right_wing_up.colliderect(beam):
                player_hp = player_hp - 1
                boss_beam[0][0] = 0
                boss_beam[0][1] = 1

            for fire in list_fire:
                laser = pygame.draw.rect(gameDisplay,blue,(fire[0]+ int(laser_width/2),fire[1]-50-laser_height,laser_width,laser_height))
                if laser.colliderect(beam):
                    list_fire.remove(fire)

        if boss_beam[1][0] == 3:
            beam = pygame.draw.rect(gameDisplay,light_yellow,(boss_enemy[0] - int(beam_width * 2.6),boss_enemy[1]+int(enemy_beam_height*0.5),int(beam_width*0.4),int(boss_beam[1][1] * beam_height)))
            beam2 = pygame.draw.rect(gameDisplay,light_yellow,(boss_enemy[0] + int(beam_width * 2.6),boss_enemy[1]+int(enemy_beam_height*0.5),int(beam_width*0.4),int(boss_beam[1][1] * beam_height)))

            boss_beam[1][1] = boss_beam[1][1] + 1.5

            if boss_enemy[1] + int(boss_beam[1][1] * beam_height) > display_height:
                boss_beam[1][0] = 0
                boss_beam[1][1] = 1

            if tip.colliderect(beam) or body.colliderect(beam) or left_wing.colliderect(beam) or left_wing_up.colliderect(beam) or right_wing.colliderect(beam) or right_wing_up.colliderect(beam) or tip.colliderect(beam2) or body.colliderect(beam) or left_wing.colliderect(beam2) or left_wing_up.colliderect(beam2) or right_wing.colliderect(beam2) or right_wing_up.colliderect(beam2):
                player_hp = player_hp - 1
                boss_beam[1][0] = 0
                boss_beam[1][1] = 1

            for fire in list_fire:
                laser = pygame.draw.rect(gameDisplay,blue,(fire[0]+ int(laser_width/2),fire[1]-50-laser_height,laser_width,laser_height))
                if laser.colliderect(beam) or laser.colliderect(beam2):
                    list_fire.remove(fire)

        if boss_beam[2][0] == 3:
            beam = pygame.draw.rect(gameDisplay,light_yellow,(boss_enemy[0] - int(beam_width * 5.1),boss_enemy[1]+int(enemy_beam_height*0.5),int(beam_width),int(boss_beam[2][1] * beam_height)))
            beam2 = pygame.draw.rect(gameDisplay,light_yellow,(boss_enemy[0] + int(beam_width * 4.4),boss_enemy[1]+int(enemy_beam_height*0.5),int(beam_width),int(boss_beam[2][1] * beam_height)))

            boss_beam[2][1] = boss_beam[2][1] + 0.7

            if boss_enemy[1] + int(boss_beam[2][1] * beam_height) > display_height:
                boss_beam[2][2] = boss_beam[2][2] + 1

            if boss_beam[2][2] == 250:
                boss_beam[2][0] = 0
                boss_beam[2][1] = 1
                boss_beam[2][2] = 0

            if tip.colliderect(beam) or body.colliderect(beam) or left_wing.colliderect(beam) or left_wing_up.colliderect(beam) or right_wing.colliderect(beam) or right_wing_up.colliderect(beam) or tip.colliderect(beam2) or body.colliderect(beam) or left_wing.colliderect(beam2) or left_wing_up.colliderect(beam2) or right_wing.colliderect(beam2) or right_wing_up.colliderect(beam2):
                player_hp = player_hp - 1
                boss_beam[2][0] = 0
                boss_beam[2][1] = 1

            for fire in list_fire:
                laser = pygame.draw.rect(gameDisplay,blue,(fire[0]+ int(laser_width/2),fire[1]-50-laser_height,laser_width,laser_height))
                if laser.colliderect(beam) or laser.colliderect(beam2):
                    list_fire.remove(fire)

    return player_hp

def ai_move(hard_enemy,list_fire):
    for fire in list_fire:
        for enemy in hard_enemy:
            if enemy[0] + enemy_hard_height > fire[0] > enemy[0] - enemy_hard_height and enemy[1] + 200 > fire[1]:
                if enemy[0] < 0.05 * display_width:
                    enemy[0] = enemy[0] + 5
                elif enemy[0] > 0.92 * display_width:
                    enemy[0] = enemy[0] - 5
                elif fire[0] > enemy[0]:
                    enemy[0] = enemy[0] - 5
                elif fire[0] < enemy[0]:
                    enemy[0] = enemy[0] + 5

#Draws the hp bar
def health_bar(hp):
    for i in range(hp):
        pygame.draw.rect(gameDisplay,light_blue,(display_width-20,25*(i)+15 ,15,15))

#Displays the score on the screen
def display_score(score):
    text = small_font.render("Score: " + str(score), True, white)
    gameDisplay.blit(text, [0,0])

#Tje description of the level before the level begins
def level_display(level):
    display_level = True
    speed = ""
    rate = ""
    unique = ""
    lives = 0

    while display_level:

        for event in pygame.event.get():#print(event)
                if event.type == pygame.QUIT:#Checks if u click exit button
                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        game_stars()

        message_to_screen("Level " + str(level),blue,-290,"large")

        if level == 1:
            easy_enemies(505, 175)
            speed = "Slow"
            rate = "Normal"
            lives = 2
            unique = "Speed Doubles When Hit"
        elif level == 2:
            normal_enemies(505, 175)
            speed = "Fast"
            rate = "None"
            lives = 1
            unique = "Can't Shoot"
        elif level == 3:
            hard_enemies(505, 175)
            speed = "Very Slow"
            rate = "Normal"
            lives = 2
            unique = "AI Movement"
        elif level == 4:
            create_stage_hazard([[600,175]])
            create_stage_hazard([[203,500]])
            create_stage_hazard([[303,500]])
            pygame.draw.rect(gameDisplay,blue,(200,535,laser_width,laser_height))
            text = med_font.render("->", True, red)
            gameDisplay.blit(text, [235,470])
        elif level == 5:
            beam_enemies(505, 175)
            speed = "Very Slow"
            rate = "Fast"
            lives = 3
            unique = "Fires Beam Lasers"

        if level != 4 and level != 6:
            text = medbig_font.render("New Enemy: ->", True, red)
            gameDisplay.blit(text, [150,140])
            message_to_screen("Enemy Statistics",blue,-100,"medium")
            text = med_font.render("Speed: " + speed, True, red)
            gameDisplay.blit(text, [50,290])
            text = med_font.render("Rate of Fire: "+rate, True, red)
            gameDisplay.blit(text, [50,360])
            text = med_font.render("Lives: " +str(lives), True, red)
            gameDisplay.blit(text, [50,430])
            text = med_font.render("Unique: " +str(unique), True, red)
            gameDisplay.blit(text, [50,500])
        elif level == 6:
            text = medbig_font.render("Boss Approaches", True, red)
            gameDisplay.blit(text, [150,140])
            message_to_screen("Enemy Statistics",blue,-100,"medium")
            text = med_font.render("Moves Left and Right" + speed, True, red)
            gameDisplay.blit(text, [150,290])
            text = med_font.render("Shoots Beams and Lasers"+rate, True, red)
            gameDisplay.blit(text, [150,360])
            text = med_font.render("Has 100 Lives"+rate, True, red)
            gameDisplay.blit(text, [150,430])
            text = med_font.render("Good Luck" +str(unique), True, red)
            gameDisplay.blit(text, [150,500])
        else:
            text = medbig_font .render("New Stage Hazard: ->", True, red)
            gameDisplay.blit(text, [100,140])
            message_to_screen("Black Hole Effects",blue,-100,"medium")
            text = med_font.render("Lasers are destroyed" + speed, True, red)
            gameDisplay.blit(text, [100,290])
            text = med_font.render("by Black Holes " + speed, True, red)
            gameDisplay.blit(text, [100,360])

        display_level = button("Ready",300,600,button_width,button_height,blue,light_blue,"ready")
        pygame.display.update()
        clock.tick(30)

#Destroys any laser that intersect at  black holes
def black_hole_destroy(black_hole,list_fire):
    for fire in list_fire:
        laser = pygame.draw.rect(gameDisplay,blue,(fire[0]+ int(laser_width/2),fire[1]-50-laser_height,laser_width,laser_height))
        for black in black_hole:
            black_holes = pygame.draw.circle(gameDisplay,dark_red,(black[0],black[1]),black_hole_height)
            if black_holes.colliderect(laser):
                '''
                if fire[0] <= black[0]:
                    fire[0] = fire[0] - 5
                else:
                    fire[0] = fire[0] + 5
                '''
                list_fire.remove(fire)
                break

#Creates stage hazards for the game
def create_stage_hazard(black_hole,list_fire,boss):
    for loc in black_hole:
        part = black_hole_height#Radius Black Hole
        if boss == True:
            for fire in list_fire:

                if fire[1] >= loc[1] and fire[0] < loc[0]:
                    loc[0] = loc[0] -2
                    break
                elif fire[1] >= loc[1] and fire[0] > loc[0]:
                    loc[0] = loc[0] +2
                    break
                '''
                elif fire[1] < loc[1]:
                    loc[1] = loc[1] -2
                '''

        x = loc[0]
        y = loc[1]
        pygame.draw.circle(gameDisplay,dark_red,(x,y),black_hole_height)
        pygame.draw.circle(gameDisplay,black,(x,y),int(black_hole_height/2))
        pygame.draw.circle(gameDisplay,dark_red,(x,y),int(black_hole_height/2) -1)
        pygame.draw.polygon(gameDisplay,black,((x+int(part*0.6875),y-int(part*0.8125)),(x+int(part*0.5625),y-int(part*0.6875)),(x+int(part*0.0625),y-int(part*0.375)),(x- int(part*0.125),y-int(part*0.0625)),#Top Right Thorn to Top left Corner
                                                (x- int(part*0.4325),y-int(part*0.1875)),(x- int(part*0.625),y-int(part*0.5)),(x- int(part*0.8125),y-int(part*0.6875)),#Top Left Corner to Top Left Thorn
                                                (x- int(part*0.6875),y-int(part*0.5625)),(x- int(part*0.375),y-int(part*0.0625)),(x- int(part*0.0625),y+ int(part*0.125)),#Top Left Thorn to Bottom Left Corner
                                                (x- int(part*0.1875),y+int(part*0.4325)),(x- int(part*0.5),y+int(part*0.625)),(x- int(part*0.6875),y+int(part*0.8125)),#Bottom Left Corner to Bottom Left Thorn
                                                (x- int(part*0.5625),y+int(part*0.6875)),(x- int(part*0.0625),y+int(part*0.375)),(x+ int(part*0.125),y- int(part*0.0625)),#Bottom Left Thorn to Bottom Right Corner
                                                (x+ int(part*0.4325),y+int(part*0.1875)),(x+ int(part*0.625),y+int(part*0.5)),(x+ int(part*0.8125),y+int(part*0.6875)),#Bottom Right Corner to Bottom Right Thorn
                                                (x+ int(part*0.6875),y+int(part*0.5625)),(x+ int(part*0.375),y+int(part*0.0625)),(x+ int(part*0.0625),y- int(part*0.125)),#Bottom Right Thorn to Top Right Corner
                                                (x+ int(part*0.1875),y-int(part*0.4325)),(x+ int(part*0.5),y-int(part*0.625))))
        pygame.draw.circle(gameDisplay,red,(x,y),int(black_hole_height*0.0625/2))

#Creates the enemies per waves per level
def create_enemies(level, wave):
    enemy_waves = []
    enemies = []
    num_enemy = 0#Total Number of enemies
    next_enemy = 0#Type of enemies 0-Easy, 1- Normal, 2-Hard, 3-Beam

    easy_num = []#Level 1 enemies
    normal_num = []#Level 2 enemies
    hard_num = []#Level 3 enemies
    beam_num = []#Level 5 enemies

    black_hole = []#Level 4 Stage Hazard
    num_black_hole = 0

    boss = False
    boss_enemy = []

    lives = [2,1,2,3]

    if level == 1:
        easy_num = [1,2,2,3,3,3,4,4,4,5,5,5,6,6,7]#Number of enemies per wave
    elif level == 2:
        easy_num =   [0,1,0,2,3,2,0,3,4,1,2,5,3,4,6,5]
        normal_num = [1,1,2,1,1,2,3,2,2,3,3,2,3,3,2,3]
    elif level == 3:
        easy_num =   [0,1,0,0,1,1,0,0,1,2,1,1,2,2,1,2]
        normal_num = [0,0,1,0,1,0,1,0,2,1,2,1,2,1,2,2]
        hard_num =   [1,1,1,2,1,2,2,3,1,2,2,3,2,3,3,3]
    elif level == 4:
        easy_num =   [1,1,0,1,0,2,1,1,2,0,3,1,2,2,1,2]
        normal_num = [0,1,2,1,1,1,2,1,3,2,0,1,1,2,2,2]
        hard_num =   [1,1,1,1,2,1,1,2,0,3,2,3,2,1,2,2]
        black_hole = [7,7,7,8,8,8,9,9,9,10,10,10,11,11,11,12]
    elif level == 5:
        easy_num =   [0,1,1,0,1,1,0,1,1,2,1,1,2,2,1,2]
        normal_num = [1,0,0,1,1,0,1,0,2,1,2,1,2,2,2,1]
        hard_num =   [0,1,1,1,1,1,1,2,1,2,2,2,1,1,2,2]
        black_hole = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8]
        beam_num =   [1,1,1,1,1,2,2,1,2,2,1,2,2,2,2,3]
    elif level == 6:
        boss = True

    enemy_waves.append(easy_num)
    enemy_waves.append(normal_num)
    enemy_waves.append(hard_num)
    enemy_waves.append(beam_num)

    if black_hole != []:
        num_black_hole = black_hole[wave]

    row_enemy = []

    for x in range(len(enemy_waves)):
        random_enemy = []

        if len(enemy_waves[x]) != 0:
            for y in range(enemy_waves[x][wave-1]):#Creates Easy Enemies per wave
                x_loc = random.randrange(display_width * 0.05, display_width * 0.92)
                y_loc = int(-20 - 100 * int(num_enemy /3))

                if num_enemy % 3 == 1:
                    while row_enemy[-1][0] + 0.15 * display_width > x_loc > row_enemy[-1][0] - 0.15 * display_width:
                        x_loc = random.randrange(display_width * 0.05, display_width * 0.92)

                if num_enemy % 3 == 2:
                    while row_enemy[-1][0] + 0.15 * display_width > x_loc > row_enemy[-1][0] - 0.15 * display_width or row_enemy[-2][0] + 0.15 * display_width > x_loc > row_enemy[-2][0] - 0.15 * display_width:
                        x_loc = random.randrange(display_width * 0.05, display_width * 0.92)

                location = []
                location.append(x_loc)
                location.append(y_loc)
                location.append(lives[next_enemy])#Have to change this when adding normal_minions
                if next_enemy == 3:#Beam Enemies
                    location.append(1)
                else:
                    location.append(0)
                location.append(1)#Height of Beam
                random_enemy.append(location)#Add easy_enemy to list
                row_enemy.append(location)
                num_enemy = num_enemy + 1

            next_enemy = next_enemy + 1#
        enemies.append(random_enemy)

    if boss == True:
        x_loc = int(display_width /2)
        y_loc = int(0)
        boss_enemy.append(x_loc)
        boss_enemy.append(y_loc)
        boss_enemy.append(100)
        boss_enemy.append(1)
        boss_enemy.append(1)

    print(enemies)
    print(boss_enemy)
    return enemies,num_black_hole,boss,boss_enemy

#Draws the enemies and moves the enemies
def level_create(easy_enemy,easy_vel,normal_enemy,normal_vel,hard_enemy,hard_vel,beam_enemy,beam_vel,player_hp,delay,boss_enemy):
    wave_complete = False
    if delay == 1:
            normal_vel = normal_vel + 1
            hard_vel = hard_vel + 1
            beam_vel = beam_vel + 1

    if easy_enemy != []:
        for loc in easy_enemy:
            if loc[2] == 1:
                vel = easy_vel * 2

            else:
                vel = easy_vel
            loc[1] = loc[1] + vel
            if loc[1] > display_height:
                easy_enemy.remove(loc)
                player_hp = player_hp -1#Losses life if spaceship gets past the end
                continue
            easy_enemies(loc[0],loc[1],loc[2])

    if normal_enemy != []:
        for loc in normal_enemy:
            loc[1] = loc[1] + normal_vel
            if loc[1] > display_height:
                normal_enemy.remove(loc)
                player_hp = player_hp -1#Losses life if spaceship gets past the end
                continue
            normal_enemies(loc[0],loc[1],loc[2])

    if hard_enemy != []:
        for loc in hard_enemy:
            loc[1] = loc[1] + hard_vel
            if loc[1] > display_height:
                hard_enemy.remove(loc)
                player_hp = player_hp -1#Losses life if spaceship gets past the end
                continue
            hard_enemies(loc[0],loc[1],loc[2])

    if beam_enemy != []:
        for loc in beam_enemy:
            loc[1] = loc[1] + beam_vel
            if loc[1] > display_height:
                beam_enemy.remove(loc)
                player_hp = player_hp -1#Losses life if spaceship gets past the end
                continue
            beam_enemies(loc[0],loc[1],loc[2],loc[3])

    #if normal_enemies == []:
    #    print("nothing")
    if easy_enemy == [] and normal_enemy == [] and hard_enemy == [] and beam_enemy == [] and boss_enemy == []:
        wave_complete = True
    return player_hp, wave_complete

#Better to start the game from function
def game_loop():
    game_exit = False
    game_over = False
    FPS = 50

    score = 0

    player_hp = 15
    space_ship_x = display_width * 0.5
    space_ship_y = display_height * 0.99
    move_x = 0
    move_y = 0

    #stupid commenting system
    key_right = False
    key_left = False
    key_up = False
    key_down = False

    list_fire = []
    vel_shot = 5
    beam_fire = []
    beam_shot = 20#Speed of the beam

    global laser_width,laser_height
    laser_width = 7#originally 5
    laser_height = 20

    global beam_width
    global beam_height
    beam_width = 17
    beam_height = 20#Speed of the shot

    level = 6
    display_level = True
    wave = 1
    create_wave = True
    waves_per_level = [15,16,16,16,16,1]
    enemies = [] # [0] = easy_enemies, [1] = normal_enemies

    enemy_fire = 0
    enemy_list_fire = []
    delay = 0 #for 0.5 vel shots

    global enemy_easy_height
    enemy_easy_height = 32
    easy_rate_fire = 50
    easy_vel = 1
    easy_vel_shot = 5

    global enemy_norm_height
    global enemy_norm_width
    enemy_norm_height = 64
    enemy_norm_width = 52
    normal_vel = 3

    global enemy_hard_height
    enemy_hard_height = 64
    hard_rate_fire = 60
    hard_vel = 0#This is actually 0.5

    num_black_hole = 0
    black_hole = []
    global black_hole_height
    black_hole_height = 20

    global enemy_beam_height
    global enemy_beam_width

    enemy_beam_width = 32
    enemy_beam_height = 64
    beam_vel = 0#This is actually 0.5
    beam_rate_fire = 50

    boss = False
    boss_enemy = []
    global enemy_boss_height
    global enemy_boss_width
    enemy_boss_width = 64
    enemy_boss_height = 128
    boss_rate_fire = 25
    boss_beam_main = 50
    boss_beam_small = 75
    boss_beam_wing = 125
    boss_beam = [[0,0],[0,0],[0,0,0]]#0 - main, 1- small, 2- wing

    while not game_exit:
        for event in pygame.event.get():#print(event)
            if event.type == pygame.QUIT:#Checks if u click exit button
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    key_left = False
                elif event.key == pygame.K_RIGHT:
                    key_right = False
                elif event.key == pygame.K_UP:
                    key_up = False
                elif event.key == pygame.K_DOWN:
                    key_down = False

            #When the key is pressed
            if event.type == pygame.KEYDOWN:#Moves object
                if event.key == pygame.K_LEFT:
                    key_left = True
                elif event.key == pygame.K_RIGHT :
                    key_right = True
                elif event.key == pygame.K_UP:
                    key_up = True
                elif event.key == pygame.K_DOWN :
                    key_down = True
                elif event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_SPACE :#Fires lasers
                    loc_fire = []
                    loc_fire.append(space_ship_x)
                    loc_fire.append(space_ship_y)
                    list_fire.append(loc_fire)

        gameDisplay.fill(black)

        if display_level:
            wave = 1
            player_hp = 15
            list_fire = []
            move_x = 0
            move_y = 0
            level_display(level)
            display_level = False
            create_wave = True
            num_black_hole = 0

        if create_wave:
            enemies,num_black_hole,boss,boss_enemy = create_enemies(level,wave)
            wave += 1
            if wave == waves_per_level[level-1]:
                display_level = True
                level = level + 1

            black_hole = []
            for x in range(num_black_hole):
                loc = []
                x_loc = random.randrange(0.05*display_width,0.92*display_width)
                y_loc = random.randrange(0.3*display_height,0.8*display_height)
                if len(black_hole)>2:
                    while black_hole[-1][0] + 0.15 * display_width > x_loc > black_hole[-1][0] - 0.15 * display_width or black_hole[-2][0] + 0.15 * display_width > x_loc > black_hole[-2][0] - 0.15 * display_width or black_hole[-1][1] + 0.1 * display_width > y_loc > black_hole[-1][1] - 0.1 * display_width or black_hole[-2][1] + 0.1 * display_width > y_loc > black_hole[-2][1] - 0.10 * display_width:
                            x_loc = random.randrange(display_width * 0.05, display_width * 0.92)
                            y_loc = random.randrange(0.3*display_height,0.8*display_height)
                loc.append(x_loc)
                loc.append(y_loc)
                black_hole.append(loc)

            if boss == True:
                loc = []
                x_loc = random.randrange(0.05*display_width,0.92*display_width)
                y_loc = int(display_height*0.5)
                loc.append(x_loc)
                loc.append(y_loc)
                black_hole.append(loc)
            create_wave = False



        #Moves Spaceship
        move_x = -5 if key_left else 5 if key_right else 0
        move_y = -5 if key_up else 5 if key_down else 0
        space_ship_x += move_x
        space_ship_y += move_y

        enemy_fire = (enemy_fire + 1) % 1000
        delay = (delay + 1) % 2

        #Boundaries for x-direction
        if space_ship_x - display_width * 0.03 < 0:
            space_ship_x = display_width * 0.03
        elif space_ship_x + display_width * 0.045> display_width:
            space_ship_x = display_width * 0.955

        #Boundaries for y-direction
        if space_ship_y > display_height * 0.99:
            space_ship_y = display_height * 0.99
        elif space_ship_y - display_height * 0.07 <0:
            space_ship_y = display_height * 0.07

        for loc in list_fire:
            loc[1] = loc[1] - vel_shot
            if loc[1] < 75:
                list_fire.remove(loc)

        game_stars()
        display_score(score)
        health_bar(player_hp)
        black_hole_destroy(black_hole,list_fire)
        create_stage_hazard(black_hole,list_fire,boss)

        fire(list_fire)
        score = player_fire_collision(list_fire,enemies,score,enemy_list_fire,boss,boss_enemy)
        player_hp = enemy_fire_collision(space_ship_x,space_ship_y,enemy_list_fire,player_hp)
        player_hp = beam_fires(space_ship_x,space_ship_y,enemies[3],list_fire,player_hp,boss,boss_enemy,boss_beam)

        # enemies: [0] = easy_enemies, [1] = normal_enemies, [2] = hard_enemies
        # [3] = beam_enemies, [4] = boss
        # [][0] = xPos, [][1] = yPos, [][2] = life
        player_hp,create_wave = level_create(enemies[0],easy_vel,enemies[1],normal_vel,enemies[2],hard_vel,enemies[3],beam_vel,player_hp,delay,boss_enemy)
        ai_move(enemies[2],list_fire)

        if boss == True:
            create_boss(boss_enemy)
            boss_stuff(boss_enemy,space_ship_x)

        if enemy_fire % easy_rate_fire == 0:#Firing for easy enemies
            for loc in enemies[0]:
                if loc[1] > 0:
                    loc_fire = []
                    loc_fire.append(loc[0])
                    loc_fire.append(loc[1])
                    enemy_list_fire.append(loc_fire)

        if enemy_fire % hard_rate_fire == 0:#Firing for normal enemies
            for loc in enemies[2]:
                if loc[1] > 0:
                    loc_fire = []
                    loc_fire.append(loc[0])
                    loc_fire.append(loc[1])
                    enemy_list_fire.append(loc_fire)

        if enemy_fire % beam_rate_fire == 20:
            for loc in enemies[3]:
                if loc[3] != 3:
                    loc[3] = (loc[3] + 1) % 4

        if enemy_fire % boss_rate_fire == 0 and boss == True:#Firing for Boss enemies
                loc_fire = []
                loc_fire.append(random.randrange(int(boss_enemy[0]-enemy_boss_width*1.5),int(boss_enemy[0]+enemy_boss_width*1.5)))
                loc_fire.append(boss_enemy[1]+30)
                enemy_list_fire.append(loc_fire)

        if enemy_fire % boss_beam_main == 0 and boss == True:
                if boss_beam[0][0] != 3:
                    boss_beam[0][0] = (boss_beam[0][0] + 1) % 4

        if enemy_fire % boss_beam_small == 0 and boss == True:
                if boss_beam[1][0] != 3:
                    boss_beam[1][0] = (boss_beam[1][0] + 1) % 4

        if enemy_fire % boss_beam_wing == 0 and boss == True:
                if boss_beam[2][0] != 3:
                    boss_beam[2][0] = (boss_beam[2][0] + 1) % 4

        for loc in enemy_list_fire:
            loc[1] = loc[1] + easy_vel_shot
            if loc[1] > display_height:
                enemy_list_fire.remove(loc)

        enemy_fires(enemy_list_fire)
        player = space_ship(space_ship_x,space_ship_y)

        enemies, player_hp,score = player_collision(player,enemies,player_hp,score)

        if player_hp <= 0:
            gameover(score)

        if score < 0:
            score = 0

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()#Uninitializes pygamer_change = +1
    quit()#quits phyton

game_intro()

