#Diseñar un programa que reciba el nombre y la edad de una persona, a partir de allí tiene que devolver como mensaje: el nombre de la persona seguido de la leyenda “puede votar”, si la persona es mayor a 16 años o bien la leyenda “debe esperar para votar” en caso contrario.

print("Bienvenidos al Registro de Votación")
print("-----------------------------------")
print("")

nombre = input("Por favor ingrese su nombre  ")
print ("")

edad = int (input("Por favor ingrese su edad  "))
print("")

if edad > 16:
    print(nombre +" puede votar")
else:
    print(nombre +" debe esperar para votar")
        