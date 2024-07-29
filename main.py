import time
from turtle import Turtle, Screen
from platforms import Platform
from ball import Ball
from division import Division
from  scoreboard import ScoreboardP1, ScoreboardP2

# setting up screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=960, height=810)
screen.tracer(0)
# setup platforms
plat1 = Platform((-400, 0), "red")
plat2 = Platform((400, 0), "blue")

# Setup division
division = Division()
# Setup of movimentation of platform 2
screen.listen()
screen.onkey(plat1.move_up, "w")
screen.onkey(plat1.move_down, "s")
screen.onkey(plat2.move_up, "Up" )
screen.onkey(plat2.move_down, "Down" )

# setup ball
ball = Ball()
START = (0, 0)
# setup scoreboard
scoreboard_p1 = ScoreboardP1()
scoreboard_p2 = ScoreboardP2()
game_on = True

while game_on:
    screen.update()
    time.sleep(0.001)
    ball.move()

    if ball.xcor() > 0:
        ball.change_color("blue")
    else:
        ball.change_color("red")
    if ball.ycor() > 390:
        ball.down = True
    elif ball.ycor() < -390:
        ball.down = False
    if ball.distance(plat2) < 30:
        ball.left = True
    elif ball.distance(plat1) < 30:
        ball.left = False

    if ball.xcor() >= 480:
        scoreboard_p1.point("p1")
        ball.goto(START)
    elif ball.xcor() <= -480:
        scoreboard_p2.point("p2")
        ball.goto(START)


# make screen only close when click
screen.exitonclick()
