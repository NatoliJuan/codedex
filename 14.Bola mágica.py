
import random

question = input("Hazme una pregunta: ")

random_number = random.randint(1, 4)

if random_number == 1:
    answer = "Claro que si"
elif random_number == 2:
    answer = "Seguramente no."
elif random_number == 3:
    answer = "Ni de coña"
elif random_number == 4:
    answer = "Por supuesto"
else:
    answer = "error"
    
print("Pregunta: " + question)
print("Bola Mágica: " + answer)

