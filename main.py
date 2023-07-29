import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


turtle = Turtle()
right_pad = Paddle((350, 0))
left_pad = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# off screen animation
screen.tracer(0)

# controlling paddles
screen.listen()
screen.onkey(right_pad.up, "Up")
screen.onkey(right_pad.down, "Down")
screen.onkey(left_pad.up, "w")
screen.onkey(left_pad.down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    
    # detect collision with wall and change direction
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    # detect collision with paddle and change direction
    if ball.distance(right_pad) < 50 and ball.xcor() > 320 or ball.distance(left_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x() 

    # detect Right Paddle misses the boll
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # detect Left Paddle misses the boll
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()


    ball.move()




screen.exitonclick()
