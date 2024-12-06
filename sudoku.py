import pygame

from board2 import Board
import sudoku_generator
from button import Button

width, height = 540,620
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku") #not necessary, I just want to feel fancy
maple = pygame.image.load("maple.jpg").convert()

#initializes pygame
def main():
    try:
        pygame.init()

        draw_board = None
        running = True
        state = "menu"

        b1 = Button(40, 400, "EASY", 120,True)
        b2 = Button(180, 400, "MEDIUM", 120,True)
        b3 = Button(320, 400, "HARD", 120,True)
        buttons = [b1, b2, b3]

        b4 = Button(40, 560, "Reset", 80,False)
        b5 = Button(180, 560, "Restart", 80,False)
        b6 = Button(320, 560, "Exit", 80,False)
        game_buttons = [b4, b5, b6]

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
                                if button.txt == "EASY" and button.active == True:
                                    sudoku = sudoku_generator.generate_sudoku(9,30)
                                    draw_board = Board(9,9,screen,"easy",sudoku)
                                elif button.txt == "MEDIUM" and button.active == True:
                                    sudoku = sudoku_generator.generate_sudoku(9,40)
                                    draw_board = Board(9,9,screen,"easy",sudoku)
                                elif button.txt == "HARD" and button.active == True:
                                    sudoku = sudoku_generator.generate_sudoku(9,50)
                                    draw_board = Board(9,9,screen,"hard",sudoku)
                                for button in buttons:
                                    button.active = False
                                state = "game"

                        for button in game_buttons:
                            if button.check_click(mouse_x, mouse_y):
                                print(f"Button {button.txt} clicked!")
                                if button.txt == "Reset":
                                    running = False
                                if button.txt == "Restart":
                                    state = "menu"
                                if button.txt == "Exit":
                                    running = False

            if state == "menu":
                screen.blit(maple, (0,0))
                cursiveFont = pygame.font.Font('C:\Windows\Fonts\ITCEDSCR.ttf', 120)
                text_surface = cursiveFont.render('Sudoku', False, (0, 0, 0))
                shadow = cursiveFont.render('Sudoku', False, (255, 255, 255))
                screen.blit(shadow, (98, 81))
                screen.blit(text_surface, (100, 80))
            #consider this?

                for button in buttons:
                    button.check_button(mouse_x, mouse_y)
                    button.draw_btn(screen, pygame.font.SysFont('Arial', 20))
            elif state == "game":
                screen.fill((0, 0, 255))
                draw_board.draw()

                for button in game_buttons:
                    button.check_button(mouse_x, mouse_y)
                    button.draw_btn(screen, pygame.font.SysFont('Arial', 20))

            pygame.display.update()

    finally:
        pygame.quit()

if __name__ == '__main__':
    main()
