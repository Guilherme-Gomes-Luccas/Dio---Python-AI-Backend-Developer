def sacar(valor):

    saldo = 500

    if saldo >= valor:
        print("Valor sacado")

    print("Obrigado por sacar")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(100)
depositar(100)