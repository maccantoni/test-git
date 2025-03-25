# TP1 - ESTRUCTURAS SECUENCIALES | MACARENA CANTONI

# 1. Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 

print("¡Hola Mundo!")

# 2. Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 

nombre = input("Hola! Ingresa tu nombre: ")
print(f"Hola {nombre}!")

# 3. Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingresa tu nombre")
apellido = input("Ahora ingresa tu apellido")
edad = input("Que edad tienes?")
residencia = input("Donde vives?")

print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

# 4. Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingresa el radio del círculo"))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio

print(f"El área del círculo es {area} y su perímetro es {perimetro}")

# 5. Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Ingresa una catidad de segundos"))
horas = segundos / 3600 

print(f"{segundos} segundos serían {horas} horas")

# 6. Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.  

numero = int(input("Ingresa un número"))
tabla0 = numero * 0
tabla1 = numero * 1
tabla2 = numero * 2
tabla3 = numero * 3
tabla4 = numero * 4
tabla5 = numero * 5
tabla6 = numero * 6
tabla7 = numero * 7
tabla8 = numero * 8
tabla9 = numero * 9
tabla10 = numero * 10

print(f"{numero} * 0 = {tabla0}")
print(f"{numero} * 1 = {tabla1}")
print(f"{numero} * 2 = {tabla2}")
print(f"{numero} * 3 = {tabla3}")
print(f"{numero} * 4 = {tabla4}")
print(f"{numero} * 5 = {tabla5}")
print(f"{numero} * 6 = {tabla6}")
print(f"{numero} * 7 = {tabla7}")
print(f"{numero} * 8 = {tabla8}")
print(f"{numero} * 9 = {tabla9}")
print(f"{numero} * 10 = {tabla10}")




# 7. Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Ingresa un número entero"))
numero2 = int(input("Ahora ingresa otro número entero"))

suma = numero1 + numero2
division = numero1 / numero2
multi = numero1 * numero2
resta = numero1 - numero2

print(f"El resultado de la suma es {suma}")
print(f"El resultado de la división es {division}")
print(f"El resultado de la multiplicación es {multi}")
print(f"El resultado de la resta es {resta}")

# 8.  Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC = peso en kg / altura en m2.

peso = float(input("Ingresa tu peso en kg"))
altura = float(input("Ingresa tu altura en cm"))

imc = peso / altura

print(f"Tu IMC es de {imc}")

# 9. Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 

celsius = float(input("Ingresa la temperatura en Celcius"))
far = (celsius * 9/5) + 32

print(f"La temperatura {celsius}° equivale a {far} F")

# 10. Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números. 

numero1 = float(input("Ingresa un número"))
numero2 = float(input("Ingresa otro número"))
numero3 = float(input("Ingresa otro número mas"))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio es de {promedio}")

