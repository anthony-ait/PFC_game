import pygame
import button



pygame.init()




#game window
screen_width = 1000
screen_height = 768



#define fonts
font = pygame.font.SysFont('MinimalPixel2', 40)

#define color
backgrd_color = (52, 69, 94)
text_color = (255, 255, 255)

#define screen

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Menu principal')





#load images
#main menu image
img = pygame.image.load('img/Background/game.png').convert_alpha()
backgrd_game_img = pygame.transform.scale(img, (img.get_width() * 0.75, img.get_height() * 0.75))
#background image
img = pygame.image.load('img/Background/home.png').convert_alpha()
backgrd_home_img = pygame.transform.scale(img, (img.get_width() * (screen_width/370), img.get_height() * (screen_height/330)))

#buttons image
menu_button = pygame.image.load('img/Button/Normal.png').convert_alpha()





#function for drawing background
#home home background
def draw_backgrd_home():
    screen.blit(backgrd_home_img, (0, 0))
    #draw button
#game background
def draw_backgrd_game():
    screen.blit(backgrd_game_img, (116, 0))

#create function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



#create buttons
menu_new_game_button = button.Button(screen, (screen_width - 270)/2, 300, menu_button, 270, 64)
menu_load_button = button.Button(screen, (screen_width - 270)/2, 400, menu_button, 270, 64)



def home_menu():
    run = True

    while run:
        #draw background
        draw_backgrd_home()

        #launch game if button clicked
        if menu_new_game_button.draw():
            game()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()

def game():
    run = True

    while run:

        #draw background
        screen.fill(backgrd_color)
        pygame.display.set_caption('Jeu')
        draw_backgrd_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()


home_menu()