# ejercicio17.py
aprendices = [
    "Álvarez", "Bermúdez", "Cardona", "Díaz", "Espitia",
    "García", "López", "Martínez", "Ramírez", "Zamora"
]
print("Lista actual:")
print(aprendices)
nuevo = input("Ingrese el apellido del nuevo aprendiz: ")
aprendices.append(nuevo)
aprendices.sort()
print("Lista actualizada:")
print(aprendices)
