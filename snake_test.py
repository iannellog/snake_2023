import unittest
from snake import Snake


class Snake_test(unittest.TestCase):

    def test_create(self):
        snake = Snake()
        self.assertIsInstance(snake, Snake, 'cannot create a Snake instance')

    def test_place_in_start_position(self):
        snake = Snake()
        position = [0, 0]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        head_position = snake.get_head_position()
        self.assertEqual(head_position, position, f'wrong head position ({head_position} instead of {position})')

    def test_check_initial_move_nofood(self):
        snake = Snake()
        position = [0, 0]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        new_position = [1, 0]
        self.assertTrue(snake.check_move(new_position, False))

    def test_check_initial_move_food(self):
        snake = Snake()
        position = [0, 0]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        new_position = [1, 0]
        self.assertTrue(snake.check_move(new_position, True))

    def test_check_move_nofood_nooverlap(self):
        snake = Snake()
        snake.body = [[1, 0], [1, 1], [0, 1], [0, 0]]
        snake.play_field_size = [10, 10]
        self.assertTrue(snake.check_move([2, 0], False))

    def test_check_move_nofood_overlap(self):
        snake = Snake()
        snake.body = [[1, 0], [1, 1], [0, 1], [0, 0]]
        snake.play_field_size = [10, 10]
        self.assertFalse(snake.check_move([0, 1], False))

    def test_check_move_food_nooverlap(self):
        snake = Snake()
        snake.body = [[1, 0], [1, 1], [0, 1], [0, 0]]
        snake.play_field_size = [10, 10]
        self.assertTrue(snake.check_move([2, 0], True))

    def test_check_move_food_overlap(self):
        snake = Snake()
        snake.body = [[1, 0], [1, 1], [0, 1], [0, 0]]
        snake.play_field_size = [10, 10]
        self.assertFalse(snake.check_move([0, 1], True))

    def test_check_move_nofood_nocross(self):
        snake = Snake()
        snake.body = [[1, 0], [1, 1], [0, 0]]
        snake.play_field_size = [10, 10]
        self.assertTrue(snake.check_move([0, 1], False))

    def test_check_move_food_cross(self):
        snake = Snake()
        snake.body = [[1, 0], [1, 1], [0, 0]]
        snake.play_field_size = [10, 10]
        self.assertFalse(snake.check_move([0, 1], True))

    def test_check_move_around_nofood_nocross(self):
        snake = Snake()
        snake.body = [[0, 9], [0, 0], [9, 9]]
        snake.play_field_size = [10, 10]
        self.assertTrue(snake.check_move([9, 0], False))

    def test_check_move_around_food_cross(self):
        snake = Snake()
        snake.body = [[0, 9], [0, 0], [9, 9]]
        snake.play_field_size = [10, 10]
        self.assertFalse(snake.check_move([9, 0], True))

    def test_update(self):
        snake = Snake()
        position = [0, 0]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        new_position = [0, 0]
        snake.update(new_position, False)
        head_position = snake.get_head_position()
        self.assertEqual(head_position, new_position, f'wrong head position ({head_position} instead of {new_position})')


if __name__ == '__main__':
    unittest.main()
