from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
scoreboard = 0

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # Detect collision w/ food.
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        score.increase_score()
        print(f"snake's head ={snake.head.position()}")

    # Detect collision w/ wall
    if snake.head.xcor() > 280.01 or snake.head.xcor() < -280.01 or snake.head.ycor() > 280.01 or snake.head.ycor() < -280.01:
        game_on = False
        score.game_over()

    # Detect collision w/ any piece of tail
    for piece in snake.snake[1:]:
        if snake.head.distance(piece) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
