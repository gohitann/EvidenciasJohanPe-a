# ejercicio16.py
valores = [1000, 500, 200, 100, 50]
cobro = int(input("Ingrese el valor a cobrar: "))
entregado = int(input("Ingrese el valor entregado: "))
if entregado < cobro:
    print("Monto insuficiente.")
else:
    cambio = entregado - cobro
    print(f"Cambio a devolver: {cambio}")
    for v in valores:
        cantidad = cambio // v
        if cantidad > 0:
            print(f"{cantidad} moneda(s) de {v}")
            cambio %= v
