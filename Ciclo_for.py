"""
Ciclo for en python

Permite realizar una serie de instrucciones
una cantidad determinada de veces

Estructura:
for i in [1...n]:
    instrucciones

range(fin) 
     range(3) [0, 1, 2]
range(inicio, fin)
      range(4, 7) [4, 5, 6]
range(inicio, fin, pasos)
      range(2, 9, 2) [2, 4, 6, 8]    
"""
# Ejemplo: Imprimir los numeros del 1 al 10
for i in range(10):
    print(f"Num: { i + 1 }, vuelta { i }")

#Ejemplo: Imprimir los numeros del 10 al 20
for i in range(10, 21):
    print(f"Num: { i }")

#Imprimir pares del 0 al 20
for i in range(0, 21, 2):
    print(f"{ i }")    

# Imprimir la tabla de multiplicar de un numero leidpo desde el teclado
n = int(input("Ingresa un numero:"))
for i in range(11):
    print(f"{ n } x { i } = { i*n }")