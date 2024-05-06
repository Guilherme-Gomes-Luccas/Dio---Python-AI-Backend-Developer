nome = "Guilherme"
idade = 20
profissao = "programador"
linguagem = "Python"
saldo = 45.425

dados = {"nome": "Guilherme", "idade": 20}

print("Nome: %s \nIdade: %d" % (nome, idade))
print("Nome: {} \nIdade: {}".format(nome, idade))
print("Nome: {1} \nIdade: {0}".format(idade, nome))
print("Nome: {nome} \nIdade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} \nIdade: {idade}".format(**dados))

print(f"Saldo: {saldo:.0f}")
print(f"Saldo: {saldo:.2f}")
print(f"Saldo: {saldo:10.2f}")