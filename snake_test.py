import unittest
from snake import Snake


class Snake_test(unittest.TestCase):

    def test_check_move(self):
        snake = Snake()
        self.assertIsInstance(snake, Snake, 'cannot create a Snake instance')
        snake.place_in_start_position(None, (0, 0))
        self.assertTrue(snake.check_move('S', False))

    def test_place_in_start_position(self):
        snake = Snake()
        self.assertIsInstance(snake, Snake, 'cannot create a Snake instance')
        snake.place_in_start_position(None, (0, 0))
        # check if the snake has been correctly placed in the play field

    def test_update(self):
        snake = Snake()
        self.assertIsInstance(snake, Snake, 'cannot create a Snake instance')
        snake.place_in_start_position(None, (0, 0))
        snake.update('S')
        # check if the move has been correctly performed


if __name__ == '__main__':
    unittest.main()
