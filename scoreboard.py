from turtle import Turtle

with open("score.txt") as score_file:
    high_score = score_file.read()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.current_score = 0
        self.display_score()

    def display_score(self):
        """ Display current score"""
        self.clear()

        self.goto(-280, 280)
        self.write(f"Score: {self.current_score}", align="left")

        self.goto(-180, 280)
        self.write(f"High Score: {high_score}", align="left")

    def add_to_score(self):
        """ Add one to score and update scoreboard"""
        self.current_score += 1
        self.display_score()

    def update_high_score(self):
        """ Update current high score """
        if self.current_score > int(high_score):
            self.display_score()
            with open("score.txt", "w") as file:
                file.write(str(self.current_score))
