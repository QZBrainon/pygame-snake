from random import randint

class Food():
    @staticmethod
    def generate_food(snake, window):
        food = None
        while food == None:
            food = [randint(1, window.width), randint(1, window.heigth)]
            if food in snake.body:
                food = None
        return food
