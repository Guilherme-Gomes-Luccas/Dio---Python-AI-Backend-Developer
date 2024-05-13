def exibir_mensagem():
    print("Olá mundo")

def exibir_mensagem_2(nome):
    print(f"Olá {nome}")

def exibir_mensagem_3(nome = "User"):
    print(f"Olá {nome}")

exibir_mensagem()
exibir_mensagem_2("Guilherme")
exibir_mensagem_3()
exibir_mensagem_3("Gabriel")