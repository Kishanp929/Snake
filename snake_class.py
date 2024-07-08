from turtle import Screen , Turtle
import time

class snake:
    def __init__(self):
        starting_positions = [ (0,0) , (-20 ,0) , (-40 , 0) ]
        self.turtle_direction = 0
        self.turtles = []

        for positions in starting_positions:
            timmy1 = Turtle(shape="square")
            timmy1.penup()
            timmy1.speed(0)
            timmy1.color("white")
            timmy1.goto( positions[0] , positions[1] )
            self.turtles.append(timmy1)
        self.head = self.turtles[0]
    def snake_move( self ):
        x_corr = 0
        y_corr = 0
        for i in range(len(self.turtles)):
            if(i == 0):
                x_corr = self.turtles[0].xcor()
                y_corr = self.turtles[0].ycor()
                self.turtles[0].forward( 20 )
                time.sleep(0.09)
            else:
                temp_x_corr = x_corr
                temp_y_corr = y_corr
                x_corr = self.turtles[i].xcor()
                y_corr = self.turtles[i].ycor()
                self.turtles[i].goto(temp_x_corr , temp_y_corr)

    def increase_snake_length(self):
        timmy1 = Turtle(shape="square")

        timmy1.penup()
        timmy1.speed(0)
        timmy1.color("white")
        timmy1.goto(self.turtles[-1].xcor() , self.turtles[-1].ycor())
        self.turtles.append(timmy1)
    
    def move_up(self):
        if(self.turtle_direction == 270):
            return
        self.turtles[0].setheading(90)
        self.turtle_direction = 90

    def move_down(self):
        if(self.turtle_direction == 90):
            return
        self.turtles[0].setheading(270)
        self.turtle_direction = 270

    def move_left(self):
        if(self.turtle_direction == 0):
            return
        self.turtles[0].setheading(180)
        self.turtle_direction = 180

    def move_right(self):
        if(self.turtle_direction == 180):
            return
        self.turtles[0].setheading(0)
        self.turtle_direction = 0
