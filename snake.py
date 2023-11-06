"""
Created on Sept. 30, 2023
by Giulio Iannello
"""


class Snake:
    """
    Implements a moving snake including its path
    """

    def __init__(self):
        pass

    def place_in_start_position(self, initial_position):
        """
        place the snake in the play field at a given initial position
        :param initial_position: initial position
        :return: None
        """
        pass

    def get_head_position(self):
        """
        return the snake head position
        :return: snake head position
        """
        return [0, 0]

    def check_move(self, new_position, eats):
        """
        check if the new position is valid for the snake taking into account if it contains food
        :param new_position: new position of the snake head
        :param eats: if the new position contains food
        :return: if the move is valid
        """
        return True

    def update(self, new_position, eats):
        """
        update the snake body and its path according to the new position and it it contains food
        :param eats: if the new position contains food
        :param new_position: new position of the snake head
        :return: None
        """
        pass
