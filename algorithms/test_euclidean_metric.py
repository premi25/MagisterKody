import unittest
import math
from euclidean_metric import calculateEuclidean
from DataPointClass import DataPoint

class EuclideanMetricTestCase(unittest.TestCase):
    def test_EuclideanMetricWith2Points(self):
        point1 = DataPoint(value=[0.1,0.2,0.3])
        point2 = DataPoint(value=[0.2,0.3,0.4])
        resultExpected = round(math.pow(0.03, 0.5),5)
        resultReceived = calculateEuclidean([point1,point2])
        self.assertEqual(resultReceived, resultExpected)
    def test_EuclideanMetricWith1Point(self):
        point1 = DataPoint(value=[0.1,0.2,0.3])
        resultExpected = 0
        resultReceived = calculateEuclidean([point1])
        self.assertEqual(resultReceived, resultExpected)
    def test_EuclideanMetricWith0Points(self):
        resultExpected = "List's length should be in range from 1 to 2!"
        with self.assertRaises(ValueError) as ve:
            calculateEuclidean([])
        self.assertEqual(ve.exception.args[0], resultExpected)
    
    
if __name__ == "__main__":
    unittest.main()