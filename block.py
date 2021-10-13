from turtle import Turtle
from random import choice
COLORS = ["red", "yellow", "green", "purple", "orange"]


class Block(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=3)
        self.color(choice(COLORS))
        self.goto(x, y)
