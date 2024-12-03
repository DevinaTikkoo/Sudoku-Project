import pygame,board,sudoku_generator

#initializes pygame
def main():
    try:
        pygame.init()

        #sets up the screen :)
        width, height = 480, 480
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sudoku") #not necessary, I just want to feel fancy
        maple = pygame.image.load("maple.jpg").convert()

        running = True

        while running:
            for event in pygame.event.get():
                #screen.fill((0, 0, 255)) #full screen fill
                screen.blit(maple, (0,0))
                #background image fill! It's currently a very zoomed in maple tree image, we can change it if we want

                my_font = pygame.font.Font('C:\Windows\Fonts\ITCEDSCR.ttf', 120)
                text_surface = my_font.render('Sudoku', False, (0, 0, 0))
                shadow = my_font.render('Sudoku', False, (255, 255, 255))
                screen.blit(shadow, (95, 81))
                screen.blit(text_surface, (100, 80))
                #consider this?

                pygame.display.flip()
                if event.type == pygame.QUIT:
                    running = False

    finally:
        pygame.quit()

if __name__ == '__main__':
    main()
