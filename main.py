import string
import random

def GeradorDeSenha(qt_letras, qt_numeros, qt_caracteres_especiais):
    lista_senha = []
    for i in range(1, qt_letras + 1):
        lista_senha.append(random.choice(letras))
    for i in range(1, qt_numeros + 1):
        lista_senha += random.choice(numeros)
    for i in range(1, qt_caracteres + 1):
        lista_senha += random.choice(caracteres_especiais)
    random.shuffle(lista_senha)
    return ''.join(str(char) for char in lista_senha)

letras = list(string.ascii_letters)
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
caracteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', ';', ':', "'", '"', '.', '<', '>', '?', '/']

qt_letras = int(input("Quantas letras você quer na sua senha?\n"))
qt_numeros = int(input("Quantos números?\n"))
qt_caracteres = int(input("Quantos caracteres especiais?\n"))

print(f"sua senha é: {GeradorDeSenha(qt_letras, qt_numeros, qt_caracteres)}")