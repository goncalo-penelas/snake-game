from turtle import Turtle

SCORE_POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
FONT_GAME_OVER = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = self.get_highscore()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(SCORE_POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT_GAME_OVER)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def get_highscore(self):
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read().strip())
        except FileNotFoundError:
            with open("high_score.txt", "w") as file:
                self.high_score = 0
                file.write(str(self.high_score))

        return self.high_score
