import pygame
import time
import random
import os

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 215, 0)  # Gold for better contrast
dark_green = (0, 100, 0)  # Darker green for snake
orange = (255, 140, 0)  # Orange for normal food
black = (0, 0, 0)
blue = (30, 144, 255)  # Bonus food
red = (220, 20, 60)    # Speed food
purple = (148, 0, 211) # Slow food

# Modern color palette (high contrast for background image)
flat_snake = (0, 255, 127)      # Bright green
flat_food = (255, 69, 0)        # Bright orange-red
flat_bonus = (255, 255, 0)      # Bright yellow
flat_speed = (30, 144, 255)     # Bright blue
flat_slow = (186, 85, 211)      # Bright purple
obstacle_color = (255, 255, 255) # White for obstacles
shadow = (0, 0, 0, 120)

# Set display dimensions based on background image
width = 800
height = 600

# Define snake block size and speed
snake_block = 20
snake_speed = 15

# Create the game window
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Load and scale background image
background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (width, height))
# Optional custom background
try:
    custom_bg = pygame.image.load("background2.jpg")
    custom_bg = pygame.transform.scale(custom_bg, (width, height))
except:
    custom_bg = None
# Optional custom snake skin
try:
    custom_snake_img = pygame.image.load("snake_skin.png")
    custom_snake_img = pygame.transform.scale(custom_snake_img, (snake_block, snake_block))
except:
    custom_snake_img = None

# Load sound effects
try:
    eat_sound = pygame.mixer.Sound("eat.wav")
except:
    eat_sound = None
try:
    gameover_sound = pygame.mixer.Sound("gameover.wav")
except:
    gameover_sound = None

# Set clock for controlling game speed
clock = pygame.time.Clock()

# Set font style for displaying score and messages
font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 40)

# Modern font
try:
    modern_font = pygame.font.SysFont("arialrounded", 36)
except:
    modern_font = font_style

# High score file
HIGH_SCORE_FILE = "high_score.txt"
def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, 'r') as f:
            try:
                return int(f.read())
            except ValueError:
                return 0
    return 0

def save_high_score(score):
    with open(HIGH_SCORE_FILE, 'w') as f:
        f.write(str(score))

# Function to display the player's score and high score
def display_score(score, high_score=None):
    value = score_font.render("Score: " + str(score), True, yellow)
    game_window.blit(value, [10, 10])
    if high_score is not None:
        hs_value = font_style.render(f"High Score: {high_score}", True, yellow)
        game_window.blit(hs_value, [10, 50])

# Draw rounded rectangle
def draw_rounded_rect(surface, color, rect, radius=8):
    pygame.draw.rect(surface, color, rect, border_radius=radius)

# Draw drop shadow text
def draw_shadow_text(text, font, color, x, y, shadow_offset=2):
    shadow_surf = font.render(text, True, (0,0,0))
    surface = game_window
    surface.blit(shadow_surf, (x+shadow_offset, y+shadow_offset))
    text_surf = font.render(text, True, color)
    surface.blit(text_surf, (x, y))

# Function to draw the snake
def draw_snake(snake_block, snake_list, use_custom=False):
    for block in snake_list:
        if use_custom and custom_snake_img:
            game_window.blit(custom_snake_img, (block[0], block[1]))
        else:
            draw_rounded_rect(game_window, flat_snake, [block[0], block[1], snake_block, snake_block], radius=8)

# Draw modern food icons
def draw_food_icon(x, y, food_type):
    if food_type["effect"] == "normal":
        # Apple: red circle with green leaf
        pygame.draw.circle(game_window, flat_food, (int(x+snake_block/2), int(y+snake_block/2)), snake_block//2)
        pygame.draw.ellipse(game_window, (0,200,0), [x+snake_block*0.6, y+snake_block*0.2, snake_block*0.3, snake_block*0.2])
    elif food_type["effect"] == "bonus":
        # Star: yellow
        points = []
        cx, cy, r = x+snake_block/2, y+snake_block/2, snake_block/2
        for i in range(5):
            angle = i * 144 * 3.14159 / 180
            points.append((cx + r * 0.95 * pygame.math.cos(angle), cy + r * 0.95 * pygame.math.sin(angle)))
        pygame.draw.polygon(game_window, flat_bonus, points)
    elif food_type["effect"] == "speed":
        # Lightning bolt: blue
        bolt = [
            (x+snake_block*0.3, y+snake_block*0.2),
            (x+snake_block*0.6, y+snake_block*0.2),
            (x+snake_block*0.4, y+snake_block*0.8),
            (x+snake_block*0.7, y+snake_block*0.8),
            (x+snake_block*0.5, y+snake_block*0.4),
            (x+snake_block*0.7, y+snake_block*0.4),
        ]
        pygame.draw.polygon(game_window, flat_speed, bolt)
    elif food_type["effect"] == "slow":
        # Snail: purple shell (circle) and body (rect)
        pygame.draw.circle(game_window, flat_slow, (int(x+snake_block*0.65), int(y+snake_block*0.65)), snake_block//3)
        pygame.draw.rect(game_window, (120, 80, 200), [x+snake_block*0.3, y+snake_block*0.7, snake_block*0.7, snake_block*0.2], border_radius=5)

# Function to display a message on the screen
def display_message(msg, color, y_offset=0):
    draw_shadow_text(msg, modern_font, color, int(width / 6), int(height / 3 + y_offset))

def display_pause():
    text_lines = ["Game Paused. Press P to Resume"]
    draw_overlay(text_lines, color=yellow)
    pygame.display.update()

def draw_obstacles(obstacles):
    for obs in obstacles:
        pygame.draw.rect(game_window, black, [obs[0], obs[1], snake_block, snake_block])

# Draw modern overlays
def draw_overlay(text_lines, color=(255,255,255), alpha=180):
    overlay = pygame.Surface((width, height), pygame.SRCALPHA)
    overlay.fill((30,30,30,alpha))
    y = height//3
    for line in text_lines:
        draw_shadow_text(line, modern_font, color, width//6, y)
        y += 50
    game_window.blit(overlay, (0,0))

def start_screen():
    use_custom = False
    while True:
        bg = custom_bg if use_custom and custom_bg else background_img
        game_window.blit(bg, (0, 0))
        text_lines = ["SNAKE GAME", "Press SPACE to Start", "Arrows: Move | P: Pause | Q: Quit | C: Replay", "Press S to Toggle Skins"]
        draw_overlay(text_lines, color=yellow)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return use_custom
                if event.key == pygame.K_s:
                    use_custom = not use_custom

# Main game loop
def game_loop(use_custom=False):
    game_over = False
    game_close = False
    replay = False

    # High score
    high_score = load_high_score()
    # Initial position of the snake
    x = width / 2
    y = height / 2

    # Change in position
    x_change = 0
    y_change = 0

    # Snake body (list of blocks)
    snake_list = []
    snake_length = 1

    # Food types: (color, effect, points)
    FOOD_TYPES = [
        {"color": orange, "effect": "normal", "points": 1},
        {"color": blue, "effect": "bonus", "points": 3},
        {"color": red, "effect": "speed", "points": 1},
        {"color": purple, "effect": "slow", "points": 1},
    ]
    # Initial food
    food_type = random.choices(FOOD_TYPES, weights=[80, 10, 5, 5])[0]
    food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    # Generate obstacles (10 random blocks)
    obstacles = []
    for _ in range(10):
        while True:
            ox = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            oy = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            # Avoid placing on initial snake or food
            if (ox, oy) != (width/2, height/2) and (ox, oy) != (food_x, food_y):
                obstacles.append([ox, oy])
                break

    paused = False
    # Set base speed for this game
    base_speed = 15
    snake_speed = base_speed
    while not game_over:
        while game_close:
            bg = custom_bg if use_custom and custom_bg else background_img
            game_window.blit(bg, (0, 0))
            text_lines = ["GAME OVER!", f"Final Score: {snake_length - 1}", f"High Score: {high_score}", "Press Q to Quit or C to Play Again"]
            draw_overlay(text_lines, color=yellow)
            pygame.display.update()
            if gameover_sound:
                gameover_sound.play()
                time.sleep(1)
                gameover_sound.stop()
                gameover_sound.set_volume(0)
                gameover_sound.set_volume(1)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        replay = True
                        game_over = True
                        game_close = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0 and not paused:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0 and not paused:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0 and not paused:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0 and not paused:
                    y_change = snake_block
                    x_change = 0
                elif event.key == pygame.K_p:
                    paused = not paused
        while paused:
            display_pause()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = False
            clock.tick(5)

        # Check for boundary collision
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        # Check for obstacle collision
        for obs in obstacles:
            if x == obs[0] and y == obs[1]:
                game_close = True

        # Update snake position
        x += x_change
        y += y_change
        bg = custom_bg if use_custom and custom_bg else background_img
        game_window.blit(bg, (0, 0))

        # Draw obstacles
        for obs in obstacles:
            draw_rounded_rect(game_window, obstacle_color, [obs[0], obs[1], snake_block, snake_block], radius=8)
        # Draw food icon
        draw_food_icon(food_x, food_y, food_type)

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
        draw_snake(snake_block, snake_list, use_custom=use_custom)
        display_score(snake_length - 1, high_score)
        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            # Choose new food type and position
            food_type = random.choices(FOOD_TYPES, weights=[80, 10, 5, 5])[0]
            food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            # Handle food effect
            if food_type["effect"] == "normal":
                snake_length += 1
            elif food_type["effect"] == "bonus":
                snake_length += 3
            elif food_type["effect"] == "speed":
                snake_length += 1
                snake_speed = min(snake_speed + 3, 40)
            elif food_type["effect"] == "slow":
                snake_length += 1
                snake_speed = max(snake_speed - 3, 5)
            if eat_sound:
                eat_sound.play()
            if snake_length - 1 > high_score:
                high_score = snake_length - 1
                save_high_score(high_score)

        # Gradually increase speed with score (except for food effects)
        snake_speed = base_speed + (snake_length // 5)
        clock.tick(snake_speed)

    pygame.quit()
    quit()
    return replay

# Run the game
use_custom = start_screen()
while True:
    replay = game_loop(use_custom)
    if not replay:
        break
