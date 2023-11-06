"""
Created on Sept. 30, 2023
by Giulio Iannello
"""


class Play_field:
    """
    Implements a play field
    play field representation
    - height
    - width
    - list of obstacles (coordinates)
    - list of food (coordinates)
    - snake position

    positions are represented by a list [row, column]
    """

    def __init__(self, height, width, obstacles, food):
        self.height = height
        self.width = width
        self.obstacles = obstacles
        self.food = food
        self.snake_position = None

    def place_snake(self, initial_position):
        """
        store the initial position of the head of the snake
        :param initial_position: initial position of the head of the snake
        :return: None
        """
        self.snake_position = list(initial_position)

    def check_move(self, move):
        """
        check if move is valid for play field and if snake finds food
        :param move: move to be taken by the snake
        :return: tuple(if the move is valid, if the snake has found food)
        """
        return True, False

    def update(self, move):
        """
        update play field
        :param move: move to be taken by the snake
        :return: None
        """
        if move == 'S':
            self.snake_position[0] = self.snake_position[0] + 1
        else:
            raise ValueError(f'unknown move ({move})')

        if self.snake_position[0] < 0:  # snake move to bottom
            self.snake_position[0] = self.height - 1
        elif self.snake_position[0] == self.height: # snake move to top
            self.snake_position[0] = 0

        if self.snake_position[1] < 0:  # snake move to right border
            self.snake_position[1] = self.width - 1
        elif self.snake_position[1] == self.height: # snake move to left border
            self.snake_position[1] = 0

