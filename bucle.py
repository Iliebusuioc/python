# while

import random

numero1 = random.randint (1, 10)

numero2 = int(input("Dime un numero "))

while numero1 != numero2:
    if numero1 < numero2:
        print("Tu numero es mayor")
    if numero1 > numero2:
        print("Tu numero es menor")
    numero2 = int(input("Dime un numero "))

print ("Congratulations")

