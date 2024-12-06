import button
from cell import Cell
from sudoku_generator import SudokuGenerator
import pygame

#constants
CELL_SIZE = 60
GRID_SIZE = 9

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)

class Board :
    def __init__(self, width, height, screen, difficulty,og_values):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        self.board = [[Cell(og_values[row][col], row, col, screen, is_initial=(og_values[row][col] != 0))
                       for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]
        self.selected_cell = None

        #In main will set this equal to board from self.board
        self.og_values = og_values

    def draw(self):
        # for x in range(0, GRID_SIZE*CELL_SIZE, CELL_SIZE):
        #     for y in range(0, GRID_SIZE*CELL_SIZE, CELL_SIZE):
        #         pygame.draw.line(self.screen, "pink", [x, y], [x + CELL_SIZE, y],3)
        #         pygame.draw.line(self.screen, "pink", [x, y], [x, y + CELL_SIZE],3)
        for row in range(self.height):
            for col in range(self.width):
                self.board[row][col].draw()
                value = self.og_values[row][col]
                if value != 0:  # If the cell is not empty, set the value
                    self.board[row][col].set_cell_value(value)

        for row in range(0, GRID_SIZE, 3):
            for col in range(0, GRID_SIZE, 3):
                # Draw thick lines at every 3rd row and column (for 3x3 blocks)
                pygame.draw.rect(self.screen, BLACK,
                                 (col * CELL_SIZE, row * CELL_SIZE, 3 * CELL_SIZE, 3 * CELL_SIZE),
                                 5)


    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.selected = False

        #Make cell coord as current cell
        self.selected_cell = self.board[row][col]
        self.selected_cell.selected = True

    def click(self, x, y):

        #Grid bounds for box
        row = x // CELL_SIZE
        col = y // CELL_SIZE

        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            #calling select cell
            self.select(row,col)
            #makeing tuple to return
            return (row,col)
        return None

    def clear(self):

        if self.selected_cell and not self.selected_cell.is_initial:
            row = self.selected_cell.row
            col = self.selected_cell.col
            self.board[row][col].set_cell_value(0)
            self.board[row][col].sketched_value = None

    def sketch(self, value):

        if self.selected_cell and not self.selected_cell.is_initial:
            row = self.selected_cell.row
            col = self.selected_cell.col
            self.board[row][col].set_sketched_value(value)

    def place_number(self, value):

        if self.selected_cell:
            row = self.selected_cell.row
            col = self.selected_cell.col

            if self.selected_cell.sketched_value is not None:
                self.board[row][col].set_cell_value(self.selected_cell.sketched_value)
                self.board[row][col].sketched_value = None
            else:
                self.board[row][col].set_cell_value(value)

    def reset_to_original(self):
        #loop through current board and check if was originally 0
        #og 0s mean for user input so change those back to 0
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.board[i][j].value = self.og_values[i][j]
                self.board[i][j].sketched_value = None

    def is_full(self):
        #loop through board and check for 0s
        #if none left then board is full
        for row in self.board:
            for i in row:
                if i.value == 0:
                    return False
        return True

    def update_board(self):
        #may not work because functionality may be in other methods
        #but it's a start
        return self.board

    def find_empty(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.board[i][j].value == 0:
                    return (i,j)

    def check_board(self):
        if not self.is_full():
            return None

        sudoku_gen = SudokuGenerator()

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                value = self.board[row][col].value
                if value != 0:
                    if not sudoku_gen.is_valid(row, col, value):
                        return False
        print("win!")
        return True
