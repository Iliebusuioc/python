palabra_secreta = "gato"

letras_correctas = []
letras_incorrectas = []

while True:
    for letra in palabra_secreta:
        if letra in letras_correctas:
            print (letra, end="")
        else:
         print ("_ ", end="")

    letra_pedida = input ("Dime una letra: ")

    if letra_pedida in palabra_secreta:
        letras_correctas.append(letra_pedida)
    else:
        letras_incorrectas.append(letra_pedida)
    print("correctas" ,letras_correctas)
    print("incorrectas " ,letras_incorrectas)