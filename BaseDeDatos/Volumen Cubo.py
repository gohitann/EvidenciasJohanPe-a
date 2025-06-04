import math

def ingresarValor(mensaje):
    while True: 
        try: 
            x = float(input(mensaje))
            break
        except:
            print("ingrese un valor correcto")
    return x
    
#volumen del cubo    
    
lado1 = float(input("Ingrese el valor del lado"))

volumen = lado1 ** 3
print(f"el volumen del cubo es {volumen:.2f}")
