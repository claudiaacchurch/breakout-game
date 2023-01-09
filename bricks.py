from turtle import Turtle, Screen

BRICK_START_PS = [(-230, 280), (-230, 250), (-230, 220), (-230, 190), (-230, 160), (-230, 130), (-230, 100), (-230, 70),
                  (-140, 280), (-140, 250), (-140, 220), (-140, 190), (-140, 160), (-140, 130), (-140, 70), (-140, 100),
                  (-50, 280), (-50, 250), (-50, 220), (-50, 190), (-50, 160), (-50, 130), (-50, 100), (-50, 70),
                  (40, 280), (40, 250), (40, 220), (40, 190), (40, 160), (40, 130), (40, 100), (40, 70),
                  (130, 280), (130, 250), (130, 220), (130, 190), (130, 160), (130, 130), (130, 100), (130, 70),
                  (220, 280), (220, 250), (220, 220), (220, 190), (220, 160), (220, 130), (220, 100), (220, 70)]

screen = Screen()


class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.brick_list = []
        self.yellow_bricks = []
        self.green_bricks = []
        self.orange_bricks = []
        self.red_bricks = []
        self.set_up()

    def set_up(self):
        screen.tracer(0)
        for pos in BRICK_START_PS:
            self.add_brick(pos)

    def add_brick(self, ps):
        new_brick = Turtle("square")
        new_brick.penup()
        new_brick.goto(ps)
        new_brick.shapesize(stretch_wid=1, stretch_len=4)
        for brick in self.brick_list:
            if brick.ycor() == 70 or brick.ycor() == 100:
                brick.color("yellow")
                self.yellow_bricks.append(brick)
            if brick.ycor() == 130 or brick.ycor() == 160:
                brick.color("green")
                self.green_bricks.append(brick)
            if brick.ycor() == 190 or brick.ycor() == 220:
                brick.color("orange")
                self.orange_bricks.append(brick)
            if brick.ycor() == 250 or brick.ycor() == 280:
                brick.color("red")
                self.red_bricks.append(brick)
        self.brick_list.append(new_brick)

    def if_collision(self, brick, ball):
        ball.bounce_y()
        brick.hideturtle()








