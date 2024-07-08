from turtle import Turtle,Screen
import random 
import snake_class

class food(Turtle):

    def __init__ (self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5 , stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(random.randint(-280 , 280) , random.randint(-280 , 280) )

    def food_eaten(self):
        self.goto(random.randint(-280 , 280) , random.randint(-280 , 280) )


