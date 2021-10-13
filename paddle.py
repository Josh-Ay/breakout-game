from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.color("blue")
        self.penup()
        self.goto(x, y)

    def move_left(self):
        """ Move the paddle to the left """
        if self.xcor() > -280:
            self.back(20)

    def move_right(self):
        """ Move the paddle to the right """
        if self.xcor() < 280:
            self.forward(20)
