#Makes a SpaceBlasters Games
import pygame
import random

pygame.init()#Initialize the modules in pygame

white = (255,255,255)#Have to create ur colours in python
black = (0,0,0)
light_black = (30,30,30)
grey = (50,50,50)
red = (200,0,0)#red,green,blue
light_red = (255,0,0)
blue = (0,0,255)#red,green,blue
light_blue = (0,162,232)
violet = (53,0,106)
dark_violet = (46,0,91)
yellow = (200,200,0)
light_yellow = (255,255,0)
green = (34,177,76)
light_green = (0,255,0)

display_width = 700
display_height = 700

gameDisplay = pygame.display.set_mode((display_width,display_height))#Create a frame 800 by 600
pygame.display.set_caption("Space Blasters")

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
    else:
        pygame.draw.rect(gameDisplay,inactive_color,(x,y,width,height))

    text_to_button(text,black,x,y,width,height)

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
        message_to_screen("Move SpaceShip: Arrow Keys",blue,-80,"medium")
        message_to_screen("Fire: Spacebar",blue,-20,"medium")
        message_to_screen("Pause: P",blue,40,"medium")
        message_to_screen("Kill Enemies to increase score!",blue,100,"medium")
        message_to_screen("Beat lvl 10 to win the game",blue,160,"medium")

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

        button_width = 150
        button_height = 75

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

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        game_stars()
        message_to_screen("Game Over!!",red,y_displace =-100,size = "large")
        message_to_screen("Your total score is: " + str(score),blue,0,"medium")


        button_width = 150
        button_height = 75

        #Make Buttons, pygame does not have buttons
        button("Play Again", 12, 600, button_width, button_height,green, light_green, action = "play")
        button("Main", 187, 600, button_width, button_height, yellow, light_yellow, action = "main")
        button("High Scores", 362, 600, button_width, button_height, blue, light_blue,action = "highscore")
        button("Quit", 537, 600, button_width, button_height, red, light_red,action = "quit")

        pygame.display.update()
        clock.tick(15)#Frames per second, great graphics low fps, meh graphics high mid fps

#Creates the players space_ship
def space_ship(x,y):
    #Draws the body
    #1ST cor: head  3rd line: tail
    player = pygame.draw.polygon(gameDisplay,light_black,((x+7,y-50),(x+1,y-37),(x-5,y-30),(x-5,y-28),(x+3,y-30),(x+3,y-20),
                                           (x-3,y-20),(x-23,y-2),(x-23,y+5),(x-10,y+5),(x-5,y),(x-3,y+5),(x+3,y+6),
                                           (x+7,y+13),(x+10,y+6),(x+15,y+5),(x+18,y),(x+23,y+5),(x+35,y+5),
                                           (x+35,y-3),(x+15,y-20),(x+10,y-20),(x+10,y-30),(x+18,y-28),(x+18,y-30),
                                           (x+12,y-38)))

    pygame.draw.polygon(gameDisplay,red,((x-6,y-9),(x-23,y+5),(x-10,y+5),(x-5,y)))#Left Wing
    pygame.draw.polygon(gameDisplay,red,((x+19,y-9),(x+35,y+5),(x+23,y+5),(x+18,y)))#Right Wing
    pygame.draw.circle(gameDisplay,grey,(int(x+7),int(y-34)),3)

    return player

#If the players ship collides with the enemies ship
def player_collision(player,enemies, player_hp):
    for loc in enemies[0]:#Collision for easy_enemies
        if player.colliderect(int(loc[0]-enemy_easy_height),int(loc[1]-enemy_easy_height),enemy_easy_height*2,enemy_easy_height*2):
            player_hp = player_hp - 1
            enemies[0].remove(loc)

    return enemies, player_hp

#Creates the easy enemies for the game
def easy_enemies(x,y, lives):
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
        pygame.draw.rect(gameDisplay,blue,(loc[0] + laser_width,loc[1]-50-laser_height,laser_width,laser_height))

#Players Laser Collision for enemy laser and enemies
def player_fire_collision(list_fire,enemies,score,enemy_list_fire):
    for fire in list_fire:
        laser = pygame.draw.rect(gameDisplay,blue,(fire[0] + laser_width,fire[1]-50-laser_height,laser_width,laser_height))
        for enemy_fire in enemy_list_fire:
            if laser.colliderect(enemy_fire[0],enemy_fire[1],laser_width,laser_height):
                list_fire.remove(fire)
                enemy_list_fire.remove(enemy_fire)
                break

    for fire in list_fire:
        for loc in enemies[0]:#Easy Enemies
            laser = pygame.draw.rect(gameDisplay,blue,(fire[0] + laser_width,fire[1]-50-laser_height,laser_width,laser_height))
            if laser.colliderect(int(loc[0]-enemy_easy_height),int(loc[1]-enemy_easy_height),enemy_easy_height*2,enemy_easy_height*2):
                list_fire.remove(fire)
                loc[2] = loc[2] - 1
                if loc[2] <= 0:
                    score =  score + 100
                    enemies[0].remove(loc)
                break#need to break if a laser overlaps with 2 enemies at the same location

    return score

#Draws the enemies lasers
def enemy_fires(enemy):
    for loc in enemy:
        pygame.draw.rect(gameDisplay,red,(loc[0],loc[1],laser_width,laser_height))

#Enemy laser collision for the player and reduces hp of player if true
def enemy_fire_collision(player,enemy_list_fire,player_hp):
    for fire in enemy_list_fire:
        laser = pygame.draw.rect(gameDisplay,red,(fire[0],fire[1],laser_width,laser_height))
        if player.colliderect(laser):
            player_hp = player_hp - 1
            enemy_list_fire.remove(fire)
    return player_hp

#Draws the hp bar
def health_bar(hp):
    for i in range(hp):
        pygame.draw.rect(gameDisplay,light_blue,(display_width-20,25*(i)+15 ,15,15))

#Displays the score on the screen
def display_score(score):
    text = small_font.render("Score: " + str(score), True, white)
    gameDisplay.blit(text, [0,0])

#Creates the enemies per waves per level
def create_enemies(level, wave):
    easy_enemies = []
    normal_enemies = []
    enemy_waves = []
    enemies = []
    num_enemies = 1
    waves = 0

    easy_num = []
    normal_num = []

    easy_lives = 2

    if level == 1:
        easy_num = [1,1,1,2,2,2,2,2,3,3]

    enemy_waves.append(easy_num)
    enemy_waves.append(normal_num)

    for x in range(len(enemy_waves)):
        random_enemy = []
        if len(enemy_waves[x]) != 0:
            for y in range(enemy_waves[x][wave-1]):#Creates Easy Enemies per wave
                x_loc = random.randrange(display_width * 0.05, display_width * 0.92)
                y_loc = -20
                location = []
                location.append(x_loc)
                location.append(y_loc)
                location.append(easy_lives)#Have to change this when adding normal_minions
                random_enemy.append(location)#Add easy_enemy to list

        enemies.append(random_enemy)

    print(enemies)
    print(enemies[1])
    '''
    for x in range(5):
        location = []
        location.append(x)
        location.append(x)
        normal_enemies.append(location)
    enemies.append(normal_enemies)

    for x in enemies[1]:
        print(x[0],x[1])
    '''
    return enemies

def level_create(easy_enemy,easy_vel,normal_enemy,normal_vel,player_hp):
    wave_complete = False

    if easy_enemy != []:
        for loc in easy_enemy:
            loc[1] = loc[1] + easy_vel
            if loc[1] > display_height:
                easy_enemy.remove(loc)
                player_hp = player_hp -1#Losses life if spaceship gets past the end
                continue
            easy_enemies(loc[0],loc[1],loc[2])

    #if normal_enemies == []:
    #    print("nothing")
    if easy_enemy == [] and normal_enemy == []:
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

    level = 1
    wave = 1
    create_wave = True
    enemies = [] # [0] = easy_enemies, [1] = normal_enemies
    easy_vel = 1
    normal_vel = 2
    enemy_fire = 0
    enemy_list_fire = []

    global enemy_easy_height
    easy_enemy_fire = 50
    enemy_easy_height = 32
    easy_vel_shot = 5

    while not game_exit:
        gameDisplay.fill(black)
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
                if event.key == pygame.K_SPACE :#Fires lasers
                    loc_fire = []
                    loc_fire.append(space_ship_x)
                    loc_fire.append(space_ship_y)
                    list_fire.append(loc_fire)

        if create_wave:
            enemies = create_enemies(level,wave)
            wave += 1
            if wave == 11:
                wave = 1
            create_wave = False


        #Moves Spaceship
        space_ship_x += move_x
        space_ship_y += move_y

        enemy_fire = (enemy_fire + 1) % 1000

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

        # enemies: [0] = easy_enemies, [1] = normal_enemies
        # [][0] = xPos, [][1] = yPos, [][2] = life
        player_hp,create_wave = level_create(enemies[0],easy_vel,enemies[1],normal_vel,player_hp)

        fire(list_fire)
        score = player_fire_collision(list_fire,enemies,score,enemy_list_fire)

        if enemy_fire % easy_enemy_fire == 0:#Firing for easy enemies
            for loc in enemies[0]:
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

        enemies, player_hp = player_collision(player,enemies,player_hp)
        player_hp = enemy_fire_collision(player,enemy_list_fire,player_hp)

        if player_hp <= 0:
            gameover(score)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()#Uninitializes pygamer_change = +1
    quit()#quits phyton

game_intro()

