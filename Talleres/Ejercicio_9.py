##Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
montoInicial=int(input("Ingrese el monto inicial: "))
interesAnual=float(input("Ingrese el interes anual: "))/100
años=int(input("Ingrese el número de años: "))
capital=montoInicial*(1+interesAnual)**años
print("El capital obtenido es de",capital)
# 4, 6, 8, 11