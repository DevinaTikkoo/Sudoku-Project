import pygame

class Button:
    def __init__(self, x, y, text, size,active=True):
        self.x = x # top left corner x-coordinate
        self.y = y # top left corner y-coordinate
        self.txt = text # button text
        self.w = size # button width
        self.h = int(size / 2) # button height
        self.active = active
        self.on = False # True when mouse moved within button
    def check_button(self, x, y):
        if self.x < x < self.x + self.w and self.y < y < self.y + self.h:
            self.on = True
        else:
            self.on = False
    def check_click(self, x, y):
        if self.x < x < self.x + self.w and self.y < y < self.y + self.h:
            # sound effect file must be present!
            click_sound = pygame.mixer.Sound("click.mp3") # play sound
            click_sound.play()
            return True
        return False
    def draw_btn(self, win, font):
        pos = (self.x, self.y, self.w, self.h)
        if self.on:
            pygame.draw.rect(win, "red", pos, 0, 10)
        else:
            pygame.draw.rect(win, "gray", pos, 0, 10)
            pygame.draw.rect(win, "black", pos, 1, 10)
        txt_surf = font.render(self.txt, True, "white")
        center = ((self.x + self.w //2), (self.y + self.h//2))
        txt_frame = txt_surf.get_rect(center=center)
        win.blit(txt_surf, txt_frame)

if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((540,620))
    pygame.display.set_caption("Buttons")

    running = True
    b1 = Button(70,400,"EASY",120)
    b2 = Button(210,400,"MEDIUM", 120)
    b3 = Button(350,400,"HARD",120)
    buttons = [b1, b2, b3]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for button in buttons:
                        button.check_click(mouse_x, mouse_y)

        win.fill("black")

        mouse_x, mouse_y = pygame.mouse.get_pos()
        for button in buttons:
            button.check_button(mouse_x,mouse_y)

        my_font = pygame.font.SysFont('Arial',20)
        for button in buttons:
            button.draw_btn(win,my_font)

        pygame.display.update()




