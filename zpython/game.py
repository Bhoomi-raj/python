import pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Bouncing Ball")

# Ball properties
x, y = 300, 200
dx, dy = 3, 3
radius = 15

running = True
while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move ball
    x += dx
    y += dy

    # Bounce logic
    if x <= radius or x >= 600 - radius:
        dx = -dx
    if y <= radius or y >= 400 - radius:
        dy = -dy

    # Draw
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.update()

pygame.quit()