#Operadores lógicos

height = int(input('What is your height (cm)? '))
credits = int(input('How many credits do you have? '))


if credits >= 10:
    if height >= 137:
        print("Disfruta del viaje")
    else:
        print("No tienes suficiente altura")
else:
    if height >= 137:
        print("No tienes suficientes créditos")
    else:
        print("No cumple ninguno de los requisitos")







