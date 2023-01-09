from turtle import Turtle, Screen

screen = Screen()
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.speed("slowest")

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)

    def go_slow(self):
        self.speed("slow")

    def go_normal(self):
        self.speed("normal")

    def go_fast(self):
        self.speed("fast")

    def go_fastest(self):
        self.speed("fastest")



