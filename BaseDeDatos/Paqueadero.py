#programa parqueadero 
def ingresarHora (tipo):
    hora = int(input(f"ingrese la hora de {tipo} (hhmm):  "))
    hh = hora // 100
    mm = hora % 100
    mm += hh * 60
    return mm
    
##############   PROGRAMA PRINCIPAL ##################
he = ingresarHora("entrada")
hs = ingresarHora("salida")

#CALCULAR TIEMPO EN MINUTOS
if hs < he:
    tm = 1440 -  he + hs     # salio al otro dia 
    
else: 
    tm = hs - he             # salio el mismo dia 
    tm = 360 - 1080
#CALCULAR TIEMPO
tm = hs - he 
th = tm // 60 
resto = tm % 60
if resto > 0:
    th += 1

#CALCULAR COSTO 
th += 1
valor = 2000 - th * 800

#mostrar calculo
print(f"El valor a pagar es ${valor}")
