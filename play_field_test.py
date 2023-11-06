import unittest
from play_field import Play_field


class Play_field_test(unittest.TestCase):

    def test_create(self):
        play_field = Play_field(10, 10, [], [])
        self.assertIsInstance(play_field, Play_field, 'cannot create a Play_field instance')

    def test_check_move_S_valid_nofood(self):
        play_field = Play_field(10, 10, [], [])
        valid, new_position, food = play_field.check_move([0, 0], 'S')
        self.assertTrue(valid)
        self.assertGreaterEqual(new_position[0], 0, 'invalid snake position')
        self.assertLess(new_position[0], play_field.height, 'invalid snake position')
        self.assertGreaterEqual(new_position[1], 0, 'invalid snake position')
        self.assertLess(new_position[1], play_field.width, 'invalid snake position')
        self.assertFalse(food)

    def test_update(self):
        play_field = Play_field(10, 10, [], [])
        play_field.update([0, 0])
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
