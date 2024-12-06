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

        running = True
        state = "menu"

        b1 = Button(80, 480, "EASY", 120,True)
        b2 = Button(210, 480, "MEDIUM", 120,True)
        b3 = Button(340, 480, "HARD", 120,True)
        buttons = [b1, b2, b3]

        b4 = Button(100, 560, "Reset", 80,False)
        b5 = Button(230, 560, "Restart", 80,False)
        b6 = Button(360, 560, "Exit", 80,False)
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
                        if state == "game":
                            clicked_cell = draw_board.click(mouse_x, mouse_y)
                            if clicked_cell:
                                print(f"Cell clicked: {clicked_cell}")

                        for button in game_buttons:
                            if button.check_click(mouse_x, mouse_y):
                                print(f"Button {button.txt} clicked!")
                                if button.txt == "Reset":
                                    running = False
                                if button.txt == "Restart":
                                    state = "menu"
                                    for button in buttons:
                                        button.active = True
                                if button.txt == "Exit":
                                    running = False

                if event.type == pygame.KEYDOWN:
                    if state == "game" and draw_board.selected_cell:
                        key = event.key
                        if pygame.K_1 <= key <= pygame.K_9:
                            draw_board.sketch(key - pygame.K_0)
                        if key == pygame.K_BACKSPACE:
                            draw_board.clear()
                        if key == pygame.K_RETURN:
                            draw_board.place_number(draw_board.selected_cell.value)

                        if key == pygame.K_LEFT and draw_board.selected_cell.row > 0:
                            draw_board.select(draw_board.selected_cell.row - 1, draw_board.selected_cell.col)
                        if key == pygame.K_RIGHT and draw_board.selected_cell.row < 8:
                            draw_board.select(draw_board.selected_cell.row + 1, draw_board.selected_cell.col)
                        if key == pygame.K_UP and draw_board.selected_cell.col > 0:
                            draw_board.select(draw_board.selected_cell.row, draw_board.selected_cell.col - 1)
                        if key == pygame.K_DOWN and draw_board.selected_cell.col < 8:
                            draw_board.select(draw_board.selected_cell.row, draw_board.selected_cell.col + 1)

            if state == "menu":
                screen.blit(maple, (0,0))
                cursiveFont = pygame.font.Font('C:\Windows\Fonts\ITCEDSCR.ttf', 120)
                text_surface = cursiveFont.render('Sudoku', False, (0, 0, 0))
                shadow = cursiveFont.render('Sudoku', False, (255, 255, 255))
                screen.blit(shadow, (117, 81))
                screen.blit(text_surface, (120, 80))
            #consider this?

                for button in buttons:
                    button.check_button(mouse_x, mouse_y)
                    button.draw_btn(screen, pygame.font.SysFont('Arial', 20))

            elif state == "game":
                screen.fill((255,140,0))
                draw_board.draw()

                for button in game_buttons:
                    button.check_button(mouse_x, mouse_y)
                    button.draw_btn(screen, pygame.font.SysFont('Arial', 20))

            pygame.display.update()

    finally:
        pygame.quit()

if __name__ == '__main__':
    main()
