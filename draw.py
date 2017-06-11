
''' modules '''
import pygame
import pygame.locals as constants

def main():
    DISPLAYSURF, centre = init()

    draw(DISPLAYSURF, centre)  

    game_loop()

def init():
    pygame.init()
    size = (800, 800)
    centre = (size[0] / 2, size[1] / 2)
    DISPLAYSURF = pygame.display.set_mode(size)
    pygame.display.set_caption('Drawing things')
    return DISPLAYSURF, centre

class cololrs:
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)

def game_loop():
    while True:
        # events
        for event in pygame.event.get():
            if event.type == constants.QUIT:
                pygame.quit()
                sys.exit()

        # updating the drawings
        pygame.display.update()

def draw(DISPLAYSURF, centre):
    # Draw stuff
    DISPLAYSURF.fill(cololrs.WHITE)
    pygame.draw.line(DISPLAYSURF, cololrs.RED, centre, [80, 100], 20)

    pygame.draw.circle(DISPLAYSURF, cololrs.RED, centre, 30)  # small circle
    pygame.draw.circle(DISPLAYSURF, cololrs.RED, centre, 200, 14)  # outside circle


if __name__=="__main__":
	main()
