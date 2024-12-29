from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from barrier import Barrier 
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()
t_barrier = Barrier((0,300))
b_barrier = Barrier((0,-290))
b_barrier.shapesize(stretch_len=600,stretch_wid=0.2)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collison with the wall
    if ball.ycor() > 270 or ball.ycor()<-270:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
 
    # Detecct r sided paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect l isded paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    
 



   
screen.exitonclick()
