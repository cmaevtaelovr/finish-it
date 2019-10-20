def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def divide(a,b):
    return a//b
def multiply(a,b):
    return a*b

## add is to add two integers together

## minus is to calculate a-b

## divide is to calculate a//b
## try to build some error in the section 


## max(a,b) will return which number is bigger
import unittest

class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,2),3)

    def test_minus(self):
        self.assertEqual(minus(3,2),1)
        
    def test_divide(self):
        self.assertEqual(divide(10,5),2)
        
    def test_max(self):
        self.assertEqual(max(5,6),6)
        
    def test_multiply(self):
        self.assertEqual(multiply(10,2),20)
        
if __name__ == '__main__':
    unittest.main()
