##Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
nombre=input("Ingrese su nombre: ")

horasTrabajadas=float(input("Ingrese el número de horas que trabajó: "))
costoDeHora=float(input("Ingrese el costo de la hora: "))

pago=horasTrabajadas*costoDeHora

print("Estimad@",nombre,"usted recibirá","$", pago)