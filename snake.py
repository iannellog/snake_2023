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

    def check_move(self, move, eats):
        """
        check if the move is valid for the snake taking into account if the snake eats food
        :param move: move to be taken
        :param eats: if the snake has found food
        :return: if the move is valid
        """
        return True

    def place_in_start_position(self, play_field, initial_position):
        """
        place the snake in the play field at a given initial position
        :param play_field: play field
        :param initial_position: initial position
        :return:
        """
        pass

    def update(self, move):
        """
        update the snake body and its path according to the move
        :param move: move to be taken
        :return: None
        """
        pass
