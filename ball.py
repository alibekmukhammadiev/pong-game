from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.shapesize(stretch_wid=1, stretch_len=1)

        self.x_move = 10
        self.y_move = 10

        # changing ball speed every time it collides with the paddles
        self.move_speed = 0.1

    def move(self):
        ball_ycor = self.ycor() + self.y_move
        ball_xcor = self.xcor() + self.x_move

        self.goto(ball_xcor, ball_ycor) 

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1  
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()      
        
              