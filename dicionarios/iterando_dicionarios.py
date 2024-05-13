contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "Telefone": "3333-221"},
    "gabriel@gmail.com": {"nome": "Gabriel", "Telefone": "2234-351"}
}

for chave in contatos:
    print(chave, contatos[chave])

# Melhor forma para percorrer dicionarios
for chave, valor in contatos.items(): # Metodo items retorna uma tupla de items
    print(chave, valor)