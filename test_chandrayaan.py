from chandrayaanFunc import chandrayaanFunc
import unittest   # The test framework


class Test_chandrayaan(unittest.TestCase):
    def test_chandrayaan(self):
        
        inPos = [0,0,0]
        inDir = "N"
        commands = ['f', 'r', 'u', 'd', 'u','f','f','r','r','f','f','l','d','f','r','f','r','u']
        
        expected_direction = "U"
        expected_pos = [-2, 1, 0]
        
        returned_position, returned_direction = chandrayaanFunc(inPos,inDir,commands)
        
        self.assertEqual(expected_direction, returned_direction)
        self.assertEqual(expected_pos, returned_position)


if __name__ == '__main__':
    unittest.main()