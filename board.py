import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator
'''
Navigation tips on the board:
col,x,i,width,w : refers to left-to-right direction. LEFT border is col=x=i=0
row,y,j,height,h : refers to top-to-bottom direction. TOP border is row=y=j=0
'''
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width # MUST BE 9
        self.height = height # MUST BE 9
        self.screen = screen
        if difficulty == "easy":
            # unfilled is used for removal and checking end-of-game
            self.removal = 30
        elif difficulty == "medium":
            self.removal = 40
        elif difficulty == "hard":
            self.removal = 50
        self.unfilled = self.removal
        self.board = self.init_board() # keeps a 2D list of Cell objects
        self.cur_row = 4 # the selected cell, row number
        self.cur_col = 4 # the selected cell, column number
        self.select(self.cur_col,self.cur_row)
    def init_board(self):
        """initiate a board, fill values, hide some of them"""
        sudoku = SudokuGenerator(self.width, self.unfilled)
        sudoku.fill_values() # generate a sudoku solution
        bl = []
        for row in range(self.height):
            bl.append([])
            for col in range(self.width):
                # use sudoku solution to initiate Cell objects
                cell = Cell(sudoku.board[row][col], row, col, self.screen)
                bl[row].append(cell)
        # remove part of sudoku solutions
        sudoku.remove_cells()
        for row in range(self.width):
            for col in range(self.width):
                if sudoku.board[row][col] == 0:
                    # set corresponding "hidden" attribute
                    bl[row][col].hidden = True
        return bl
    def draw(self):
        # set fonts used in each cell
        font1 = pygame.font.SysFont('Arial', 20)
        font2 = pygame.font.SysFont('Georgia', 18)
        font3 = pygame.font.SysFont('Arial', 20)
        font3.set_italic(True)
        # step 1: draw lines for board, vertical and horizontal
        for i in range(1, self.width):
            start = (i * 60, 0) # hard-coded '60'
            end = (i * 60, 540) # hard-coded '60,540'
            pygame.draw.line(self.screen, (50,50,50), start, end, 1)
        for j in range(1, self.height):
            start = (0, j * 60) # hard-coded '60'
            end = (540, j * 60) # hard-coded '60,540'
            pygame.draw.line(self.screen, (50,50,50), start, end, 1)
        # step 2: draw bold outlines for boxes
        for i in range(1, self.width // 3):
            start = (i * 180, 0) # hard-coded '180'
            end = (i * 180, 540) # hard-coded '180,540'
            pygame.draw.line(self.screen, 'black', start, end, 3)
        for j in range(1, self.height // 3 + 1):
            start = (0, j * 180) # hard-coded '180'
            end = (540, j * 180) # hard-coded '180,540'
            pygame.draw.line(self.screen, 'black', start, end, 3)
        # step 3: draw cells, including border and numbers
        for row in range(self.height):
            for col in range(self.width):
                self.board[row][col].draw_cell(font1, font2, font3)
    def select(self, row, col):
        """ Marks the cell at (row, col) as the current selected cell"""
        # step 1： set the last selected cell to be not-selected
        self.board[self.cur_row][self.cur_col].selected = False
        # step 2: change the pointer to new position (row, col)
        self.cur_row = row
        self.cur_col = col
        # step 3： set the cell at new position to be selected
        self.board[self.cur_row][self.cur_col].selected = True
    def click(self, x, y): # this method not used
        if y < 540:
            col = x // 60
            row = y // 60
            return (row, col)
        return None
    def clear(self):
        self.board[self.cur_row][self.cur_col].guess = 0
        if self.board[self.cur_row][self.cur_col].confirm != 0:
            self.board[self.cur_row][self.cur_col].confirm = 0
            self.unfilled += 1 # important: add back unfilled
    def sketch(self, value):
        self.board[self.cur_row][self.cur_col].set_sketched_value(value)
    def place_number(self, value):
        if self.board[self.cur_row][self.cur_col].confirm == 0: # important!
            self.board[self.cur_row][self.cur_col].set_confirmed_value(value)
            self.unfilled -= 1 # unfilled = 0, means end of game
    def reset_to_original(self):
        for row in range(self.height):
            for col in range(self.width):
                self.board[row][col].guess = 0
                self.board[row][col].confirm = 0
        self.unfilled = self.removal # Important: reset unfilled value
    def is_full(self):
        if self.unfilled == 0:
            return True
        else:
            return False
    def update_board(self):
        pass
    def find_empty(self):
        """	Finds an empty cell and returns its row and col as a tuple (x,y)"""
        pass
    def check_board(self):
        """Check whether the Sudoku board is solved correctly"""
        for row in range(self.height):
            for col in range(self.width):
                # important: only check those hidden cells
                if self.board[row][col].hidden:
                    if self.board[row][col].confirm != self.board[row][col].value:
                        return False
        return True
    def handle_key(self, key):
        # this handles all keybaord events, including button 1~9 for data entry
        # BACKSPACE for clear the cell, RETURN for confirm the cell
        if key == pygame.K_UP and self.cur_row > 0:
            self.select(self.cur_row - 1, self.cur_col)
        if key == pygame.K_DOWN and self.cur_row < 8:
            self.select(self.cur_row + 1, self.cur_col)
        if key == pygame.K_LEFT and self.cur_col > 0:
            self.select(self.cur_row, self.cur_col - 1)
        if key == pygame.K_RIGHT and self.cur_col < 8:
            self.select(self.cur_row, self.cur_col + 1)
        for num_key in range(pygame.K_1, pygame.K_9 + 1):
            if key == num_key and self.board[self.cur_row][self.cur_col].hidden == True:
                guess = num_key - pygame.K_1 + 1
                self.sketch(guess)
        if key == pygame.K_BACKSPACE and self.board[self.cur_row][self.cur_col].hidden == True:
            self.clear()
        if key == pygame.K_RETURN and self.board[self.cur_row][self.cur_col].hidden == True:
            temp = self.board[self.cur_row][self.cur_col].guess
            self.place_number(temp)
            self.sketch(0)