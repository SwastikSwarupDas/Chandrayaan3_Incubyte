from chandrayaanFunc import chandrayaanFunc
import unittest   # The test framework


class Test_chandrayaan(unittest.TestCase):
    def test_chandrayaan(self):
        
        inPos = [0,0,0]
        inDir = "N"
        commands  = ['f','r','u','b','l']
        
        expected_direction = "N"
        expected_pos = [0, 1, -1]
        
        returned_direction, returned_position = chandrayaanFunc(inPos,inDir,commands)
        
        self.assertEqual(expected_direction, returned_direction)
        self.assertEqual(expected_pos, returned_position)


if __name__ == '__main__':
    unittest.main()