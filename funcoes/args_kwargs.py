def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Quarta-feira, 15 de maio de 2024",
    "zen of Python",
    "Beautiful is better than ugly.",
    autor="Tim Peters",
    ano=1999)

# Kwargs --> atributos chaves: valores
# args --> valores