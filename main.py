from turtle import Screen, Turtle
from ball import Ball
from bricks import Bricks
from paddle import Paddle
from scoreboard import Scoreboard
import time

turtle = Turtle()
screen = Screen()
game_on = True
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Breakout")

paddle = Paddle((0, -250))
brick = Bricks()
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")


while game_on:
    screen.tracer(1)
    screen.update()
    ball.move()
    for brick_position in brick.brick_list:
        if brick_position.isvisible():
            if ball.distance(brick_position) < 50:
                brick.if_collision(brick_position, ball)

                if brick_position in brick.yellow_bricks:
                    score.keep_score()
                elif brick_position in brick.green_bricks:
                    for i in range(3):
                        score.keep_score()
                elif brick_position in brick.orange_bricks:
                    for i in range(5):
                        score.keep_score()
                elif brick_position in brick.red_bricks:
                    for i in range(7):
                        score.keep_score()
    if score == 2:
        ball.go_slow()
    if score.score == 4:
        ball.go_normal()
    if ball.ycor() == 200:
        ball.go_fast()
    if ball.ycor() == 280:
        ball.go_fastest()

    if ball.xcor() < -240 or ball.xcor() > 230:
        ball.bounce_x()
    if ball.ycor() > 280:
        paddle.shrink_paddle()
        ball.bounce_y()
    if ball.distance(paddle) < 60 and ball.ycor() < -220:
        ball.bounce_y()
    elif ball.ycor() < -240:
        ball.reset_position()
        score.clear()
        score.show_scores()
        paddle.goto((0, -250))
        time.sleep(5)
        score.continue_game()
screen.exitonclick()
