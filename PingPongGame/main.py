from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.screensize(800, 400)
screen.setup(width=900, height=500)
screen.title("Pong")
l_player = Paddle((-380, 0))
r_player = Paddle((380, 0))
ball = Ball()



screen.listen()
screen.onkeypress(l_player.up, "w")
screen.onkeypress(l_player.down, "s")
screen.onkeypress(r_player.up, "Up")
screen.onkeypress(r_player.down, "Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.start()

    if ball.ycor() > 240 or ball.ycor() < - 240:
        ball.bounce()



screen.exitonclick()