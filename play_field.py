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

    position are represented by a list [row, column]
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
        return True, [0, 0], False

    def update(self, snake_position):
        """
        update play field
        :param snake_position: new position of snake head
        :return: None
        """
        pass
