import button
from cell import Cell
import pygame

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

        self.board = [[Cell(0, row, col, screen) for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]
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


    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.selected = False

        #Make cell coord as current cell
        self.selected_cell = self.board[row][col]
        self.selected_cell.selected = True

    def click(self, x, y):

        #Grid bounds for box
        row = y // CELL_SIZE
        col = x // CELL_SIZE

        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            #calling select cell
            self.select(row,col)
            #makeing tuple to return
            x = (row,col)
            return x
        return None

    def clear(self):

        if self.selected_cell:
            row = self.selected_cell.row
            col = self.selected_cell.col
            self.board[row][col].set_cell_value(0)

    def sketch(self, value):

        if self.selected_cell:
            row = self.selected_cell.row
            col = self.selected_cell.col
            self.board[row][col].set_sketched_value(value)

    def place_number(self, value):

        if self.selected_cell:
            row = self.selected_cell.row
            col = self.selected_cell.col
            self.board[row][col].set_cell_value(value)

    def reset_to_original(self):
        #loop through current board and check if was originally 0
        #og 0s mean for user input so change those back to 0
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.board[i][j] != self.og_values[i][j]:
                    self.board[i][j] = 0

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
                    return tuple(i,j)







