from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier"
SIZE = 12
STYLE = "normal"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}",
                   move=False,
                   align=ALIGNMENT,
                   font=(FONT, SIZE, STYLE)
                   )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_file()
        self.score = 0
        self.update_score()

    def write_file(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highscore}")

