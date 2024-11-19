import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if mole_x <= x < mole_x + 32 and mole_y <= y < mole_y + 32:
                        mole_x = random.randrange(0,20) * 32
                        mole_y = random.randrange(0, 16) *32

            screen.fill("light blue")
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            for i in range(1,20):
                pygame.draw.line(screen, 'black', (i * 32, 0), (i* 32,640))
            for j in range(1,16):
                pygame.draw.line(screen, 'black', (0, j*32), (640, j*32))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
