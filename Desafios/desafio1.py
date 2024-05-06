# Primeiro desafio do bootcamp

# Sistema bancario composto pelas opções de depósitar, sacar e extrato
# Extrato - Permitir ver todos os depósitos e saques feitos utilizando o formato R$ xxx.xx
# Saques - 3 saques diários com limite de 500 reais
# Depósito - Apenas um úsuario

# Extrato - Utilizar append para fazer uma lista que recebe tanto os depósitos quanto os saques

saques = ""
depositos = ""
extrato = ""

conta = 0
deposito = 0

options = "1"

#for number in saque:
#    if "," in number:
#        print(f"extrato: {float(extrato):.2f}\n")
#        extrato = ""
#    else:
#        extrato += number

while options != "0":
    options = input("""
    ########## BANCO SNAKE ##########
    #                               #
    #    O que deseja fazer?        #
    #                               #
    #    [1] - Depositar            #
    #    [2] - Sacar                #
    #    [3] - Extrato              #
    #    [0] - Sair                 #
    #################################
    O que deseja fazer: """)

    if options == "1":
        deposito = int(input("Digite a quantidade do deposito: "))
        depositos += deposito + ","
    