from turtle import Turtle
import random

FOOD_SIZE = 0.5


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(FOOD_SIZE, FOOD_SIZE)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-265, 265)
        random_y = random.randint(-265, 265)
        self.goto(random_x, random_y)
