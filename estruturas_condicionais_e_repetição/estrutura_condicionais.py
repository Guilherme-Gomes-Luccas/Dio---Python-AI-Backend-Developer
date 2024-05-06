MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade")

if idade < MAIOR_IDADE:
    print("Menor de idade")

if idade >= MAIOR_IDADE:
    print("Maior de idade")
else:
    print("Menor de idade")


if idade >= MAIOR_IDADE:
    print("Maior de idade")
elif idade < IDADE_ESPECIAL:
    print("Menor de idade")
else:
    print("Adolescente")