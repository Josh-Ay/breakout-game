from turtle import Screen
from ball import Ball
from paddle import Paddle
from block import Block
from scoreboard import Score
from random import choice

game_on = True

# Creating the screen
screen = Screen()


# Configuring the screen
screen.title("BreakOut Game")
screen.setup(700, 600)
screen.bgcolor("black")
screen.tracer(0)


# Creating instances of the ball, paddle and blocks
ball = Ball()
paddle = Paddle(0, -260)
score = Score()
score.display_score()

blocks = []

x_range = [x for x in range(-330, 330)]
y_range = [y for y in range(200, 260)]

for _ in range(10):
    new_block = Block(choice(x_range), choice(y_range))
    blocks.append(new_block)


# Tying events to the 'left' and 'right' keys
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

# Listening for the above events
screen.listen()


def play_game():
    global game_on

    if game_on:
        screen.update()     # update the screen

        ball.move()     # move the ball

        # bounce off the wall
        if ball.xcor() > 330 or ball.xcor() < -330:
            ball.bounce_off_wall()

        # bounce off the paddle
        if paddle.distance(ball) < 28.8:
            ball.bounce()

        # bounce off top wall
        if ball.ycor() > 280:
            ball.bounce()

        # detect collision between a block and destroy the destroy the corresponding block
        for block in blocks:
            if block.distance(ball) < 28.8:
                score.add_to_score()    # add one to current score
                blocks.remove(block)    # remove block from list
                ball.bounce()
                block.goto(1000, 1000)  # bye-bye block

        # GAME_OVER: CHECK IF THERE ARE NO BLOCKS LEFT OR IF THE PADDLE WENT OUT OF RANGE
        if ball.ycor() < -280 or len(blocks) == 0:
            game_on = False
            score.update_high_score()

    screen.ontimer(play_game, 1)    # keep calling 'play_game' after 1 millisecond


play_game()

screen.mainloop()
