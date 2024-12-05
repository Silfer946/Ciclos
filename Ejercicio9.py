op💥💯, Tú
4/11/2024
condicionales if:

evaluan expresiones boolanas

estructura:

If expressen:

Instrucciones

alser

Instrucciones

12 If expreston:

Instrucciones

11 alif expreston

Instrucciones

else:

Instrucciones

print("programa que verifica si un numero es positivo") mum-Int(Input("Ingresa un numero;"))

Apreguntar el numero es mayor

print("el numero es positivo")

elser

print("el numero es negativo")

print("programa que verifica si un numero es par") nus Int(input("Ingresa un numero"))

If num 20

print("Es un numro par")

elser

print("Es in numero Inpar")
09:30

116 kB

19:27
F-CID-001-R10-ENTREVISTA-INICIAL_2...pdf
3 páginas•PDF•474 kB
F-CID-001-R10-ENTREVISTA-INICIAL_2...pdf
20:29
10 F-CID-008-R05-VAK-Cuestionario-para-determinar-el-ESTILO-DE-APRENDIZAJE 230124.pdf
1 página•PDF•381 kB
10 F-CID-008-R05-VAK-Cuestionario-para-determinar-el-ESTILO-DE-APRENDIZAJE 230124.pdf
20:29
9 F-CID-009-R04-TEST-DE-INTELIGENCIAS-MÚLTIPLES 230124.pdf
2 páginas•PDF•230 kB
9 F-CID-009-R04-TEST-DE-INTELIGENCIAS-MÚLTIPLES 230124.pdf
20:29
5/11/2024
Diferenciar y aplicabilidad de distintas herramientas digitales: 
De búsqueda de información y contenidos 
De filtrado y selección y selección de la información 
De creación de contenidos 
De organización de contenidos 
De difusión 
De comunicación
11:26

😢
10/11/2024
T
Top💥💯
Sin título
3 MB
19:10
Q
21:09
HOY
T
Top💥💯
'''
Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''
print("Identificador de vocales (para salir ingresa espacio)")
while True:
    l = input("Escribe una letra: ")
    l = l.upper()
    
    if l == " ":
        break
    else:
        if l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U' :
            print("ES VOCAL")
        else:
            print("NO ES VOCAL")
09:16
'''
Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''
limite_in = int(input("Escribe el limite inferior: "))
limite_su = int(input("Escribe el limite superior: "))
for i in range(limite_in,limite_su + 1):
    if i % 2 == 0:
        print(i)
09:19
'''
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
'''
limite_in = int(input("Escribe el limite inferior: "))
limite_su = int(input("Escribe el limite superior: "))
suma = 0
contf = 0
conti = 0
while True:
    if limite_in >= limite_su:
        limite_in=int(input('El limite inferior no puede ser mayor o igual al superior, REESCRIBELO: '))
    else:
        break
    
while True :
    n = int(input('Escribe un numero: '))
    if n == 0:
        break
    else: 
        if n == limite_in or n == limite_su:
            conti += 1
        else:
            if n > limite_in and n < limite_su:
                suma += n
            else:
                contf += 1
                
                
print(f'La suma de los números que están dentro del intervalo es: {suma}')
print(f'Los números que están fuera del intervalo fueron: {contf}')
print(f'Los números que fueron iguales a los intervalos fueron: {conti}')