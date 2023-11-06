import unittest
from play_field import Play_field


class Play_field_test(unittest.TestCase):
    def test_place_snake(self):
        play_field = Play_field()
        self.assertIsInstance(play_field, Play_field, 'cannot create a Play_field instance')
        play_field.place_snake((0, 0))
        # check if the snake has been correctly placed in the play field

    def test_check_move_valid_nofood(self):
        play_field = Play_field()
        self.assertIsInstance(play_field, Play_field, 'cannot create a Play_field instance')
        valid, food = play_field.check_move('S')
        self.assertTrue(valid)
        self.assertFalse(food)

    def test_update(self):
        play_field = Play_field()
        self.assertIsInstance(play_field, Play_field, 'cannot create a Play_field instance')
        play_field.update(('S'))
        # check if the move has been correctly performed


if __name__ == '__main__':
    unittest.main()
