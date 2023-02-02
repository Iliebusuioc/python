
import random

casilla = [" "," "," ", " ", " ", " ", " ", " ", " "]

'''
| X | O |  | Casillas 0,1,2
| O |   |  | Casillas 3,4,5
|   | X |  | Casillas 6,7,8
'''

casilla[0] = "_"
casilla[1] = "_"
casilla[2] = "_"
casilla[3] = "_"
casilla[4] = "_"
casilla[5] = "_"
casilla[6] = "_"
casilla[7] = "_"
casilla[8] = "_"

print(casilla [0], casilla [1], casilla [2])
print(casilla [3], casilla [4], casilla [5])
print(casilla [6], casilla [7], casilla [8])

posicion = int(input("Elige casilla "))
