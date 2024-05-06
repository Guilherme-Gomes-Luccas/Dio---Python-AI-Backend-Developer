while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

print(" ")

for numero in range(100):
    if numero % 2 == 0:
        continue # Similar ao break, mas em vez de parar a operação inteira ele pula somente essa etapa
    
    print(numero, end=" ")