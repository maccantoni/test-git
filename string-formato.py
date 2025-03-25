# F String (Concatenaciones)
# Se pueden usar en cualquier ámbito donde se necesite una cadena de caracteres y se concatenen partes literales y partes variables en una sintaxis mas amena.

# EJ 1

nombre = "Maca"
edad = 31

print("Tu nombre es: " ,nombre, "y tu edad es: " ,edad)
print("Tu nombre es: " + nombre + " y tu edad es: " + str(edad))
print(f"tu nombre es: {nombre} y tu edad es: {edad}") # Formatea las concatenaciones en una única cadena que inyecta las variables.

# EJ 2:

nombre = input("Ingrese su nombre")
edad = input(f"Ingrese su edad, {nombre}: ") # uso el f string para concatenar ambas variables y usar el dato de una en otra.

print(f"tu nombre es: {nombre} y tu edad es: {edad}")