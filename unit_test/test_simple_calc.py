import unittest
import simple_calc

# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

class TestSimpleCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(simple_calc.add(3,1), 4)
        self.assertNotEqual(simple_calc.add(2,2), 5)
        self.assertIsInstance(simple_calc.add(1,1), int)
        
    def test_substract(self):
        self.assertEqual(simple_calc.substract(1,1), 0)
        self.assertNotEqual(simple_calc.substract(1,0), 0)
        self.assertIsInstance(simple_calc.substract(1,1), int)
        
    def test_multiply(self):
        self.assertEqual(simple_calc.multiply(2,3), 6)
        self.assertNotEqual(simple_calc.multiply(1,0), 1)
        self.assertIsInstance(simple_calc.multiply(1,1), int)
        
    def test_divide(self):
        self.assertEqual(simple_calc.divide(5,2), 2.5)
        self.assertEqual(simple_calc.divide(-1,-1), 1)
        
        with self.assertRaises(ZeroDivisionError):
            simple_calc.divide(13,0)

if __name__ == "__main__":
    unittest.main()