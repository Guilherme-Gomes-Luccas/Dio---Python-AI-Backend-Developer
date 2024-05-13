def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
# Desse jeito será necessario seguir a ordem dos atributos

#salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
# Desse jeito não será necessario seguir a ordem de argumento da função
# Mas caso seja mudando o nome de um dos argumentos, será retornado um erro
# Exemplo: o atributo modelo ir para model

#salvar_carro(**{"marca":"Fiat", "modelo":"Palio", "ano":1999, "placa":"ABC-1234"})
# Séra passado um dicionario e o ** indica que os valores do dicionario serão adquiridos