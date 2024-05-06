nome = "guilhERme"

print(nome.upper()) # Todas as letras maiusculas
print(nome.lower()) # Todas as letras minusculas
print(nome.title()) # Primeira letra maiuscula

texto = "  Ola mundo  "

print(texto)
print(texto.strip()) # Tira todos os espaços
print(texto.lstrip()) # Tira os espaços a esquerda
print(texto.rstrip()) # Tiras os espaços a direita

menu = "Python"

print(menu.center(14, "#"))
print("-".join(menu))