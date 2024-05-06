# texto = input("Informe um texto: ")
texto = ""
VOGAIS = "AEIOU"

# Exemplo utilizando iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
    else:
        print()
        print("Termino do for", end="")

# Exemplo com range
for numero in range(0, 51, 5):
    print(numero, end=" ")