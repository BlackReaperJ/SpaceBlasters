#Lesson for Pseudo 3D
#Makes a basic snake game
import pygame
import random

pygame.init()#Initialize the modules in pygame

white = (255,255,255)#Have to create ur colours in python
black = (0,0,0)
light_black = (30,30,30)
red = (200,0,0)#red,green,blue
light_red = (255,0,0)
blue = (0,0,255)#red,green,blue
light_blue = (0,162,232)
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

def game_stars():
    for loc in stars:
        loc[1] = (loc[1] + 1) % display_height
        pygame.draw.circle(gameDisplay,white,(loc[0],loc[1]),2)

def text_objects(text,color,size):#Use to center text
    if size == "small":
        text_surface = small_font.render(text, True, color)
    elif size == "medium":
        text_surface = med_font.render(text, True, color)
    elif size == "large":
        text_surface = large_font.render(text, True, color)
    return text_surface, text_surface.get_rect()#Returns the surface and rectangle of the surface


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

def space_ship(x,y):
    #Draws the body
    #1ST cor: head  3rd line: tail
    pygame.draw.polygon(gameDisplay,light_black,((x+6,y-50),(x+1,y-37),(x-5,y-30),(x-5,y-28),(x+3,y-30),(x+3,y-20),
                                           (x-3,y-20),(x-23,y-2),(x-23,y+5),(x-10,y+5),(x-5,y),(x-3,y+5),(x+3,y+6),
                                           (x+6,y+13),(x+10,y+6),(x+15,y+5),(x+18,y),(x+23,y+5),(x+35,y+5),
                                           (x+35,y-3),(x+15,y-20),(x+10,y-20),(x+10,y-30),(x+18,y-28),(x+18,y-30),
                                           (x+12,y-38)))

    pygame.draw.polygon(gameDisplay,red,((x-6,y-9),(x-23,y+5),(x-10,y+5),(x-5,y)))#Left Wing
    pygame.draw.polygon(gameDisplay,red,((x+19,y-9),(x+35,y+5),(x+23,y+5),(x+18,y)))#Right Wing



#Better to start the game from function
def game_loop():
    game_exit = False
    game_over = False
    FPS = 20

    player_lives = 3
    space_ship_x = display_width * 0.5
    space_ship_y = display_height * 0.98
    move_x = 0
    move_y = 0

    while not game_exit:

        for event in pygame.event.get():#print(event)
            if event.type == pygame.QUIT:#Checks if u click exit button
                pygame.quit()
                quit()

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

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    move_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    move_y = 0

        space_ship_x += move_x
        space_ship_y += move_y

        if space_ship_x - display_width * 0.03 < 0:
            space_ship_x = display_width * 0.03
        elif space_ship_x + display_width * 0.045> display_width:
            space_ship_x = display_width * 0.955

        if space_ship_y > display_height * 0.98:
            space_ship_y = display_height * 0.98

        gameDisplay.fill(black)
        game_stars()

        space_ship(space_ship_x,space_ship_y)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()#Uninitializes pygamer_change = +1
    quit()#quits phyton

game_intro()

