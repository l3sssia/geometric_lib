import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
      res = triangle.area(10, 0)
      self.assertEqual(res, 0)
      res = triangle.area(0, 10)
      self.assertEqual(res, 0)
       
   def test_square_mul(self):
      res = triangle.area(10, 10)
      self.assertEqual(res, 50)

   def test_sum(self):
      res = triangle.perimeter(10, 2, 5)
      self.assertEqual(res, 17)

   def test_negative(self):
      with self.assertRaises(ValueError):
         triangle.area(-10, 1)
      with self.assertRaises(ValueError):
         triangle.area(10, -1)
      with self.assertRaises(ValueError):
         triangle.perimeter(10, 1, -12)
      with self.assertRaises(ValueError):
         triangle.perimeter(10, -1, 12)
      with self.assertRaises(ValueError):
         triangle.perimeter(-10, 1, 12)

if __name__ == '__main__':
    unittest.main()