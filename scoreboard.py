from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.show()

    def increase_score(self, direction):
        if direction:
            self.l_score += 1
        else:
            self.r_score += 1
        self.show()

    def show(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
