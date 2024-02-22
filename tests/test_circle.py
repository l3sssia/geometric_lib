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
   
   def test_precision(self):
      res = circle.area(10)
      delta_ = 0.00001
      self.assertAlmostEqual(314.159265358, res, None,  delta= delta_)
      res = circle.perimeter(10)
      self.assertAlmostEqual(62.8318530716, res, None, delta = delta_)
if __name__ == '__main__':
    unittest.main()