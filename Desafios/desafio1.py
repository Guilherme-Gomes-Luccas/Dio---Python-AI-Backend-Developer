# Primeiro desafio do bootcamp

# Sistema bancario composto pelas opções de depósitar, sacar e extrato
# Extrato - Permitir ver todos os depósitos e saques feitos utilizando o formato R$ xxx.xx
# Saques - 3 saques diários com limite de 500 reais
# Depósito - Apenas um úsuario

saques = ""
depositos = ""
extrato = ""

conta = 0
quantidade = 0
quantidade_saques = 3

options = "1"

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

    if options == "0":
        print("Obrigado por utilizar banco snake!!")
        break
    elif options == "1":
        quantidade = int(input("Digite a quantidade do deposito: "))
        while quantidade < 0:
            quantidade = int(input("Valor negativo, digite uma quantidade de deposito valida: ")) 
        depositos += str(quantidade) + ","
        conta += quantidade
    elif options == "2":
        if quantidade_saques < 1:
            print("Quantidade diaria de saques foi alcançada, tente novamente amanhã")
            continue

        quantidade = int(input("Digite a quantidade do saque: "))
        if quantidade > conta:
            print("Quantidade do saque informado é maior que o dinheiro atual na conta")
            continue
        else:
            if quantidade > 500:
                print("Não são aceitados valores acima de 500 reais para saque")
            else:
                saques += str(quantidade) + ","
                conta -= quantidade
                quantidade_saques -= 1
    elif options == "3":
        print(f"Total na conta: {conta:.2f}\n")

        print("Saques:")
        for number in saques:
            if "," in number:
                print(f"R${float(extrato):.2f}")
                extrato = ""
            else:
                extrato += number
        
        print("\n\n")

        print("Depositos:")
        for number in depositos:
            if "," in number:
                print(f"R${float(extrato):.2f}")
                extrato = ""
            else:
                extrato += number
    else:
        print("Opção não identificada, tente novamente")
