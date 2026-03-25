#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

#Cambios para rangos de factoriales

if len(sys.argv) == 1:
    entrada = input("Debe informar un número o rango (ej. 4-8): ")
else:
    entrada = sys.argv[1]

# Verificamos si la entrada tiene un guion (es decir, si es un rango)
if "-" in entrada:
    partes = entrada.split("-")
    desde = int(partes[0])
    hasta = int(partes[1])
    
    # Calculamos el factorial para cada número en ese rango
    for i in range(desde, hasta + 1):
        print("Factorial", i, "! es", factorial(i))
else:
    # Si no tiene guion, es un número solo normal
    num = int(entrada)
    print("Factorial", num, "! es", factorial(num))

