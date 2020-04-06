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
pygame.display.update()  # to update changes here it is optional

# game specific variables
exit_game = False
game_over = False

snake_x = 45
snake_y = 55
snake_size = 10

fps = 30


clock = pygame.time.Clock()

while not exit_game:

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10

    gamewindow.fill(white)
    pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()  # to update changes
    clock.tick(fps)

pygame.quit()
quit()
