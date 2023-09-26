from Functions import solve
from math import radians
import unittest

def roundValues(result):
    if (len(result) > 2):
        for i in range(0, 6): # Rounds each of the solved values to 2 places
            result[i] = round(result[i], 2)
    else :
        for i in range(0, len(result)):
            for j in range(0, 6):
                result[i][j] = round(result[i][j], 2)

global validTriangle
validTriangle = [3, 4, 5, 36.87, 53.13, 90]


class TestTriangles(unittest.TestCase):
    
    #tests all functions with a 3 - 4 - 5 triangle
    
    def testSideSideSide(self):
        testTriangle = solve(3, 4, 5, None, None, None)
        roundValues(testTriangle)
        self.assertEqual(testTriangle, validTriangle)

    def testAngleAngleAngleSide(self):
        testTriangle = solve(3, None, None, radians(36.87), radians(53.13), None)
        roundValues(testTriangle)
        self.assertEqual(testTriangle, validTriangle)
    
    def testSideAngleSide(self):
        testTriangle = solve(3, None, 5, None, None, radians(90))
        roundValues(testTriangle)
        self.assertEqual(testTriangle, validTriangle)
    
    def testAngleSideAngle(self):
        testTriangle = solve(None, None, 5, radians(36.87), radians(53.13), None)
        roundValues(testTriangle)
        self.assertEqual(testTriangle, validTriangle)
    
    def testAngleAngleSide(self):
        testTriangle = solve(3, None, None, radians(36.87), radians(53.13), None)
        roundValues(testTriangle)
        self.assertEqual(testTriangle, validTriangle)
    
    def testSideSideAngle(self): #Ambiguous case creates two triangles
        secondCase = [3, 4, 1.4, 36.87, 126.87, 16.26]
        testTriangle = solve(3, 4, None, radians(36.87), None, None)
        roundValues(testTriangle)
        self.assertEqual(testTriangle, (validTriangle, secondCase))

unittest.main()