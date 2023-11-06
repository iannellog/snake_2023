import unittest
from play_field import Play_field


class Play_field_test(unittest.TestCase):

    def test_create(self):
        play_field = Play_field(10, 10, [], [])
        self.assertIsInstance(play_field, Play_field, 'cannot create a Play_field instance')

    def test_check_move_N_valid_nofood(self):
        play_field = Play_field(10, 10, [], [])
        snake_head_position = [0, 0]
        valid, new_position, food = play_field.check_move(snake_head_position, 'N')
        self.assertTrue(valid)
        self.assertGreaterEqual(new_position[0], 0, 'invalid snake position')
        self.assertLess(new_position[0], play_field.height, 'invalid snake position')
        self.assertGreaterEqual(new_position[1], 0, 'invalid snake position')
        self.assertLess(new_position[1], play_field.width, 'invalid snake position')
        self.assertFalse(food)

    def test_check_move_E_valid_nofood(self):
        play_field = Play_field(10, 10, [], [])
        snake_head_position = [0, 0]
        valid, new_position, food = play_field.check_move(snake_head_position, 'N')
        self.assertTrue(valid)
        self.assertGreaterEqual(new_position[0], 0, 'invalid snake position')
        self.assertLess(new_position[0], play_field.height, 'invalid snake position')
        self.assertGreaterEqual(new_position[1], 0, 'invalid snake position')
        self.assertLess(new_position[1], play_field.width, 'invalid snake position')
        self.assertFalse(food)

    def test_check_move_S_valid_nofood(self):
        play_field = Play_field(10, 10, [], [])
        snake_head_position = [0, 0]
        valid, new_position, food = play_field.check_move(snake_head_position, 'N')
        self.assertTrue(valid)
        self.assertGreaterEqual(new_position[0], 0, 'invalid snake position')
        self.assertLess(new_position[0], play_field.height, 'invalid snake position')
        self.assertGreaterEqual(new_position[1], 0, 'invalid snake position')
        self.assertLess(new_position[1], play_field.width, 'invalid snake position')
        self.assertFalse(food)

    def test_check_move_W_valid_nofood(self):
        play_field = Play_field(10, 10, [], [])
        snake_head_position = [0, 0]
        valid, new_position, food = play_field.check_move(snake_head_position, 'N')
        self.assertTrue(valid)
        self.assertGreaterEqual(new_position[0], 0, 'invalid snake position')
        self.assertLess(new_position[0], play_field.height, 'invalid snake position')
        self.assertGreaterEqual(new_position[1], 0, 'invalid snake position')
        self.assertLess(new_position[1], play_field.width, 'invalid snake position')
        self.assertFalse(food)

    def test_check_move_NE_valid_nofood(self):
        play_field = Play_field(10, 10, [], [])
        snake_head_position = [0, 0]
        valid, new_position, food = play_field.check_move(snake_head_position, 'N')
        self.assertTrue(valid)
        self.assertGreaterEqual(new_position[0], 0, 'invalid snake position')
        self.assertLess(new_position[0], play_field.height, 'invalid snake position')
        self.assertGreaterEqual(new_position[1], 0, 'invalid snake position')
        self.assertLess(new_position[1], play_field.width, 'invalid snake position')
        self.assertFalse(food)

    def test_check_move_NW_valid_nofood(self):
        play_field = Play_field(10, 10, [], [])
        snake_head_position = [0, 0]
        valid, new_position, food = play_field.check_move(snake_head_position, 'N')
        self.assertTrue(valid)
        self.assertGreaterEqual(new_position[0], 0, 'invalid snake position')
        self.assertLess(new_position[0], play_field.height, 'invalid snake position')
        self.assertGreaterEqual(new_position[1], 0, 'invalid snake position')
        self.assertLess(new_position[1], play_field.width, 'invalid snake position')
        self.assertFalse(food)

    def test_check_move_SE_valid_nofood(self):
        play_field = Play_field(10, 10, [], [])
        snake_head_position = [0, 0]
        valid, new_position, food = play_field.check_move(snake_head_position, 'N')
        self.assertTrue(valid)
        self.assertGreaterEqual(new_position[0], 0, 'invalid snake position')
        self.assertLess(new_position[0], play_field.height, 'invalid snake position')
        self.assertGreaterEqual(new_position[1], 0, 'invalid snake position')
        self.assertLess(new_position[1], play_field.width, 'invalid snake position')
        self.assertFalse(food)

    def test_check_move_SW_valid_nofood(self):
        play_field = Play_field(10, 10, [], [])
        snake_head_position = [0, 0]
        valid, new_position, food = play_field.check_move(snake_head_position, 'N')
        self.assertTrue(valid)
        self.assertGreaterEqual(new_position[0], 0, 'invalid snake position')
        self.assertLess(new_position[0], play_field.height, 'invalid snake position')
        self.assertGreaterEqual(new_position[1], 0, 'invalid snake position')
        self.assertLess(new_position[1], play_field.width, 'invalid snake position')
        self.assertFalse(food)

    def test_check_move_S_novalid_nofood(self):
        play_field = Play_field(10, 10, [[1, 0]], [])
        snake_head_position = [2, 0]
        valid, new_position, food = play_field.check_move(snake_head_position, 'N')
        self.assertFalse(valid)
        self.assertGreaterEqual(new_position[0], 0, 'invalid snake position')
        self.assertLess(new_position[0], play_field.height, 'invalid snake position')
        self.assertGreaterEqual(new_position[1], 0, 'invalid snake position')
        self.assertLess(new_position[1], play_field.width, 'invalid snake position')
        self.assertFalse(food)

    def test_check_move_S_valid_food(self):
        play_field = Play_field(10, 10, [], [[1, 0]])
        snake_head_position = [2, 0]
        valid, new_position, food = play_field.check_move(snake_head_position, 'N')
        self.assertTrue(valid)
        self.assertGreaterEqual(new_position[0], 0, 'invalid snake position')
        self.assertLess(new_position[0], play_field.height, 'invalid snake position')
        self.assertGreaterEqual(new_position[1], 0, 'invalid snake position')
        self.assertLess(new_position[1], play_field.width, 'invalid snake position')
        self.assertTrue(food)

    def test_update_remove_food(self):
        play_field = Play_field(10, 10, [], [[1, 0]])
        play_field.update([1, 0])
        valid, new_position, food = play_field.check_move([0, 0], 'S')
        self.assertFalse(food)


if __name__ == '__main__':
    unittest.main()
