# # 1. imprimir los numeros del 1 al 10

# print("Imprimir los numeros del 1 al 10")

# n=1
# while n <= 10:
#     print(n)
#     n += 1



# # Sumar los primeros 100 numeros naturales
    
# print("Suma de los primeros 100 numeros naturales")

# n = 1
# suma = 0

# while n <= 100:
#     suma += n
#     n += 1

# print(f"suma: {suma}")



# # Imrpima numeros del 1 al numero ingresado

# print("Imprimir los numeros del 1 al numero que usted a ingresado")

# num = int(input("Ingresa un numero entero positivo"))
# n=1

# while n <= num:
#     print(n)
#     n += 1



# # imprima los primeros 10 numeros pares

# print("Imprimir los primeros 10 numeros pares")

# n = int(input("Ingresa el numero desde donde empezar a buscar pares"))
# contador = 0

# while contador < 10:
#     if n % 2 ==0:
#         print(n)
#         contador += 1
    
#     n += 1

    


# # Imprima los pares desde el numero2 hasta el numero ingresado
    
# print("Imprimir los pares desde el numero2 hasta el numero ingresado")

# num = int(input("Ingrese el numero entero positivo"))
# n = 2

# while n <= num:
#     print(n)
#     n += 2



# #Calcular el factorial de un numero ingresado
    
# num = int(input("Ingrese el numero entero positivo"))
# resultado = 1

# while num > 0:
#     resultado *= num
#     num -= 1
# print(f"Factorial: {resultado}")


 
# # Sumar los digitos de un numero

# print("Sumar los digitos de un numero")

# num = int(input("Ingrese el numero entero positivo"))
# suma = 0

# while num > 0:
#     suma += num % 10
#     num //= 10
# print(f"Suma de los digitos {suma}")



# #Imprimir los numeros del 1 al 100 que sean multiplos de 3

# print("Imprimir los numeros del 1 al 100 que sean multiplos de 3")
# n = 1
# while n <= 100:
#     if n % 3 == 0:
#         print(n)
#     n += 1



# #Imprimir los numeros impares desde el 1 al numero ingresado
    
# print(Imprimir los numeros impares desde el 1 al numero ingresado)

# num = int(input("Ingrese el numero entero positivo"))
# n = 1

# while n < num:
#     if n % 2 != 0:
#         print(n)
#     n += 1



#Imprima la suma de los primeros pares del 1 al 100

print("Imprima la suma de los primeros pares del 1 al 100")

n = 2
suma = 0

while n < 100:
    suma += n
    n += 2
print(f"La suma de los pares es: {suma}")

