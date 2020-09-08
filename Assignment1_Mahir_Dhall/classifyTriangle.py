import unittest
# from classifyTriangle import classify_triangle
"""
Was confused about the type of inputs to be expected float or int in order to do a type check for invalid inputs 
How to check for invalid triangle 
Check for floating point precision
Should i test for good and bad route?
What should be printed in the text file/report 
"""


def classify_triangle(a, b, c, f) -> str:

    f.write(f"Input --> a = {a}, b = {b}, c = {c} \n")
    # Checks for data type of the lengths
    if type(a) != float or type(b) != float or type(c) != float:
        f.write("length of sides should be of type float \n")
        return "length of sides should be of type float"

    # rounds each side to precision of 2
    a = round(a, 2)
    b = round(b, 2)
    c = round(c, 2)

    # Checks for negative values
    if a < 0 or b < 0 or c < 0:
        f.write("Length of sides cannot be negative \n")
        return "Length of sides cannot be negative"

    # checks for invalid triangle
    if a > b+c or b > a+c or c > a+b:
        f.write("This is not a valid Triangle \n")
        return "This is not a valid Triangle"

    if a == b == c:
        f.write("This is an equilateral Triangle \n")
        return "This is an equilateral Triangle"

    if a == b or a == c or b == c:
        f.write("This is an isosceles Triangle \n")
        return "This is an isosceles Triangle"

    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        f.write("This is a right angle Triangle \n")
        return "This is a right angle Triangle"

    f.write("This is a scalene Trianlge \n")
    return "This is a scalene Trianlge"


class TriangleTest(unittest.TestCase):

    def test_type(self):
        f = open("test.txt", "a")
        value = classify_triangle("A", 1.0, 2.0, f)
        f.close()
        self.assertEqual(value,
                         "length of sides should be of type float")

    def test_negative(self):
        f = open("test.txt", "a")
        value = classify_triangle(-1.0, 2.0, 3.0, f)
        f.close()
        self.assertEqual(value,
                         "Length of sides cannot be negative")

    def test_validity(self):
        f = open("test.txt", "a")
        value = classify_triangle(5.0, 2.0, 2.0, f)
        f.close()
        self.assertEqual(value,
                         "This is not a valid Triangle")

    def test_equilateral(self):
        f = open("test.txt", "a")
        value = classify_triangle(5.00002, 5.00004, 5.0007, f)
        f.close()
        self.assertEqual(value,
                         "This is an equilateral Triangle")

    def test_isosceles(self):
        f = open("test.txt", "a")
        value = classify_triangle(5.00002, 5.00004, 4.0007, f)
        f.close()
        self.assertEqual(value,
                         "This is an isosceles Triangle")

    def test_right(self):
        f = open("test.txt", "a")
        value = classify_triangle(4.0, 5.0, 3.0, f)
        f.close()
        self.assertEqual(value,
                         "This is a right angle Triangle")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
