#  Pedimos un número al usuario

numero_entero = input("Por favor, ingresa un número entero: ")

# Casteamos el dato ingresado a un número entero con int()

numero_entero = int(numero_entero) #Así, la variable ahora tiene un entero, no texto.

# Mostramos el número entero usando print

print("El número que ingresaste es: " , numero_entero)

# Pedimos al user un número decimal 

numero_decimal = input("Por favor, ahora ingresa un número decimal: ")

# Convertimos el dato ingresado a decimal usando float()

numero_decimal = float(numero_decimal) # Ahora la variable es un número decimal.

# Mostramos el número decimal usando print

print("el número que ingresaste es: " , numero_decimal)

# realizamos una operación con los números ingresados anteriormente.

suma = numero_entero + numero_decimal
print("La suma de ambos números ingresados es: " , suma)