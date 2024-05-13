pessoa = {"nome": "Guilherme", "idade": 28, "endereco": {"numero": 24, "cidade": "Caraguatatuba"}}
pessoa.clear() # Limpa o dicionario
print(pessoa)

print("-----------------------------")

pessoa = {"nome": "Guilherme", "idade": 28, "endereco": {"numero": 24, "cidade": "Caraguatatuba"}}
pessoa_bk = pessoa.copy()
pessoa_bk["nome"] = "Lucas"
print(pessoa_bk)

print("-----------------------------")

dic1 = dict.fromkeys(["Nome", "Telefone"]) # {"nome": None, "Telefone": None}
# fromkeys cria um dicionario atraves dos atributos passados,
# nesse caso criando duas chaves vazias
print(dic1)

dic2 = dict.fromkeys(["Nome", "Telefone"], "vazio") # {"nome": vazio, "Telefone": vazio}
# Cria o dicionario e inseri o valor padrão vazio para todas as chaves
print(dic2)

print("-----------------------------")

print(pessoa.get("telefone"))
print(pessoa.get("telefone", {}))
print(pessoa.get("endereco", {}))
# Metoo get é um outro jeito e obter valores de um dicionarios
# Esse metodo evita exceções caso a chave não exista

print("-----------------------------")

print(pessoa.items()) # Retorna os items do dicionario

print("-----------------------------")

print(pessoa.keys()) # Retorna as chaves do dicionario

print("-----------------------------")

print(pessoa_bk.pop("endereco")) # remove os valores de acordo com a chave indicada
print(pessoa_bk.pop("endereco", {}))
# como ser indicado o retorno caso não seja encontrado a chave indicada

print("-----------------------------")

print(pessoa_bk.popitem()) # Remove os items em sequencia
# Caso não tenha mais items, será retornado um erro

print("-----------------------------")

print(pessoa.setdefault("nome", "Gabriel"))
# Setdefault tenta adicionar uma chave e um valor padrão para o dicionario
# caso a chave nome ja exista, será retornado o valor da chave
print(pessoa_bk.setdefault("cidade", "Caraguatatuba"))

print("-----------------------------")

pessoa_bk.update({"nome": "Gabriel"}) 
# O metodo update recebe um novo dicionario e atualiza os items do dicionario
# ou caso o dicionario informado contenha items novos, esses items serão inseridos no dicionario
print(pessoa_bk)
pessoa_bk.update({"idade": 42}) 
print(pessoa_bk)

print("-----------------------------")

print(pessoa.values()) # irá retorna todos os valores do dicionario

print("-----------------------------")

resultado = "idade" in pessoa
print(f"idade no dicionario pessoa é: {resultado}")
resultado = "altura" in pessoa
print(f"altura no dicionario pessoa é: {resultado}")
resultado = "numero" in pessoa["endereco"]
print(f"numero no dicionario pessoa é: {resultado}")
# Com o in, conseguimos verificar se uma chave existe um não

print("-----------------------------")

print(pessoa)
del pessoa["endereco"]["numero"] # remove chave de um dicionario
print(pessoa)
