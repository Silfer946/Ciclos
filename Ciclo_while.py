"""
ciclo while (Mientras)

while exp_booleana:
    instrucciones
    actualizacion de valores
"""

num = 1
while num < 10:
    print(f"Hello {num}")
    num = num + 5

# Mas operadores matematicos
"""
n = n + 5 == n += 5
n = n - 5 == n -= 5
n = n * 5 == n *= 5
n = n / 5 == n /= 5
"""
"""
Implementacion Do while (hacer, hasta) en python


while True:
   instrucciones 
   if exp_bool:
      break
"""

while True:
    option = input("Escribe salir: ")
    if option.upper == "salir":
        break