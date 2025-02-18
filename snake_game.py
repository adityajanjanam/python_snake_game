import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 215, 0)  # Gold for better contrast
dark_green = (0, 100, 0)  # Darker green for snake
orange = (255, 140, 0)  # Orange for food
black = (0, 0, 0)

# Set display dimensions based on background image
width = 800
height = 600

# Create the game window
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Load and scale background image
background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (width, height))

# Set clock for controlling game speed
clock = pygame.time.Clock()

# Define snake block size and speed
snake_block = 20
snake_speed = 15

# Set font style for displaying score and messages
font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 40)

# Function to display the player's score
def display_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    game_window.blit(value, [10, 10])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_window, dark_green, [block[0], block[1], snake_block, snake_block])

# Function to display a message on the screen
def display_message(msg, color, y_offset=0):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [width / 6, height / 3 + y_offset])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x = width / 2
    y = height / 2

    # Change in position
    x_change = 0
    y_change = 0

    # Snake body (list of blocks)
    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:
        while game_close:
            game_window.blit(background_img, (0, 0))
            display_message("You Lost! Press Q-Quit or C-Play Again", yellow)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = snake_block
                    x_change = 0

        # Check for boundary collision
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        # Update snake position
        x += x_change
        y += y_change
        game_window.blit(background_img, (0, 0))

        # Draw food
        pygame.draw.rect(game_window, orange, [food_x, food_y, snake_block, snake_block])

        # Add new block to the snake's body
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for self-collision
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Draw snake and update display
        draw_snake(snake_block, snake_list)
        display_score(snake_length - 1)
        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
game_loop()
