# Sombrero Howars


casas = {
    "griffindor" : 0,
    "ravenclaw" : 0,
    "hufflepuff" : 0,
    "slytherin" : 0
}

# Pregunta numero 1.
print(                              )

print("  Que prefieres? ") 
print("  1-Amanecer ")
print("  2-Anochecer ")

print(                              )

answer = int(input('Elije la respuesta (1-2): '))
print(                              )


if answer == 1:

    casas["griffindor"] += 1
    casas["ravenclaw"] += 1
    
    Gryffindor += 1
    Ravenclaw += 1

elif answer == 2:

    casas["hufflepuff"] += 1
    casas["slytherin"] += 1

    Hufflepuff += 1
    Slytherin += 1

else:
    print("Entrada incorrecta." )
print(                              )



# Pregunta numero 2.

print("  Cuando ya no esté aqui, me recordaran como: ")
print("  1-El bueno ")
print("  2-El grande ")
print("  3-El sabio ")
print("  4-El valiente ")
print(                              )


answer = int(input('Elije la respuesta (1-4): '))
print(                              )
   
if answer == 1:
    casas["hufflepuff"] += 2
    Hufflepuff += 2 
elif answer == 2:
    Slytherin += 2
    casas["slytherin"] += 2
elif answer == 3:
    Ravenclaw += 2
    casas["ravenclaw"] += 2
elif answer == 4:
    casas["griffindor"] += 2
    Gryffindor += 2
else:
    print("Entrada incorrecta.")
print(                              )

# Pregunta numero 3.


print("  Qué instrumento te gusta más oir?")
print("  1-Violin ")
print("  2-Trompeta ")
print("  3-Piano ")
print("  4-Batería ")
print(                              )


answer = int(input("Elije una respuesta: (1-4)"))
print(                              )

if answer == 1:
    casas["slytherin"] += 4
    Slytherin +=  4
elif answer == 2:
    casas["hufflepuff"] += 4
    Hufflepuff += 4
elif answer == 3:
    casas["ravenclaw"] += 4
    Ravenclaw += 4
elif answer == 4:
    casas["griffindor"] += 4
    Gryffindor += 4
else:
    print("Entrada incorrecta.")

print(                          )
  
print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)

print(                        )

#if Gryffindor >= Ravenclaw and Gryffindor>= Hufflepuff and Gryffindor >= Slytherin:
#    print("Tu casa es Gryffindor!")
#elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
#    print("Tu casa es Ravenclaw!")
#elif Hufflepuff >= Slytherin:
#    print("Tu casa es Hufflepuff!")
#else:
#    print("Tu casa es Slytherin!")
print(casas)
print("Tu casa es : " + max(casas, key=casas.get))
print(                              )







