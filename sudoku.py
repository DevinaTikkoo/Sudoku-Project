import pygame

#initializes pygame
def main():
    try:
        pygame.init()

        #sets up the screen :)
        width, height = 480, 480
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sudoku") #not necessary, I just want to feel fancy

        running = True

        while running:
            for event in pygame.event.get():
                screen.fill((0, 0, 255))
                #^ could be replaced with image or something
                pygame.display.flip()
                if event.type == pygame.QUIT:
                    running = False

    finally:
        pygame.quit()

if __name__ == '__main__':
    main()
