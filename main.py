from turtle import Screen , Turtle
import time
import snake_class
import food
import score_board

food1 = food.food()
scoreboard = score_board.scoreboard()

screen = Screen()
screen.setup(width = 600 , height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)




snake1 = snake_class.snake()

screen.listen()

screen.onkey(key = "Up" , fun = snake1.move_up)
screen.onkey(key = "Down" , fun = snake1.move_down)
screen.onkey(key = "Left" , fun = snake1.move_left)
screen.onkey(key = "Right" , fun = snake1.move_right)
gameison = True
while(gameison):
    screen.update()
    snake1.snake_move()

    if snake1.head.distance(food1) < 17 :
        snake1.increase_snake_length()
        food1.food_eaten()
        scoreboard.increase_score()

    # detect colision
    if ( snake1.head.xcor() > 300 or snake1.head.xcor() < -300 or snake1.head.ycor() > 300 or snake1.head.ycor() < -300 ) :
        scoreboard.game_over()
        
        # scoreboard.clear()
        snake1.head.goto(0,0)
        time.sleep(3)

    for segment in snake1.turtles:
        if segment == snake1.head :
            continue
        elif snake1.head.distance(segment) < 18 :
            scoreboard.game_over()
            # time.sleep(3)
            # scoreboard.clear()
            snake1.head.goto(0,0)
            time.sleep(3)
            # gameison = False
            
        

    
    



screen.exitonclick()