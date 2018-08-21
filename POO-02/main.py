#!/usr/bin/python
"Calculadora basica"

"Importar la clase Sum del archivo Sum.py"
from Sum import Sum
from Multiplication import Multiplication
from Subtract import Subtract
from Division import Division

print("Ingrese un numero:")
numeroUno = input()
print("Ingrese otro numero:")
numeroDos = input()

sumar = Sum()
print sumar.calculateSum(numeroUno,numeroDos)

restar = Subtract()
print restar.calculateSubtract(numeroUno,numeroDos)

dividir = Division()
print dividir.calculateDivision(numeroUno,numeroDos)

multiplicar = Multiplication()
print multiplicar.calculateMultiplication(numeroUno,numeroDos)
