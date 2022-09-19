from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 0.1
        self.y_move = 0.1



    def start(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)


    def bounce(self):
        self.y_move *= -1
