# ejercicio21.py
import random
digitos = random.sample(range(10), 3)
intentos = 0
ganado = False
print("Adivina los 3 dígitos (entre 0 y 9).")
while not ganado:
    intento = [int(input(f"Ingrese dígito para posición {i+1}: ")) for i in range(3)]
    pista = []
    for i in range(3):
        if intento[i] == digitos[i]:
            pista.append("verde")
        elif intento[i] in digitos:
            pista.append("amarillo")
        else:
            pista.append("rojo")
    intentos += 1
    print("Pista:", pista)
    if pista == ["verde", "verde", "verde"]:
        ganado = True
print(f"¡Ganaste en {intentos} intento(s)!")
