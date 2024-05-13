def calcular_total(numero):
    return sum(numero)

def retornar_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10,25]))
print(retornar_antecessor_sucessor(2))