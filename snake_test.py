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
        position = [0, 0]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        snake.update([0, 1], True)
        snake.update([1, 1], True)
        snake.update([1, 0], True)
        # snake.body: [[1, 0], [1, 1], [0, 1], [0, 0]]
        self.assertTrue(snake.check_move([2, 0], False))

    def test_check_move_nofood_overlap(self):
        snake = Snake()
        position = [0, 0]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        snake.update([0, 1], True)
        snake.update([1, 1], True)
        snake.update([1, 0], True)
        # snake.body = [[1, 0], [1, 1], [0, 1], [0, 0]]
        self.assertFalse(snake.check_move([0, 1], False))

    def test_check_move_food_nooverlap(self):
        snake = Snake()
        position = [0, 0]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        snake.update([0, 1], True)
        snake.update([1, 1], True)
        snake.update([1, 0], True)
        # snake.body = [[1, 0], [1, 1], [0, 1], [0, 0]]
        self.assertTrue(snake.check_move([2, 0], True))

    def test_check_move_food_overlap(self):
        snake = Snake()
        position = [0, 0]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        snake.update([0, 1], True)
        snake.update([1, 1], True)
        snake.update([1, 0], True)
        # snake.body = [[1, 0], [1, 1], [0, 1], [0, 0]]
        self.assertFalse(snake.check_move([0, 1], True))

    def test_check_move_nofood_nocross(self):
        snake = Snake()
        position = [0, 0]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        snake.update([1, 1], True)
        snake.update([1, 0], True)
        # snake.body = [[1, 0], [1, 1], [0, 0]]
        self.assertTrue(snake.check_move([0, 1], False))

    def test_check_move_food_cross(self):
        snake = Snake()
        position = [0, 0]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        snake.update([1, 1], True)
        snake.update([1, 0], True)
        # snake.body = [[1, 0], [1, 1], [0, 0]]
        self.assertFalse(snake.check_move([0, 1], True))

    def test_check_move_around_nofood_nocross(self):
        snake = Snake()
        position = [9, 9]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        snake.update([0, 0], True)
        snake.update([0, 9], True)
        # snake.body = [[0, 9], [0, 0], [9, 9]]
        self.assertTrue(snake.check_move([9, 0], False))

    def test_check_move_around_food_cross(self):
        snake = Snake()
        position = [9, 9]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        snake.update([0, 0], True)
        snake.update([0, 9], True)
        # snake.body = [[0, 9], [0, 0], [9, 9]]
        self.assertFalse(snake.check_move([9, 0], True))

    def test_update_nofood(self):
        snake = Snake()
        position = [0, 0]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        new_position = [1, 0]
        len_snake_body_before = len(snake.body)
        len_snake_tail_before = len(snake.tail)
        snake.update(new_position, False)
        head_position = snake.get_head_position()
        self.assertEqual(head_position, new_position, f'wrong head position ({head_position} instead of {new_position})')
        self.assertEqual(len_snake_body_before, len(snake.body))
        self.assertEqual(len_snake_tail_before+1, len(snake.tail))

    def test_update_food(self):
        snake = Snake()
        position = [0, 0]
        play_field_size = [10, 10]
        snake.place_in_start_position(position, play_field_size)
        new_position = [1, 0]
        len_snake_body_before = len(snake.body)
        len_snake_tail_before = len(snake.tail)
        snake.update(new_position, True)
        head_position = snake.get_head_position()
        self.assertEqual(head_position, new_position, f'wrong head position ({head_position} instead of {new_position})')
        self.assertEqual(len_snake_body_before+1, len(snake.body))
        self.assertEqual(len_snake_tail_before, len(snake.tail))


if __name__ == '__main__':
    unittest.main()
