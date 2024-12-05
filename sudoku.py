import pygame
from board import Board
from sudoku_generator import SudokuGenerator
from button import Button

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

                b1 = Button(40, 400, "EASY", 120)
                b2 = Button(180, 400, "MEDIUM", 120)
                b3 = Button(320, 400, "HARD", 120)
                buttons = [b1, b2, b3]

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        for button in buttons:
                            if button.check_click(mouse_x, mouse_y):
                                print(f"Button {button.txt} clicked!")
                                if button.txt == "EASY":
                                    draw_board = Board(width, height, screen, "easy")
                                    draw_board.init_board()


            mouse_x, mouse_y = pygame.mouse.get_pos()
            for button in buttons:
                button.check_button(mouse_x, mouse_y)

                my_font = pygame.font.SysFont('Arial', 20)
                for button in buttons:
                    button.draw_btn(screen, my_font)

                pygame.display.update()

                pygame.display.flip()
                if event.type == pygame.QUIT:
                    running = False

    finally:
        pygame.quit()

if __name__ == '__main__':
    main()
