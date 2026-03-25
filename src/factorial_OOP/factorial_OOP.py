import sys

# Definimos la clase solicitada
class Factorial:
    # Método constructor
    def __init__(self):
        pass

    # Función interna para calcular un factorial individual
    def _calcular(self, num):
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

    # Método solicitado que calcula los factoriales entre un mínimo y un máximo
    def run(self, min_val, max_val):
        for i in range(min_val, max_val + 1):
            print("Factorial", i, "! es", self._calcular(i))

# --- Lógica principal para interactuar con la consola ---
if __name__ == "__main__":
    if len(sys.argv) == 1:
        entrada = input("Debe informar un número o rango (ej. 4-8, -10, 10-): ")
    else:
        entrada = sys.argv[1]

    # Parseamos la entrada igual que en el script anterior
    min_val = 1
    max_val = 1

    if "-" in entrada:
        partes = entrada.split("-")
        min_val = 1 if partes[0] == "" else int(partes[0])
        max_val = 60 if partes[1] == "" else int(partes[1])
    else:
        min_val = int(entrada)
        max_val = int(entrada)

    # 1. Instanciamos el objeto de la clase Factorial
    calculadora = Factorial()
    
    # 2. Llamamos al método run() pasándole los límites numéricos
    calculadora.run(min_val, max_val)