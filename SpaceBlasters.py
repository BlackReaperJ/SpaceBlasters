#Makes a SpaceBlasters Games
import pygame
import random

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
med_font = pygame.font.SysFont("comicsansms",45)#pygame.font.Font to use custom fonts .ttf
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
def button(text, x, y, width, height, inactive_color, active_color, action= None):
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
            elif action == "highscore":
                pass
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

#Creates a game_controls title page for the game
def game_controls():
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
        message_to_screen("Beat lvl 10 to win the game",blue,120,"medium")

        button_width = 150
        button_height = 75

        #Make Buttons, pygame does not have buttons
        button("Play", 12, 600, button_width, button_height,green, light_green, action = "play")
        button("Main", 187, 600, button_width, button_height, yellow, light_yellow, action = "main")
        button("High Scores", 362, 600, button_width, button_height, blue, light_blue,action = "highscore")
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
        button("High Scores", display_width/2 - 0.5* button_width, 445, button_width, button_height, blue, light_blue,action = "highscore")
        button("Quit", display_width/2 - 0.5* button_width, 555, button_width, button_height, red, light_red,action = "quit")

        pygame.display.update()
        clock.tick(15)#Frames per second, great graphics low fps, meh graphics high mid fps

#Game Over screen of the game
def gameover(score):
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
        message_to_screen("Your total score is: " + str(score),blue,0,"medium")
        message_to_screen("Enter your name:"+ str(name) + type, blue, 60, "medium")

        #Make Buttons, pygame does not have buttons
        button("Play Again", 12, 600, button_width, button_height,green, light_green, action = "play")
        button("Main", 187, 600, button_width, button_height, yellow, light_yellow, action = "main")
        button("Submit Score", 362, 600, button_width, button_height, blue, light_blue,action = "submit")
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

    for loc in enemies[1]:
        if player.colliderect(int(loc[0]-enemy_norm_width/2.5),int(loc[1]-enemy_norm_height/2.5),int(enemy_norm_width*0.8),int(enemy_norm_height*0.6)):
            player_hp = player_hp - 1
            score = score - 100
            enemies[1].remove(loc)

    for loc in enemies[2]:#Collision for easy_enemies
        if player.colliderect(int(loc[0]-enemy_easy_height/1.5),int(loc[1]-enemy_easy_height/1.5),int(enemy_easy_height*1.5),int(enemy_easy_height*1.5)):
            player_hp = player_hp - 1
            score = score - 100
            enemies[2].remove(loc)

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

#Draws the players laser shots
def fire(list):
    for loc in list:
        pygame.draw.rect(gameDisplay,blue,(loc[0]+ int(laser_width/2),loc[1]-50-laser_height,laser_width,laser_height))

#Players Laser Collision for enemy laser and enemies
def player_fire_collision(list_fire,enemies,score,enemy_list_fire):
    for fire in list_fire:#Player laser and Enemy Laser collision
        laser = pygame.draw.rect(gameDisplay,blue,(fire[0]+ int(laser_width/2),fire[1]-50-laser_height,laser_width,laser_height))
        for enemy_fire in enemy_list_fire:
            if laser.colliderect(enemy_fire[0],enemy_fire[1],laser_width,laser_height):
                list_fire.remove(fire)
                enemy_list_fire.remove(enemy_fire)
                break

    for fire in list_fire:#Player laser and Easy Enemy collision
        laser = pygame.draw.rect(gameDisplay,blue,(fire[0]+ int(laser_width/2),fire[1]-50-laser_height,laser_width,laser_height))
        for loc in enemies[0]:#Easy Enemies
            enemy = pygame.draw.circle(gameDisplay,black,(loc[0],loc[1]),enemy_easy_height)
            if enemy.colliderect(laser):
                list_fire.remove(fire)
                loc[2] = loc[2] - 1
                if loc[2] <= 0:
                    score =  score + 100
                    enemies[0].remove(loc)
                break#need to break if a laser overlaps with 2 enemies at the same location

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
                if loc[2] <= 0:
                    score =  score + 100
                    enemies[1].remove(loc)
                break

        for loc in enemies[2]:#Hard Enemies
            enemy = pygame.draw.circle(gameDisplay,black,(int(loc[0]),int(loc[1])),int(enemy_hard_height/2))
            if enemy.colliderect(laser):
                list_fire.remove(fire)
                loc[2] = loc[2] - 1
                if loc[2] <= 0:
                    score =  score + 100
                    enemies[2].remove(loc)
                break

    return score

#Draws the enemies lasers
def enemy_fires(enemy):
    for loc in enemy:
        pygame.draw.rect(gameDisplay,red,(loc[0],loc[1],laser_width,laser_height))

#Enemy laser collision for the player
def enemy_fire_collision(player,enemy_list_fire,player_hp):
    for fire in enemy_list_fire:
        laser = pygame.draw.rect(gameDisplay,red,(fire[0],fire[1],laser_width,laser_height))
        if player.colliderect(laser):
            player_hp = player_hp - 1
            enemy_list_fire.remove(fire)
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
            unique = "None"
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
            unique = "AI"
        elif level == 4:
            create_stage_hazard([[600,175]])

        if level != 4:
            text = med_font.render("New Enemy: ->", True, red)
            gameDisplay.blit(text, [150,140])
            message_to_screen("Enemy Statistics",blue,-100,"medium")
            text = med_font.render("Speed: " + speed, True, red)
            gameDisplay.blit(text, [100,290])
            text = med_font.render("Rate of Fire: "+rate, True, red)
            gameDisplay.blit(text, [100,360])
            text = med_font.render("Lives: " +str(lives), True, red)
            gameDisplay.blit(text, [100,430])
            text = med_font.render("Unique: " +str(unique), True, red)
            gameDisplay.blit(text, [100,500])
        else:
            text = med_font.render("New Stage Hazard: ->", True, red)
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
                list_fire.remove(fire)
                break

#Creates stage hazards for the game
def create_stage_hazard(black_hole):
    for loc in black_hole:
        part = black_hole_height#Radius Black Hole
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
    next_enemy = 0#Type of enemies 0-Easy, 1- Normal, 2-Hard

    easy_num = []#Level 1 enemies
    normal_num = []#Level 2 enemies
    hard_num = []#Level 3 enemies

    black_hole = []#Level 4 Stage Hazard
    num_black_hole = 0

    lives = [2,1,2]

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
        easy_num =   [1,0,1,1,1,2,1,2,1,2,1,1,2,2,1,2]
        normal_num = [0,1,1,1,2,1,1,2,2,1,2,1,2,1,2,2]
        hard_num =   [1,1,0,1,1,1,2,1,1,2,2,3,2,3,3,3]
        black_hole = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]

    enemy_waves.append(easy_num)
    enemy_waves.append(normal_num)
    enemy_waves.append(hard_num)

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
                random_enemy.append(location)#Add easy_enemy to list
                row_enemy.append(location)
                num_enemy = num_enemy + 1

            next_enemy = next_enemy + 1
        enemies.append(random_enemy)
    print(enemies)

    return enemies,num_black_hole

def level_create(easy_enemy,easy_vel,normal_enemy,normal_vel,hard_enemy,hard_vel,player_hp,delay):
    wave_complete = False
    if delay == 1:
            normal_vel = normal_vel + 1
            hard_vel = hard_vel + 1

    if easy_enemy != []:
        for loc in easy_enemy:
            loc[1] = loc[1] + easy_vel
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

    #if normal_enemies == []:
    #    print("nothing")
    if easy_enemy == [] and normal_enemy == [] and hard_enemy == []:
        wave_complete = True
    return player_hp, wave_complete

#Better to start the game from function
def game_loop():
    game_exit = False
    game_over = False
    FPS = 50

    score = 0

    player_hp = 10
    space_ship_x = display_width * 0.5
    space_ship_y = display_height * 0.99
    move_x = 0
    move_y = 0

    list_fire = []
    vel_shot = 5
    global laser_width,laser_height
    laser_width = 7#originally 5
    laser_height = 20

    level = 4
    display_level = True
    wave = 1
    create_wave = True
    waves_per_level = [15,16,16,16]
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
    normal_vel = 3#This is actually 3.5

    global enemy_hard_height
    enemy_hard_height = 64
    hard_rate_fire = 60
    hard_vel = 0.5

    num_black_hole = 0
    black_hole = []
    global black_hole_height
    black_hole_height = 20

    while not game_exit:
        for event in pygame.event.get():#print(event)
            if event.type == pygame.QUIT:#Checks if u click exit button
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    move_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    move_y = 0

            #When the key is pressed
            if event.type == pygame.KEYDOWN:#Moves object
                if event.key == pygame.K_LEFT:
                    move_x = -5
                elif event.key == pygame.K_RIGHT :
                    move_x = 5
                elif event.key == pygame.K_UP:
                    move_y = -5
                elif event.key == pygame.K_DOWN :
                    move_y = 5
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
            player_hp = 10
            list_fire = []
            move_x = 0
            move_y = 0
            level_display(level)
            display_level = False
            create_wave = True
            num_black_hole = 0

        if create_wave:
            enemies,num_black_hole = create_enemies(level,wave)
            wave += 1
            if wave == waves_per_level[level-1]:
                display_level = True
                level = level + 1

            black_hole = []
            for x in range(num_black_hole):
                print(num_black_hole, "hi")
                loc = []
                loc.append(random.randrange(0.05*display_width,0.92*display_width))
                loc.append(random.randrange(0.3*display_height,0.8*display_height))
                black_hole.append(loc)
            create_wave = False

        #Moves Spaceship
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
        create_stage_hazard(black_hole)

        fire(list_fire)
        score = player_fire_collision(list_fire,enemies,score,enemy_list_fire)

        # enemies: [0] = easy_enemies, [1] = normal_enemies
        # [][0] = xPos, [][1] = yPos, [][2] = life
        player_hp,create_wave = level_create(enemies[0],easy_vel,enemies[1],normal_vel,enemies[2],hard_vel,player_hp,delay)
        ai_move(enemies[2],list_fire)

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


        for loc in enemy_list_fire:
            loc[1] = loc[1] + easy_vel_shot
            if loc[1] > display_height:
                enemy_list_fire.remove(loc)

        enemy_fires(enemy_list_fire)
        player = space_ship(space_ship_x,space_ship_y)

        enemies, player_hp,score = player_collision(player,enemies,player_hp,score)
        player_hp = enemy_fire_collision(player,enemy_list_fire,player_hp)

        if player_hp <= 0:
            gameover(score)

        if score < 0:
            score = 0

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()#Uninitializes pygamer_change = +1
    quit()#quits phyton

game_intro()

