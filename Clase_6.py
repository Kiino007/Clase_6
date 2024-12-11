# 1. imprimir los numeros del 1 al 10

print("Imprimir los numeros del 1 al 10")

n=1
while n <= 10:
    print(n)
    n += 1



# Sumar los primeros 100 numeros naturales
    
print("Suma de los primeros 100 numeros naturales")

n = 1
suma = 0

while n <= 100:
    suma += n
    n += 1

print(f"suma: {suma}")



# Imrpima numeros del 1 al numero ingresado

print("Imprimir los numeros del 1 al numero que usted a ingresado")

num = int(input("Ingresa un numero entero positivo"))
n=1

while n <= num:
    print(n)
    n += 1



# imprima los primeros 10 numeros pares

print("Imprimir los primeros 10 numeros pares")

n = int(input("Ingresa el numero desde donde empezar a buscar pares"))
contador = 0

while contador < 10:
    if n % 2 ==0:
        print(n)
        contador += 1
    
    n += 1

