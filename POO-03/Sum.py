#!/usr/bin/python
from Operation import Operation

class Sum(Operation):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.name = "sum"

    def calculateOperation(self):
        self.result = self.num1 + self.num2

    def displayResult(self):
        print("The " ,self.name, " between " ,self.num1, "and " ,self.num2, "is: " ,self.result)
