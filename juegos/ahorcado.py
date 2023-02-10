palabra_secreta = "patata"

letras_correctas = []
letras_incorrectas = []

seguir_jugando = True



while seguir_jugando:
    letra_pedida = input (" Dime una letra: ")

   

    if letra_pedida not in palabra_secreta:
        letras_incorrectas.append(letra_pedida)
    else:
        for letra in palabra_secreta:
         if letra == letra_pedida:
              letras_correctas.append(letra_pedida)

    for letra in palabra_secreta:
        if letra in letras_correctas:
            print (letra, end="")
        else:
         print ("_ ", end="")

    
    if letra_pedida in palabra_secreta:
        letras_correctas.append(letra_pedida)
    else:
        letras_incorrectas.append(letra_pedida)
    print(" correctas" ,letras_correctas)
    print(" incorrectas " ,letras_incorrectas)

    if set(letras_correctas) == set(palabra_secreta):
        seguir_jugando = False
        print("Ganas!")


    


