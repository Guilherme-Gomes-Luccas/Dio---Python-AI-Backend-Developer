def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#Função por posição

def criar_carro2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro2(modelo="palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#Função por palavra chave

def criar_carro3(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro3("palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#Função por palavra chave e posição