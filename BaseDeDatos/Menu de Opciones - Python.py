#MENU
import math
def mostrarMenu():
    print("\n--- MENU ---")
    print("1. Area de un rectangulo.")
    print("2. Volumen de un cilindro.")
    print("3. Volumen de un cubo.")
    print("4. Salir.")

def ingresarValor(mensaje):
    while True: 
        try: 
            numdecimal = float(input(mensaje))
            break
        except:
            print("Ingrese un valor correcto.")
    return numdecimal



while True:
    mostrarMenu()
    opcion = input("Elige una opción del 1 al 4: ")

    if opcion == "1":
        print("\n-- Cálculo del área de un rectángulo --")
        base = ingresarValor("ingrese el valor de un lado: ") #Base de Rectangulo
        altura = ingresarValor("ingrese el valor del otro lado: ")

        area = base * altura

        print(f"El area del rectangulo es {area} ")

    elif opcion == "2":
        print("\n-- Cálculo del volumen del cilindro --")
        radio = float(input("Ingrese el radio del circulo: "))
        altura = float(input("ingrese la altura del cilindro: "))

        volumen = math.pi * radio ** 2 * altura

        print(f"El volumen del cilindro es {volumen:.2f}")

    elif opcion == "3":
        print("\n-- Cálculo del volumen del cubo --")
        lado1 = float(input("Ingrese el valor del lado: "))

        volumen = lado1 ** 3


        print(f"el volumen del cubo es {volumen:.2f}")
    
    elif opcion == "4":
        print("Vuelva pronto.")
        break

    else:
        print("Opcion no valida")