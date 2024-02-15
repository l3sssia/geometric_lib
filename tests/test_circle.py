import circle
import unittest

class CircleTestCase(unittest.TestCase):
   def test_zero_mul(self):
      res = circle.area(0)
      self.assertEqual(res, 0)
      res = circle.perimeter(0)
      self.assertEqual(res, 0)

   def test_negative(self):
      with self.assertRaises(ValueError):
         circle.area(-2)
      with self.assertRaises(ValueError):
         circle.area(-3)

if __name__ == '__main__':
    unittest.main()