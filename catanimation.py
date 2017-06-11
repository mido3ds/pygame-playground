import pygame
import pygame.locals as constants

pygame.init()

FPS = 30
clock = pygame.time.Clock()

# display the window
windowSize = (400, 300)
DISPLAY = pygame.display.set_mode(windowSize, 0, 32)
pygame.display.set_caption('Animation')

# the cat
catImg = pygame.image.load('./cat.png')
catX = 10
catY = 10
direction = 'right'


# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

Play = True
# the main loop
while Play:
    DISPLAY.fill(WHITE)

    if direction == 'right':
        catX += 5
        if catX >= 250:
            direction = 'down'

    elif direction == 'down':
        catY += 3
        if catY >= 200:
            direction = 'left'

    elif direction == 'left':
        catX -= 30
        if catX <= 14:
            direction = 'up'

    elif direction == 'up':
        catY -= 30
        if catY <= 0:
            catX = 10
            catY = 10
            direction = 'right'

    DISPLAY.blit(catImg, (catX, catY))

    # events handling
    for event in pygame.event.get():
        if event.type == constants.QUIT:
            Play = False

    # update the graphics on screen
    pygame.display.update()
    pygame.display.set_caption(
        'Now cat is moving in the direction ' + direction)

    clock.tick(FPS)


pygame.quit()