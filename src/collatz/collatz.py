import matplotlib.pyplot as plt

def calcular_iteraciones(n):
    iteraciones = 0
    # NOTA: Se utiliza 3n+1 (Conjetura de Collatz real) 
    # ya que 2n+1 diverge al infinito y no converge a 1.
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iteraciones += 1
    return iteraciones

def main():
    numeros_n = []
    lista_iteraciones = []
    
    print("Calculando la secuencia de Collatz del 1 al 10000...")
    
    # Calculamos para los números del 1 al 10000
    for i in range(1, 10001):
        numeros_n.append(i)
        lista_iteraciones.append(calcular_iteraciones(i))
        
    print("Generando el gráfico...")
    
    # Creamos el gráfico de dispersión (scatter)
    # Eje X (abscisas) = iteraciones, Eje Y (ordenadas) = número n
    plt.scatter(lista_iteraciones, numeros_n, s=2, alpha=0.6, color='blue')
    
    # Etiquetas y título
    plt.title("Conjetura de Collatz (n hasta 10000)")
    plt.xlabel("Cantidad de Iteraciones (Abscisas)")
    plt.ylabel("Número inicial 'n' (Ordenadas)")
    
    # Mostramos el gráfico
    plt.show()

if __name__ == "__main__":
    main()