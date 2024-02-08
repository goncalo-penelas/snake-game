from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_block(pos)

    def add_block(self, pos):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(pos)
        self.blocks.append(new_block)

    def extend(self):
        self.add_block(self.blocks[-1].position())

    def move(self):
        for block_num in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[block_num - 1].xcor()
            new_y = self.blocks[block_num - 1].ycor()
            self.blocks[block_num].goto(new_x, new_y)
        self.blocks[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.blocks[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.blocks[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.blocks[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.blocks[0].setheading(RIGHT)

    def reset_snake(self):
        for block in self.blocks:
            block.hideturtle()
        self.blocks.clear()
        self.create_snake()
        self.head = self.blocks[0]
