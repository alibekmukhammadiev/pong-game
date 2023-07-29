from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        self.coordinates = coordinates

        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(self.coordinates[0], self.coordinates[1])
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        ycor_up = self.ycor() + 20
        if self.ycor() < 230:
            self.goto(self.xcor(), ycor_up)
            


    def down(self): 
        ycor_down = self.ycor() - 20
        if self.ycor() > -230:
            self.goto(self.xcor(), ycor_down)


                      
        