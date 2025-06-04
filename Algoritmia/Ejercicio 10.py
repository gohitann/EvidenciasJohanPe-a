import random

# Creamos la lista con 20 números aleatorios entre 1 y 100
lista = []
for i in range(20):
    numRandom = random.randint(1, 100)
    lista.append(numRandom)

print("Lista de números:", lista)

# Calculamos la suma de todos los números
sumaTotal = sum(lista)

# Contamos cuántos números hay en la lista
cantidad = len(lista)

# Calculamos la media
media = sumaTotal / cantidad

# Mostramos el resultado
print(f"La media de los números es: {media:.2f}")
