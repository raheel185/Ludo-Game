import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Ludo Game")

ROWS = 15
COLS = 15
CELL_SIZE = 35

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (220, 50, 50)
GREEN = (50, 180, 80)
YELLOW = (240, 200, 50)
BLUE = (60, 120, 220)

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

#

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    draw_home_areas()

    for row in range(15):
        for column in range(15):

            x = column * CELL_SIZE
            y = row * CELL_SIZE

            pygame.draw.rect(
                screen,
                "black",
                (x, y, CELL_SIZE, CELL_SIZE),
                1
            )

    pygame.display.flip()

pygame.quit()