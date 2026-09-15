import pygame

pygame.init()

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

token_position = 0

def draw_token(position):
    column, row = PATH[position]

    x = column * CELL_SIZE + CELL_SIZE // 2
    y = row * CELL_SIZE + CELL_SIZE // 2

    pygame.draw.circle(
        screen,
        RED,
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

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    draw_token(token_position)

    pygame.display.flip()

pygame.quit()