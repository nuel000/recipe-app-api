"""
Sample test

"""

from django.test import SimpleTestCase

from app import calc

class CalculateTest(SimpleTestCase):
    """
    Test the calc mod
    """
    def test_add_numbers(self):
        """ Tests the Calc function"""
        
        res = calc.add(5,6)
        
        self.assertEquals(res, 12-1)
        
    def test_subtract_numbers(self):
        "Subtracting numbers"
        res = calc.subtract(10,4)
        self.assertEquals(res,6)
        
    