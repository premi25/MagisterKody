import unittest
from chebyshev_metric import calculateChebyshev
from DataPointClass import DataPoint

class ChebyshevMetricTestCase(unittest.TestCase):
    def test_ChebyshevMetricWith2Points(self):
        point1 = DataPoint(value=[0.9,0.8,0.7])
        point2 = DataPoint(value=[0.0,0.1,0.2])
        resultExpected = 0.9
        resultReceived = calculateChebyshev([point1,point2])
        self.assertEqual(resultReceived, resultExpected)
    def test_ChebyshevMetricWith1Point(self):
        point1 = DataPoint(value=[0.9,0.8,0.7])
        resultExpected = 0
        resultReceived = calculateChebyshev([point1])
        self.assertEqual(resultReceived, resultExpected)
    def test_ChebyshevMetricWith0Points(self):
        resultExpected = "List's length should be in range from 1 to 2!"
        with self.assertRaises(ValueError) as ve:
            calculateChebyshev([])
        self.assertEqual(ve.exception.args[0], resultExpected)
    
    
if __name__ == "__main__":
    unittest.main()

