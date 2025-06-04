def ingresarValor(mensaje):
    while True: 
        try: 
            x = float(input(mensaje))
            break
        except:
            print("ingrese un valor correcto")
    return x


#AREA DE RECTANGULO
base = ingresarValor("ingrese el valor de un lado: ")
altura = ingresarValor("ingrese el valor del otro lado: ")

area = base * altura

print(f"El area del rectangulo es {area} ")
