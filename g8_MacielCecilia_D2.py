#Diseñar un programa que dados una serie de 15 números pueda devolver: el mayor, el menor, la suma y el promedio de todos los números (los 15 números deberán estar ingresados en lista de forma estática).

print("Lista de 15 números:  ")
lista_de_números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print (lista_de_números)

print("\nMayor:")
print (max(lista_de_números))
'''print(max([int(num) for num in lista_de_números]))'''

print("\nMenor:")
print (min(lista_de_números))

print("\nSuma:")
suma = 0
for lista in lista_de_números:
    suma += lista
print(suma)

print("\nPromedio: ")
promediar= suma/len(lista_de_números)
print(promediar)