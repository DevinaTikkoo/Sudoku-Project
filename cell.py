import pygame

class Cell:
    def __init__(self, value, row, col, screen, is_initial=False):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = None
        self.selected = False
        self.size = 60
        self.x = row * self.size
        self.y = col * self.size
        self.is_initial = is_initial

    def set_cell_value(self, value):
        if not self.is_initial:
            self.value = value

    def set_sketched_value(self, value):
        if not self.is_initial:
            self.sketched_value = value

    def draw(self):
        #draws the rectangle
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.size, self.size))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.size, self.size),1)

        # Makes the outline red
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.size, self.size), 4)

        if self.value != 0:
            #writes the value when it isn't 0
            font = pygame.font.SysFont("Arial", 36)
            text = font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.x + self.size // 2, self.y + self.size // 2))
            self.screen.blit(text, text_rect)

        if self.sketched_value is not None:
            #writes the sketched value
            font = pygame.font.SysFont("Arial", 25)
            text = font.render(str(self.sketched_value), True, (169, 169, 169))
            text_rect = text.get_rect(topleft=(self.x + 7, self.y + 7))
            self.screen.blit(text, text_rect)
        #it won't print anything if there is no value
