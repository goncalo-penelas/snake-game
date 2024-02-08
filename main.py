import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from field import Field

from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
field = Field()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
field.draw_field()

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        scoreboard.reset_score()
        snake.reset_snake()

    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            scoreboard.reset_score()
            snake.reset_snake()


screen.exitonclick()
