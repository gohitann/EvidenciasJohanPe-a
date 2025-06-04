import math

def ingresarValor(mensaje):
    while True: 
        try: 
            x = float(input(mensaje))
            break
        except:
            print("ingrese un valor correcto")
    return x
    
#Volumen cilindro

radio = float(input("Ingrese el radio del circulo"))
altura = float(input("ingrese la altura del cilindro"))

volumen = math.pi * radio ** 2 * altura

print(f"El volumen del cilindro es {volumen:.2f}")
