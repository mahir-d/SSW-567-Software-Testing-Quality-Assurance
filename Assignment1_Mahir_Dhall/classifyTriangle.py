# HW01
# Name: Mahir Dhall
#CWID: 10445966

import unittest

"""
Was confused about the type of inputs to be expected float or int in order to do a type check for invalid inputs 
How to check for invalid triangle 
Check for floating point precision
Should i test for good and bad route?
What should be printed in the text file/report 
Type of input
Type of output to equate 
File distribution
Design of the funciton 
"""


def classify_triangle(a, b, c) -> str:

    f = open("output.txt", "a")
    f.write(f"Input --> a = {a}, b = {b}, c = {c} \n")

    # Checks for data type of the lengths
    if type(a) != float or type(b) != float or type(c) != float:
        f.write("length of sides should be of type float \n")
        f.close()
        return "length of sides should be of type float"

    # rounds each side to precision of 2
    a = round(a, 2)
    b = round(b, 2)
    c = round(c, 2)

    # Checks for negative values
    if a < 0 or b < 0 or c < 0:
        f.write("Length of sides cannot be negative \n")
        f.close()
        return "Length of sides cannot be negative"

    # checks for invalid triangle
    if a > b+c or b > a+c or c > a+b:
        f.write("This is not a valid Triangle \n")
        f.close()
        return "This is not a valid Triangle"

    # Checks for equilateral triangle
    if a == b == c:
        f.write("This is an equilateral Triangle \n")
        f.close()
        return "This is an equilateral Triangle"

    # Checks for isosceles triangle
    if a == b or a == c or b == c:
        f.write("This is an isosceles Triangle \n")
        f.close()
        return "This is an isosceles Triangle"

    # Checks for right angle triangle
    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        f.write("This is a right angle Triangle \n")
        f.close()
        return "This is a right angle Triangle"

    # If nothing else than classifys it as a scalene triangle
    f.write("This is a scalene Trianlge \n")
    f.close()
    return "This is a scalene Trianlge"


class TriangleTest(unittest.TestCase):

    def test_type(self):

        value = classify_triangle("A", 1.0, 2.0)
        """ ~Test to check for correct input data type~ """
        self.assertEqual(value,
                         "length of sides should be of type float")

    def test_negative(self):

        value = classify_triangle(-1.0, 2.0, 3.0)
        """ ~Test to check for negative values in input~ """
        self.assertEqual(value,
                         "Length of sides cannot be negative")

    def test_validity(self):

        value = classify_triangle(5.0, 2.0, 2.0)
        """ ~Test to check for a valid triangle~ """
        self.assertEqual(value,
                         "This is not a valid Triangle")

    def test_equilateral(self):

        value = classify_triangle(5.00002, 5.00004, 5.0007)
        """ ~Test to check correct classification of equilateral triangle~ """
        self.assertEqual(value,
                         "This is an equilateral Triangle")

    def test_isosceles(self):

        value = classify_triangle(5.00002, 5.00004, 4.0007)
        """ ~Test to check correct classification of isosceles triangle~ """
        self.assertEqual(value,
                         "This is an isosceles Triangle")

    def test_right(self):

        value = classify_triangle(4.0, 5.0, 3.0)
        """ ~~Test to check correct classification of right angle triangle~ """
        self.assertEqual(value,
                         "This is a right angle Triangle")

    def test_scalene(self):
        value = classify_triangle(7.0, 12.00, 15.006)
        """ ~Test to check correct classification of a scalene triangle~ """
        self.assertEqual(value, "This is a scalene Trianlge")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
