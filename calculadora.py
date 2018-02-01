#!/usr/bin/python3

import sys

op = sys.argv[1]
número1 = sys.argv[2]
número2 = sys.argv[3]

#control de argumentos
if len(sys.argv) != 4:
	sys.exit("Error número de argumentos: Introduce una operación (suma, resta, multiplicación o división) número1 número2")

try:
	número1 = float(número1)
	número2 = float(número2)
except ValueError:
	print("Los dos valores introducidos deben ser de tipo FLOAT")
	
if op == "suma":
	print("La suma es: ", número1 + número2)
elif op == "resta":
	print("La resta es: ", número1 - número2)
elif op == "multiplicación":
	print("La multiplicación es: ", número1 * número2)
elif op == "división":
	if número2 == 0:
		print("Error: No se puede dividir entre 0")
	else:		
		print("La división es: ", número1 / número2)
else:
	print("La operación debe ser: suma, resta, multiplicación o división, ", op, "es inválido")
	
	 	
