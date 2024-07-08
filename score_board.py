from turtle import Turtle 
import time

class scoreboard(Turtle):
    
    def __init__ (self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto( 0 , 270)
        self.clear()
        self.write(arg=f"Score = {self.score} , Highscore = {self.highscore}" , align = "center" , font = ("Arial" , 20 , "normal"))
        self.hideturtle()

    def game_over(self):
        self.color("white")
        self.goto(0,0)
        self.write( "Will Restart soon..." , align = "center" , font = ("Roboto" , 25 , "normal")  )
        self.reset()
        
        

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto( 0 , 270)
        self.write(arg=f"Score = {self.score} ,  Highscore = {self.highscore}" , align = "center" , font = ("Arial" , 20 , "normal"))
    
        
    def reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
        self.score = 0
    