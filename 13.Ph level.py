#condiciones

int(input('Enter a pH value (0-14): '))
ph = 7
if ph > 7:
    print("Basico")
elif ph < 7:
    print("Acido")
else: 
    print("neutral")