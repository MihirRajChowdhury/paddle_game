from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position[0],position[1])

    def up(self):
        ycor = self.ycor()
        self.goto(self.xcor(), ycor + 20)

    def down(self):
        ycor = self.ycor()
        self.goto(self.xcor(), ycor - 20)
