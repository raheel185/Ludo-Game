import pygame
import random

pygame.init()

font = pygame.font.Font(None, 50)
player_font = pygame.font.Font(None, 25)

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

BASE_POSITIONS = [
    # Player 1 - Red
    [
        (2, 2),
        (4, 2),
        (2, 4),
        (4, 4)
    ],

    # Player 2 - Green
    [
        (10, 2),
        (12, 2),
        (10, 4),
        (12, 4)
    ],

    # Player 3 - Yellow
    [
        (10, 10),
        (12, 10),
        (10, 12),
        (12, 12)
    ],

    # Player 4 - Blue
    [
        (2, 10),
        (4, 10),
        (2, 12),
        (4, 12)
    ]
]


ROWS = 15
COLS = 15
CELL_SIZE = 40

#
# colors
#
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (220, 50, 50)
GREEN = (50, 180, 80)
YELLOW = (240, 200, 50)
BLUE = (60, 120, 220)

PLAYER_COLORS = [
    RED,
    GREEN,
    YELLOW,
    BLUE
]

PLAYER_STARTS = [0, 13, 26, 39]

# 
# Game State Variables
#

current_player = 0

tokens = [
    [-1, -1, -1, -1],  # Player 1
    [-1, -1, -1, -1],  # Player 2
    [-1, -1, -1, -1],  # Player 3
    [-1, -1, -1, -1]   # Player 4
]

selected_token = None
dice_value = None

TOKEN_COLOR = GREEN

#


def draw_token(
    position,
    color,
    player_index,
    token_index,
    offset_x=0,
    offset_y=0,
    selected=False
):
    if position == -1:
        column, row = BASE_POSITIONS[player_index][token_index]
    else:
        column, row = PATH[position]

    x = column * CELL_SIZE + CELL_SIZE // 2 + offset_x
    y = row * CELL_SIZE + CELL_SIZE // 2 + offset_y

    if selected:
        pygame.draw.circle(
            screen,
            BLACK,
            (x, y),
            CELL_SIZE // 2
        )

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
    border_width = 8

    # Red home
    pygame.draw.rect(
        screen,
        RED,
        (0, 0, 6 * CELL_SIZE, 6 * CELL_SIZE),
        border_width
    )

    # Green home
    pygame.draw.rect(
        screen,
        GREEN,
        (9 * CELL_SIZE, 0, 6 * CELL_SIZE, 6 * CELL_SIZE),
        border_width
    )

    # Blue home
    pygame.draw.rect(
        screen,
        BLUE,
        (0, 9 * CELL_SIZE, 6 * CELL_SIZE, 6 * CELL_SIZE),
        border_width
    )

    # Yellow home
    pygame.draw.rect(
        screen,
        YELLOW,
        (9 * CELL_SIZE, 9 * CELL_SIZE, 6 * CELL_SIZE, 6 * CELL_SIZE),
        border_width
    )

    # Center
    pygame.draw.rect(
        screen,
        WHITE,
        (6 * CELL_SIZE, 6 * CELL_SIZE, 3 * CELL_SIZE, 3 * CELL_SIZE)
    )

    # Current player indicator
    player_text = player_font.render(
        f"Player {current_player + 1}'s Turn",
        True,
        BLACK
    )

    screen.blit(player_text, (620, 50))
#
# Can Move func

def can_move(token_index):
    if dice_value is None:
        return False

    current_position = tokens[current_player][token_index]

    # Token is in base
    if current_position == -1:
        return dice_value == 6

    # Token is already on the path
    new_position = current_position + dice_value

    # Allow the token to wrap around the board
    return True

#
#

def has_any_legal_move():
    for token_index in range(4):
        if can_move(token_index):
            return True

    return False

#
# Move token function

def move_token(token_index, amount):
    global dice_value

    current_position = tokens[current_player][token_index]

    # Token is in base
    if current_position == -1:

        if amount == 6:
            tokens[current_player][token_index] = PLAYER_STARTS[current_player]
            dice_value = None
        return

    # Token is already on the path
    new_position = (current_position + amount) % len(PATH)

    tokens[current_player][token_index] = new_position
    dice_value = None

# end move func
#

def next_turn():
    global current_player

    current_player = (current_player + 1) % 4

#
# roll dice function

def roll_dice():
    global dice_value

    dice_value = random.randint(1, 6)

# End roll dice
#


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                if dice_value is None:
                    roll_dice()
                    selected_token = None

                    if not has_any_legal_move():
                        print("No legal moves.")

                        dice_value = None
                        next_turn()

            if event.key == pygame.K_RIGHT:
                if dice_value is not None and selected_token is not None:
                    old_dice = dice_value

                    move_token(selected_token, dice_value)
                    selected_token = None

                    if dice_value is None:
                        if old_dice != 6:
                            next_turn()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            for i in range(4):

                if tokens[current_player][i] == -1:
                    column, row = BASE_POSITIONS[current_player][i]
                else:
                    column, row = PATH[tokens[current_player][i]]

                token_x = (
                    column * CELL_SIZE
                    + CELL_SIZE // 2
                    + offsets[i][0]
                )

                token_y = (
                    row * CELL_SIZE
                    + CELL_SIZE // 2
                    + offsets[i][1]
                )

                distance = (
                    (mouse_x - token_x) ** 2
                    + (mouse_y - token_y) ** 2
                ) ** 0.5

                if distance <= CELL_SIZE // 3:

                    if can_move(i):
                        selected_token = i
                        print("Selected token:", i)
                    else:
                        print("Token cannot move.")

            

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

    for player_index in range(4):
        for token_index in range(4):

            draw_token(
                tokens[player_index][token_index],
                PLAYER_COLORS[player_index],
                player_index,
                token_index,
                offsets[token_index][0],
                offsets[token_index][1],
                selected=(
                    selected_token == token_index
                    and player_index == current_player
                )
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