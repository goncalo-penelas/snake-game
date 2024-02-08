from turtle import Turtle


class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-270, 270)

    def draw_field(self):
        self.pendown()
        self.goto(-270, -270)
        self.goto(270, -270)
        self.goto(270, 270)
        self.goto(270, 270)
        self.goto(-270, 270)
