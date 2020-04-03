import pygame
pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 600

gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("snake with harry")
pygame.display.update()  # to update changes

# game specific variables
exit_game = False
game_over = False

while not exit_game:

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            exit_game = True

    gamewindow.fill(white)
    pygame.display.update()  # to update changes

pygame.quit()
quit()
