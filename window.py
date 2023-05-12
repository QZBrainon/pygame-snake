import pygame

pygame.init()

class Window():
    def __init__(self, width=600, heigth=600) -> None:
        self.width = width
        self.heigth = heigth
        self._display = pygame.display
        self._screen = pygame.display.set_mode((self.width,self.heigth))
        self.border = self._screen.get_rect()
        

    def draw_snake(self, color, snake):
        for coord in snake.body:
            pygame.draw.rect(self._screen, color, (coord[0], coord[1], 10, 10))

    def draw_food(self, food):
        pygame.draw.rect(self._screen, (255,0,0), (food[0], food[1], 10, 10))


    def bg_color(self, color):
        self._screen.fill(color)


    def title(self, title: str) -> None:
        pygame.display.set_caption(title)


    def update(self):
        self._display.update()


    def close(self):
        pygame.quit()

