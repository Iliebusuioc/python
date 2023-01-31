
casillas = [" "," "," ", " ", " ", " ", " ", " ", " ", " "]

'''
| X | O |  | Casillas 0,1,2
| O |   |  | Casillas 3,4,5
|   | X |  | Casillas 6,7,8
'''
while :
    posicion = int(input ("Elige una casilla [0 a 8]"))
    casillas[posicion] = "X"

    if (casillas [0] == casillas [1] == casillas [2]):
        print("ganador")

    if (casillas [3] == casillas [4] == casillas [5]):
        print("ganador")

    if (casillas [6] == casillas [7] == casillas [8]):
        print("ganador")

    if (casillas [0] == casillas [3] == casillas [6]):
        print("ganador")

    if (casillas [2] == casillas [5] == casillas [8]):
        print("ganador")

    if (casillas [0] == casillas [4] == casillas [8]):
        print("ganador")

    if (casillas [2] == casillas [4] == casillas [6]):
        print("ganador")

    if (casillas [1] == casillas [4] == casillas [7 ]):
        print("ganador")

