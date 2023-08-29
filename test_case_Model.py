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
        
   
if __name__ == "__main__":
    unittest.main()