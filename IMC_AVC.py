# Calculadora IMC by Abraham Valle

valida = False
nombre = ""
edad = ""
peso = ""
estatura = ""

while valida is False:
    nombre = input("Escribe tu nombre: ")
    if nombre != "":
        valida = True
        # print(nombre)
valida = False
while valida is False:
    edad = int(input("Escribe tu edad: "))
    if edad != "":
        valida = True
        #print(edad)
valida = False
while valida is False:
    peso = float(input("Escribe tu peso en kilogramos: "))
    if peso != "":
        valida = True
        #print(peso)
valida = False
while valida is False:
    estatura = float(input("Escribe tu estatura en metros: "))
    if estatura != "":
        valida = True
        #print(estatura)
    IMC = peso / estatura ** 2
    if IMC >= 0 and IMC <= 15.99 :
        IMC2 = "Delgadez severa"
    elif IMC >= 16.00 and IMC <= 16.99 :
         IMC2 = "Delgadez moderada"
    elif IMC >= 17.00 and IMC <= 18.49:
         IMC2 = "Delgadez leve"
    elif IMC >= 18.50 and IMC <= 24.99 :
         IMC2 = "Normal"
    elif IMC >= 25.00 and IMC <= 29.99:
       IMC2 = "Sobrepeso"
    elif IMC >= 30.00 and IMC <= 34.99:
         IMC2 = "obesidad leve"
    elif IMC >= 35.00 and IMC <= 39.00:
         IMC2 = "obesidad media"
    elif IMC >= 40.00:
        IMC2 = "obesidad morbida"
    print(f"Hola {nombre}, tus datos son los siguientes: \n Nombre: {nombre}\n Edad: {edad}\n Peso: {peso}\n Indice de masa corporal (IMC): {IMC}\n Condición de masa corporal: {IMC2}")
    break
