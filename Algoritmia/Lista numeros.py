import random

# Creamos la lista con 20 números aleatorios
lista = []
for i in range(20):
    numeroAleatorio = random.randint(1, 100)
    lista.append(numeroAleatorio)

print("Lista de números:", lista)

# Pedimos el número que el usuario quiere buscar
buscado = int(input("¿Qué número quieres buscar?: "))

# Buscamos el número en la lista
if buscado in lista:
    posicion = lista.index(buscado)
    print(f"¡Número encontrado en la posición {posicion}!")
else:
    print("Número no encontrado")
