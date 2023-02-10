class Carta:
    def __init__ (self, palo, valor): # constructor
        self.palo = palo
        self.valor = valor
    def __repr__ (self): # pinta info carta
        return f"{self.valor} de {self.palo}"

carta1 = Carta("Corazones", "Reina") 

print(carta1.palo)
print(carta1.valor)

print(carta1)

if carta1.valor == "Reina":
    puntos = 10

carta2 = Carta("Trebols", "As")

valores = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jota", "Reina", "Rey"]
baraja = []

for valor in valores:
    cartanueva = Carta("picas", valor)
    baraja.append(cartanueva)

print(baraja)