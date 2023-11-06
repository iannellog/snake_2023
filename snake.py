"""
Created on Sept. 30, 2023
by Giulio Iannello
"""


class Snake:
    """
    Implements a moving snake including its path
    snake representation
    - body: list of coordinates, the head of the list represents the position
            of the snake head
    - tail: list of coordinates, the head of the list represents the initial
            position of the snake head, the tail of the list represents the
            last position left by the snake
    - play_field_size: size of the play field [rows, cols]

    coordinates are represented by a list [row, column]
    """

    def __init__(self):
        self.body = []  # body empty
        self.tail = []  # tail empty
        self.play_field_size = None  # invalid value

    def place_in_start_position(self, initial_position, play_field_size):
        """
        place the snake in the play field at a given initial position
        :param initial_position: initial position
        :return: None
        """
        self.body = [initial_position]
        self.play_field_size = play_field_size

    def get_head_position(self):
        """
        return the snake head position
        :return: snake head position
        """
        return self.body[0]

    def check_move(self, new_position, eats):
        """
        check if the new position is valid for the snake taking into account if it contains food
        :param new_position: new position of the snake head
        :param eats: if the new position contains food
        :return: if the move is valid
        """
        body_copy = self.body.copy()
        if not eats:  # tail snake shifts by one position
            body_copy.pop(len(body_copy)-1)
        if len(body_copy) == 0:  # initial move with no food
            return True
        if new_position in body_copy:  # snake head overlap with its body
            return False
        # assert: snake head does not overlap with its body

        # check if snake cross its body
        # strategy: check if snake head (h) has adjacent body segments (b) all around itself
        #
        #   b b       b b      h b      b h
        #    X   or    X   or   X   or   X
        #   b h       h b      b b      b b

        direction = [(new_position[0]-body_copy[0][0]), (new_position[1]-body_copy[0][1])]

        # check if snake has crossed vertical play field boundaries
        if (new_position[0]-body_copy[0][0]) not in (-1, 0, 1):
            # snake has crossed vertically play field boundaries
            if (new_position[0]-body_copy[0][0]) == (self.play_field_size[0]-1):  # move toward N
                direction[0] = -1
            elif (new_position[0]-body_copy[0][0]) == -(self.play_field_size[0]-1):  # move toward S
                direction[0] = 1
            else:
                raise ValueError(f'invalid vertical move (new position={new_position}, snake head={body_copy[0]})')

        # check if snake has crossed horizontal play field boundaries
        if (new_position[1]-body_copy[0][1]) not in (-1, 0, 1):
            # snake has crossed horizontally play field boundaries
            if (new_position[1]-body_copy[0][1]) == (self.play_field_size[1]-1):  # move toward W
                direction[1] = -1
            elif (new_position[1]-body_copy[0][1]) == -(self.play_field_size[1]-1):  # move toward E
                direction[1] = 1
            else:
                raise ValueError(f'invalid horizontal move (new position={new_position}, snake head={body_copy[0]})')

        # actual check
        if direction == [1, 1] and \
                [(new_position[0]-1) % self.play_field_size[0], new_position[1]] in body_copy and \
                [(new_position[0]), (new_position[1]-1) % self.play_field_size[1]] in body_copy:  # move SE
            return False
        elif direction == [1, -1] and \
                [(new_position[0]-1) % self.play_field_size[0], new_position[1]] in body_copy and \
                [(new_position[0]), (new_position[1]+1) % self.play_field_size[1]] in body_copy:  # move SW
            return False
        elif direction == [-1, -1] and \
                [(new_position[0]+1) % self.play_field_size[0], new_position[1]] in body_copy and \
                [(new_position[0]), (new_position[1]+1) % self.play_field_size[1]] in body_copy:  # move NW
            return False
        elif direction == [-1, 1] and \
                [(new_position[0]+1) % self.play_field_size[0], new_position[1]] in body_copy and \
                [(new_position[0]), (new_position[1]-1) % self.play_field_size[1]] in body_copy:  # move NE
            return False
        else:  # move S, W, N, E are valid since snake head does not overlap with its body
            pass

        return True

    def update(self, new_position, eats):
        """
        update the snake body and its path according to the new position and it it contains food
        :param eats: if the new position contains food
        :param new_position: new position of the snake head
        :return: None
        """
        pass
