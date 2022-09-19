from turtle import Turtle

MOVE_DISTANCE = 30
MOVABLE_DIS_UPER = 200
MOVABLE_DIS_DOWN = -200


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)


    def up(self):
        if self.ycor() < MOVABLE_DIS_UPER:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > MOVABLE_DIS_DOWN:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)