from turtle import Turtle

class Barrier(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=600,stretch_wid=0.5)
        self.goto(position)
