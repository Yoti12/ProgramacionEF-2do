##Escribir un programa que pida al usuario dos números
# enteros y muestre por pantalla la <n> entre <m> da un cociente <c>
# y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.
numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))
cosciente = numero1/numero2
residuo = numero1%numero2
print(numero1,"entre", numero2, "da un cosciente de", cosciente,"y un residuo de ",residuo)