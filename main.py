import pygame
from window import Window
from settings import Settings
from snake import Snake
from directions import Directions
from food import Food

window = Window()
config = Settings()
snk = Snake(window)
window.title('Pygame Snake')
FPS = 10
BLACK = (0,0,0)
WHITE = (255,255,255)

def main():
    direction = Directions.RIGHT.value
    food = Food.generate_food(snk, window)
    while True:
        config.set_framerate(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window.close()
            if event.type == pygame.KEYDOWN:
                if event.key in [Directions.RIGHT.value, Directions.LEFT.value, Directions.UP.value, Directions.DOWN.value]:
                    direction = event.key
        window.bg_color(BLACK)
        window.draw_food(food)
        window.draw_snake(WHITE, snk)
        snk.move(direction)
        if snk.eats_food(food):
            new_food = Food.generate_food(snk, window)
            window.draw_food(new_food)
        else:
            snk.body.pop()
        if snk.touches_border(window) or snk.touches_itself():
            break
        window.update()
   
    

if __name__ == "__main__":
    main()
