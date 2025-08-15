import pygame
import random

pygame.init()

width = 800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Neon Snake Game")

black = (0, 0, 0)
neon_green = (57, 255, 20)
neon_pink = (255, 20, 147)
neon_blue = (0, 255, 255)
neon_orange = (255, 165, 0)

snake_block = 20
initial_speed = 8  

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25, bold=True)
score_font = pygame.font.SysFont("comicsansms", 35, bold=True)

def your_score(score):
    value = score_font.render(f"Score: {score}", True, neon_green)
    win.blit(value, [10, 10])

def our_snake(snake_block, snake_list):
    for i, pos in enumerate(snake_list):
        color_shift = (i * 15) % 255
        pygame.draw.rect(win, (color_shift, 255 - color_shift, 150), [pos[0], pos[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1
    score = 0
    snake_speed = initial_speed

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
    food_color = random.choice([neon_pink, neon_blue, neon_orange])

    while not game_over:

        while game_close:
            win.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", neon_pink)
            your_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        win.fill(black)
        pygame.draw.rect(win, food_color, [foodx, foody, snake_block, snake_block])
        
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(score)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            food_color = random.choice([neon_pink, neon_blue, neon_orange])
            length_of_snake += 1
            score += 10
            snake_speed += 1  

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
