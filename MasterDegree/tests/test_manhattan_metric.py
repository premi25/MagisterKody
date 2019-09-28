import unittest
from manhattan_metric import calculateManhattan
from DataPointClass import DataPoint

class ManhattanMetricTestCase(unittest.TestCase):
    def test_ManhattanMetricWith2Points(self):
        point1 = DataPoint(value=[0.1,0.2,0.3])
        point2 = DataPoint(value=[0.2,0.3,0.4])
        resultExpected = 0.3
        resultReceived = calculateManhattan([point1,point2])
        self.assertEqual(resultReceived, resultExpected)
    def test_ManhattanMetricWith1Point(self):
        point1 = DataPoint(value=[0.1,0.2,0.3])
        resultExpected = 0
        resultReceived = calculateManhattan([point1])
        self.assertEqual(resultReceived, resultExpected)
    def test_ManhattanMetricWith0Points(self):
        resultExpected = "List's length should be in range from 1 to 2!"
        with self.assertRaises(ValueError) as ve:
            calculateManhattan([])
        self.assertEqual(ve.exception.args[0], resultExpected)
    
    
if __name__ == "__main__":
    unittest.main()

