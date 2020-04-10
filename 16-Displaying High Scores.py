import pygame
import random
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

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])


def plot_snake(gamewindow, black, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gamewindow, black, [x, y, snake_size, snake_size])


def game_loop():
    # game specific variables
    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55
    snake_size = 10

    fps = 30
    score = 0

    # velocity
    velocity = 7
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(10, screen_width / 2)
    food_y = random.randint(10, screen_height / 2)

    snake_list = []
    snake_length = 1

    # for high score
    with open("high score.txt", "r") as f:
        high_score = f.read()

    # game loop
    while not exit_game:

        if game_over:
            with open("high score.txt", "w") as f:
                f.write(str(high_score))

            gamewindow.fill(white)
            text_screen("Game Over! Press enter to continue", red, 100, 300)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            for event in pygame.event.get():
                # print(event)

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        velocity_x = velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -velocity

                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = velocity

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                snake_length += 5
                food_x = random.randint(10, screen_width / 2)
                food_y = random.randint(10, screen_height / 2)

                if score > int(high_score):
                    high_score = score

            gamewindow.fill(white)

            text_screen("Score: " + str(score)+"  High Score: " + str(high_score), red, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                print("game over")

            plot_snake(gamewindow, black, snake_list, snake_size)
        pygame.display.update()  # to update changes
        clock.tick(fps)

    pygame.quit()
    quit()


game_loop()
