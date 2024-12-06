import pygame

from board2 import Board
import sudoku_generator
from button import Button

width, height = 540,620
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku") #not necessary, I just want to feel fancy
maple = pygame.image.load("maple.jpg").convert()
leaves = pygame.image.load("leaves.jpeg").convert()

def game_over_screen():
    screen.blit(maple, (0, 0))
    cursiveFont = pygame.font.Font('C:\Windows\Fonts\ITCEDSCR.ttf', 100)
    text_surface = cursiveFont.render('Game Over', False, (0, 0, 0))
    shadow = cursiveFont.render('Game Over', False, (255, 255, 255))
    screen.blit(shadow, (117, 81))
    screen.blit(text_surface, (120, 80))

def game_win_screen():
    screen.blit(maple, (0, 0))
    cursiveFont = pygame.font.Font('C:\Windows\Fonts\ITCEDSCR.ttf', 100)
    text_surface = cursiveFont.render('Game Win', False, (0, 0, 0))
    shadow = cursiveFont.render('Game Win', False, (255, 255, 255))
    screen.blit(shadow, (117, 81))
    screen.blit(text_surface, (120, 80))


#initializes pygame
def main():
    try:
        pygame.init()

        running = True
        state = "menu"

        '''This sets up all the button objects'''
        b1 = Button(80, 480, "EASY", 120,True)
        b2 = Button(210, 480, "MEDIUM", 120,True)
        b3 = Button(340, 480, "HARD", 120,True)
        buttons = [b1, b2, b3]

        b4 = Button(100, 560, "Reset", 80,False)
        b5 = Button(230, 560, "Restart", 80,False)
        b6 = Button(360, 560, "Exit", 80,False)
        game_buttons = [b4, b5, b6]

        restart2 = Button(210, 420, "Restart", 120, False)
        exit2 = Button(210, 420, "Exit", 120, False)

        while running:
            for event in pygame.event.get():
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    running = False

                '''This handles all button presses on the menu'''
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
                                    draw_board = Board(9,9,screen,"medium",sudoku)
                                elif button.txt == "HARD" and button.active == True:
                                    sudoku = sudoku_generator.generate_sudoku(9,50)
                                    draw_board = Board(9,9,screen,"hard",sudoku)
                                for button in buttons:
                                    button.active = False
                                state = "game"

                        '''This checks and highlights the selected cell'''
                        if state == "game":
                            clicked_cell = draw_board.click(mouse_x, mouse_y)
                            if clicked_cell:
                                print(f"Cell clicked: {clicked_cell}")

                        '''This handles all button presses on the game screen'''
                        for button in game_buttons:
                            if button.check_click(mouse_x, mouse_y):
                                print(f"Button {button.txt} clicked!")
                                if button.txt == "Reset":
                                    draw_board.reset_to_original()
                                if button.txt == "Restart":
                                    state = "menu"
                                    for button in buttons:
                                        button.active = True
                                if button.txt == "Exit":
                                    running = False

                '''This handles all key presses'''
                if event.type == pygame.KEYDOWN:
                    if state == "game" and draw_board.selected_cell:
                        key = event.key
                        if pygame.K_1 <= key <= pygame.K_9:
                            draw_board.sketch(key - pygame.K_0)
                        if key == pygame.K_BACKSPACE:
                            draw_board.clear()
                        if key == pygame.K_RETURN:
                            if draw_board.selected_cell.value is not None:
                                draw_board.place_number(draw_board.selected_cell.value)

                                '''This detects whether the user has won or lost when board is full
                                and displays the appropriate game over or game win screen '''
                                result = draw_board.check_board()
                                if result == "win":
                                    print("Valid win")
                                    for button in game_buttons:
                                        button.active = False
                                    state = "game_win"
                                elif result == "loss":
                                    for button in game_buttons:
                                        button.active = False
                                    state = "game_over"

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

            '''This generates the game's graphics'''
            if state == "game":
                screen.blit(leaves, (0,-3000))
                draw_board.draw()

                for button in game_buttons:
                    button.check_button(mouse_x, mouse_y)
                    button.draw_btn(screen, pygame.font.SysFont('Arial', 20))

            if state == "game_over":
                game_over_screen()
                restart2.active = True
                restart2.check_button(mouse_x, mouse_y)
                restart2.draw_btn(screen, pygame.font.SysFont('Arial', 20))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart2.check_click(mouse_x, mouse_y):
                        print(f"Button {restart2.txt} 2 clicked!")

                        restart2.active = False
                        state = "menu"

                        for button in buttons:
                            button.active = True
            if state == "game_win":
                game_win_screen()
                exit2.active = True
                exit2.check_button(mouse_x, mouse_y)
                exit2.draw_btn(screen, pygame.font.SysFont('Arial', 20))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart2.check_click(mouse_x, mouse_y):
                        print(f"Button {exit2.txt} 2 clicked!")

                        exit2.active = False
                        running = False
            pygame.display.update()
    finally:
        pygame.quit()

if __name__ == '__main__':
    main()
