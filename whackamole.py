import pygame


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light blue")
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            x = 0
            for i in range(32):
                x += 32
                pygame.draw.line(screen, 'black', start_pos=(x, 0), end_pos=(x,512))
            y = 0
            for j in range(32):
                y+= 32
                pygame.draw.line(screen, 'black', start_pos=(0, y), end_pos=(640, y))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
