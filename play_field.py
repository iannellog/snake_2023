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

    positions of obstacles and food are represented by a list [row, column]
    """

    def __init__(self, height, width, obstacles, food):
        self.height = height
        self.width = width
        self.obstacles = obstacles
        self.food = food

    def check_move(self, snake_position, move):
        """
        check if move from snake position is valid for play field
        compute new head position and check if it contains food
        :param snake_position: position of snake head
        :param move: move to be taken
        :return: tuple(if the move is valid, new snake head position, if it contains food)
        """
        if move == 'N':
            new_position = [(snake_position[0]-1) % self.height, snake_position[1]]
        elif move == 'E':
            new_position = [snake_position[0], (snake_position[1]+1) % self.width]
        elif move == 'S':
            new_position = [(snake_position[0]+1) % self.height, snake_position[1]]
        elif move == 'W':
            new_position = [snake_position[0], (snake_position[1]-1) % self.width]
        elif move == 'NE':
            new_position = [(snake_position[0]-1) % self.height, (snake_position[1]+1) % self.width]
        elif move == 'NW':
            new_position = [(snake_position[0]-1) % self.height, (snake_position[1]-1) % self.width]
        elif move == 'SE':
            new_position = [(snake_position[0]+1) % self.height, (snake_position[1]+1) % self.width]
        elif move == 'SW':
            new_position = [(snake_position[0]+1) % self.height, (snake_position[1]-1) % self.width]
        else:
            raise ValueError(f'unknown move {move}')
        return new_position not in self.obstacles, new_position, new_position in self.food

    def update(self, snake_position):
        """
        PRE: snake_position is not a block
        update play field
        :param snake_position: new position of snake head
        :return: None
        """
        if snake_position in self.food:
            self.food.remove(snake_position)
