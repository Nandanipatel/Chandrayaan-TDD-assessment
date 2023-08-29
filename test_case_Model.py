import unittest
from Model import control_commands

class TestSpacecraftControl(unittest.TestCase):
     # test case for forward movement ( f )
    def test_forward(self):
        initial_position = (0, 0, 0)
        initial_direction = "N"
        commands = ["f"]
        final_position, final_direction = control_commands(initial_position, initial_direction, commands)
        self.assertEqual(final_position, (0, 1, 0))
        self.assertEqual(final_direction, "N")
        
    # test case for backward movement ( b )
    def test_backward(self):    
        initial_position = (0, 0, 0)
        initial_direction = "N"
        commands = ["b"]
        final_position, final_direction = control_commands(initial_position, initial_direction, commands)
        self.assertEqual(final_position, (0, -1, 0))
        self.assertEqual(final_direction, "N")

    # test for left movement ( l )
    def test_turn_left(self):
        initial_position = (0, 0, 0)
        initial_direction = "N"
        commands = ["l"]
        final_position, final_direction = control_commands(initial_position, initial_direction, commands)
        self.assertEqual(final_position, (0, 0, 0))
        self.assertEqual(final_direction, "W")

    # test for right movement ( r )    
    def test_turn_right(self):
        initial_position = (0, 0, 0)
        initial_direction = "N"
        commands = ["r"]
        final_position, final_direction = control_commands(initial_position, initial_direction, commands)
        self.assertEqual(final_position, (0, 0, 0))
        self.assertEqual(final_direction, "E")

    # test for up movement ( u )    
    def test_turn_up(self):
        initial_position = (0, 0, 0)
        initial_direction = "N"
        commands = ["u"]
        final_position, final_direction = control_commands(initial_position, initial_direction, commands)
        self.assertEqual(final_position, (0, 0, 0))
        self.assertEqual(final_direction, "Up")

    # test for down movement ( d )    
    def test_turn_down(self):
        initial_position = (0, 0, 0)
        initial_direction = "N"
        commands = ["d"]
        final_position, final_direction = control_commands(initial_position, initial_direction, commands)
        self.assertEqual(final_position, (0, 0, 0))
        self.assertEqual(final_direction, "Down")
        
        # test for multiple commands    
    def test_multiple_commands(self):
        initial_position = (0, 0, 0)
        initial_direction = "N"
        commands = ["f", "r", "u", "b", "l"]
        final_position, final_direction = control_commands(initial_position, initial_direction, commands)
        self.assertEqual(final_position, (0, 1, -1))
        self.assertEqual(final_direction, "N")
    
    # test for out of bounds
    def test_out_of_bounds(self):
        initial_position = (0, 0, 0)
        initial_direction = "N"
        commands = ["f"] * 200
        with self.assertRaises(ValueError):
            final_position, final_direction = control_commands(initial_position, initial_direction, commands)


   
if __name__ == "__main__":
    unittest.main()