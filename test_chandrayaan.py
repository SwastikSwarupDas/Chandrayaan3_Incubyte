from chandrayaanFunc import chandrayaanFunc
import unittest   # The test framework


class Test_chandrayaan(unittest.TestCase):
    def test_chandrayaan(self):
        
        inPos = [0,0,0]
        inDir = "N"
        commands  = ['f','b','r','u','f']
        
        expected_direction = "U"
        expected_pos = [0, 0, 1]
        
        returned_position, returned_direction = chandrayaanFunc(inPos,inDir,commands)
        
        self.assertEqual(expected_direction, returned_direction)
        self.assertEqual(expected_pos, returned_position)


if __name__ == '__main__':
    unittest.main()