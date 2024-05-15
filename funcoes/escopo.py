salario = 2000

def salario_bonus(bonus):
    global salario 
    # Atributo global indica que queremos usar uma varaivel fora do escopo da função
    salario+=500
    return salario

print(salario_bonus(500))