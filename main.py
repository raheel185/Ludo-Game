import pygame

# This initializes the Pygame systems we're going to use.
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Ludo Game")

running = True

# is the game loop. 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the user clicks the close button
            running = False

    screen.fill("gray")
    pygame.draw.rect(screen, "red", (80, 80, 200, 200))
    pygame.draw.circle(screen, "blue", (500, 200), 50)
    
    pygame.display.flip()

pygame.quit()