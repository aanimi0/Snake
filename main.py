from turtle import Screen
from snake import Snake
from food import Food
from borders import Borders
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 700, height = 700)
screen.bgcolor("black")
screen.title("Saaaaarpili")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
borders = Borders()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #detect collision
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        food.refresh()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for part in snake.snake_body[1:]:
        if snake.head.distance(part) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
