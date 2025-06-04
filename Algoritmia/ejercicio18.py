# ejercicio18.py
tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
nit = int(input("Ingrese el NIT: "))
resto = nit % 23
letra = tabla[resto]
print(f"La letra de control del NIT es: {letra}")
