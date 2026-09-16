import pygame
import random

pygame.init()

font = pygame.font.Font(None, 50)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Ludo Game")

# 

PATH = [
    (6, 0),
    (7, 0),
    (8, 0),
    (8, 1),
    (8, 2),
    (8, 3),
    (8, 4),
    (8, 5),
    (9, 6),
    (10, 6),
    (11, 6),
    (12, 6),
    (13, 6),
    (14, 6),
    (14, 7),
    (14, 8),
    (13, 8),
    (12, 8),
    (11, 8),
    (10, 8),
    (9, 8),
    (8, 9),
    (8, 10),
    (8, 11),
    (8, 12),
    (8, 13),
    (8, 14),
    (7, 14),
    (6, 14),
    (6, 13),
    (6, 12),
    (6, 11),
    (6, 10),
    (6, 9),
    (5, 8),
    (4, 8),
    (3, 8),
    (2, 8),
    (1, 8),
    (0, 8),
    (0, 7),
    (0, 6),
    (1, 6),
    (2, 6),
    (3, 6),
    (4, 6),
    (5, 6),
    (6, 5),
    (6, 4),
    (6, 3),
    (6, 2),
    (6, 1),
]


ROWS = 15
COLS = 15
CELL_SIZE = 40

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (220, 50, 50)
GREEN = (50, 180, 80)
YELLOW = (240, 200, 50)
BLUE = (60, 120, 220)

#

tokens = [0, 0, 0, 0]
selected_token = None
dice_value = None

TOKEN_COLOR = GREEN

#

def draw_token(position, color, offset_x=0, offset_y=0):
    column, row = PATH[position]

    x = column * CELL_SIZE + CELL_SIZE // 2 + offset_x
    y = row * CELL_SIZE + CELL_SIZE // 2 + offset_y

    pygame.draw.circle(
        screen,
        color,
        (x, y),
        CELL_SIZE // 3
    )
#

def draw_path():
    for position in PATH:

        column, row = position

        x = column * CELL_SIZE
        y = row * CELL_SIZE

        pygame.draw.rect(
            screen,
            WHITE,
            (x, y, CELL_SIZE, CELL_SIZE)
        )

        pygame.draw.rect(
            screen,
            BLACK,
            (x, y, CELL_SIZE, CELL_SIZE),
            1
        )

#

def draw_home_areas():
    pygame.draw.rect(
        screen,
        RED,
        (0, 0, 6 * CELL_SIZE, 6 * CELL_SIZE)
    )

    pygame.draw.rect(
        screen,
        GREEN,
        (9 * CELL_SIZE, 0, 6 * CELL_SIZE, 6 * CELL_SIZE)
    )

    pygame.draw.rect(
        screen,
        BLUE,
        (0, 9 * CELL_SIZE, 6 * CELL_SIZE, 6 * CELL_SIZE)
    )

    pygame.draw.rect(
        screen,
        YELLOW,
        (9 * CELL_SIZE, 9 * CELL_SIZE, 6 * CELL_SIZE, 6 * CELL_SIZE)
    )

    pygame.draw.rect(
        screen,
        WHITE,
        (6 * CELL_SIZE, 6 * CELL_SIZE, 3 * CELL_SIZE, 3 * CELL_SIZE)
    )

#
# Move token function

def move_token(token_index, amount):
    global dice_value

    new_position = tokens[token_index] + amount

    if 0 <= new_position < len(PATH):
        tokens[token_index] = new_position
        dice_value = None

# end move func
#
# roll dice function

def roll_dice():
    global dice_value

    dice_value = random.randint(1, 6)

#
#


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                roll_dice()

            if event.key == pygame.K_RIGHT:
                move_token(0, dice_value)

            if event.key == pygame.K_LEFT:
                move_token(0, dice_value)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            for i in range(4):
                column, row = PATH[tokens[i]]

                token_x = column * CELL_SIZE + CELL_SIZE // 2 + offsets[i][0]
                token_y = row * CELL_SIZE + CELL_SIZE // 2 + offsets[i][1]

                distance = ((mouse_x - token_x) ** 2 +
                            (mouse_y - token_y) ** 2) ** 0.5

                if distance <= CELL_SIZE // 3:
                    selected_token = i
                    print("Selected token:", i)

            

    screen.fill("white")

    for row in range(ROWS):
        for column in range(COLS):

            x = column * CELL_SIZE
            y = row * CELL_SIZE

            pygame.draw.rect(
                screen,
                "black",
                (x, y, CELL_SIZE, CELL_SIZE),
                1
            )

    draw_home_areas()
    draw_path()

    offsets = [
    (-8, -8),
    (8, -8),
    (-8, 8),
    (8, 8)
]

    for i in range(4):
        draw_token(
            tokens[i],
            TOKEN_COLOR,
            offsets[i][0],
            offsets[i][1]
        )

    if dice_value is not None:
        dice_text = font.render(
            f"Dice: {dice_value}",
            True,
            BLACK
        )
        screen.blit(dice_text, (620, 500))

    
    

    pygame.display.flip()

pygame.quit()