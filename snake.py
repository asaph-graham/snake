import sys
import time

UP= (0,-1)
DOWN= (0,1)
LEFT= (-1,0)
RIGHT= (1,0)

class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self, position):
        self.body= self.body[1:] + [position]

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]


class Game:
    def __init__(self, height, width):
        self.height= height
        self.width= width
        self.snake= Snake([(0,3), (1,3), (2,3), (3,3)], RIGHT)

    def board_matrix(self):
        matrix = [[" " for _ in range(self.width + 2)]
                for _ in range(self.height + 2)]

        for x in range(self.width + 2):
            matrix[0][x] = "+"
            matrix[-1][x] = "+"

        for y in range(1, self.height+1):
            matrix[y][0] = "|"
            matrix[y][-1] = "|"

        for x, y in self.snake.body[:-1]:
            matrix[y + 1][x + 1] = "o"

        head_x, head_y = self.snake.head()
        matrix[head_y + 1][head_x + 1] = "X"

        return matrix


    def render(self):
        for row in self.board_matrix():
            print(" ".join(row))
    
    def ansi_clear(self):
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()
    def push_clear(self):
        print("\n" * 70)
    

game= Game(10,10)
game.render()
playerMove= input("enter move: ")

# while playerMove!= 'q':
#     if playerMove== 'w':
#         game.snake.set_direction(UP)
#     elif playerMove== 's':
#         game.snake.set_direction(DOWN)
#     elif playerMove== 'a':
#         game.snake.set_direction(LEFT)
#     elif playerMove== 'd':
#         game.snake.set_direction(RIGHT)

#     head_x, head_y= game.snake.head()
#     dir_x, dir_y= game.snake.direction
#     new_head= (head_x + dir_x, head_y + dir_y)
#     game.snake.take_step(new_head)

#     game.ansi_clear()
#     game.render()
#     playerMove= input("enter move: ")

while playerMove!= 'q':
    if playerMove== 'w':
        game.snake.set_direction(UP)
    elif playerMove== 's':
        game.snake.set_direction(DOWN)
    elif playerMove== 'a':
        game.snake.set_direction(LEFT)
    elif playerMove== 'd':
        game.snake.set_direction(RIGHT)
    elif playerMove== '':
        game.snake.set_direction(game.snake.direction)
    else:
        print("Invalid input")

    position= (game.snake.head()[0] + game.snake.direction[0], game.snake.head()[1] + game.snake.direction[1])
    game.snake.take_step(position)
    game.push_clear()
    game.render()
    playerMove= input("enter move: ")    



