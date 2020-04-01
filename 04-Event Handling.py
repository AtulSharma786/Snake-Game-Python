import pygame
pygame.init()

# creating window
gamewindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("my first game")

# game specific variables
exit_game = False
game_over = False

# creating a game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()
