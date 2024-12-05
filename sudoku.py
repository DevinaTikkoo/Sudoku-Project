import pygame
from board import Board
from sudoku_generator import SudokuGenerator
from button import Button

#initializes pygame
def main():
    try:
        pygame.init()

        #sets up the screen :)
        width, height = 540,620
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sudoku") #not necessary, I just want to feel fancy
        maple = pygame.image.load("maple.jpg").convert()

        draw_board = None
        running = True

        b1 = Button(40, 400, "EASY", 120)
        b2 = Button(180, 400, "MEDIUM", 120)
        b3 = Button(320, 400, "HARD", 120)
        buttons = [b1, b2, b3]

        while running:
            for event in pygame.event.get():
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        for button in buttons:
                            if button.check_click(mouse_x, mouse_y):
                                print(f"Button {button.txt} clicked!")
                                if button.txt == "EASY":
                                    draw_board = Board(9, 9, screen, "easy")


            #screen.fill((0, 0, 255)) #full screen fill
            if draw_board is None:
                screen.blit(maple, (0,0))
                my_font = pygame.font.Font('C:\Windows\Fonts\ITCEDSCR.ttf', 120)
                text_surface = my_font.render('Sudoku', False, (0, 0, 0))
                shadow = my_font.render('Sudoku', False, (255, 255, 255))
                screen.blit(shadow, (95, 81))
                screen.blit(text_surface, (100, 80))
            #consider this?

                for button in buttons:
                    button.check_button(mouse_x, mouse_y)
                    button.draw_btn(screen, pygame.font.SysFont('Arial', 20))
            else:
                screen.fill((0, 0, 255))
                draw_board.draw()
            pygame.display.update()

    finally:
        pygame.quit()

if __name__ == '__main__':
    main()
