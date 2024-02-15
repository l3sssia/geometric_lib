import unittest
from tests import RectangleTestCase, SquareTestCase, CircleTestCase, TriangleTestCase
import tests

"""
Run all tests in module "tests"
"""
def GeometricSuite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromModule(tests))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(GeometricSuite())
