#!/usr/bin/python

class Division():

	def calculateDivision(self,num1, num2):
		self.num1 = num1
		self.num2 = num2
		if num2 == 0:
			print("No se puede dividir por 0...")
		else:
			result = (num1 / num2)
		return result
