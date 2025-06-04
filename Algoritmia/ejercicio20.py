# ejercicio20.py
capital = float(input("Ingrese el capital: "))
interes_anual = float(input("Ingrese el interés anual (%): "))
años = int(input("Ingrese el número de años: "))
interes_mensual = interes_anual / 100 / 12
pagos = años * 12
cuota = capital * interes_mensual / (1 - (1 + interes_mensual) ** -pagos)
print(f"Cuota mensual: {cuota:.2f}")
print(f"Total a pagar: {cuota * pagos:.2f}")
