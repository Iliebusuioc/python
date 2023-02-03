
palabra_secreta = "patata"
letras_correctas = []

print("Juego del ahorcado")

letra_pedida = input("Pide una letra ")

longitud_palabra = (len(palabra_secreta))

while longitud_palabra > 0:
    print("_ ", end="")
    longitud_palabra = longitud_palabra -1

for letra in palabra_secreta:
    if letra == letra_pedida:
        letras_correctas.append(letra)
        print(letras_correctas)
        else:
            print("_", end="")