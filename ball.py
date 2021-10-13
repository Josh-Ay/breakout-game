from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.x_step, self.y_step = -0.5, -0.5

    def move(self):
        """ Move the ball """
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step

        self.goto(new_x, new_y)

    def bounce_off_wall(self):
        """ Bounce off vertical surface: wall """
        self.x_step *= -1

    def bounce(self):
        """ Bounce off horizontal surface """
        self.y_step *= -1

