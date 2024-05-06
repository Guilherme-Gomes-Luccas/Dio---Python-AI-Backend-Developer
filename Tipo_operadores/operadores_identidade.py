saldo = 1000
limite = 500

print(saldo is limite) #se saldo ocupa a mesma região de memoria que o limite
print(saldo is not limite)

limite = 1000

print(saldo is limite)
print(saldo is not limite)