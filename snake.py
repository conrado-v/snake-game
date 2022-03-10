import turtle as t
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_piece = t.Turtle(shape='square')
            new_piece.color('white')
            new_piece.penup()
            new_piece.goto(position)
            self.snake.append(new_piece)

    def move(self):
        for piece_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[piece_num - 1].xcor()
            new_y = self.snake[piece_num - 1].ycor()
            self.snake[piece_num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
            self.move()

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)
            self.move()

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
            self.move()

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
            self.move()
