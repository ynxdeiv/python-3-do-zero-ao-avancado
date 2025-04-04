# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multilpicar(*args):
    total = 1
    for numero in args:
        total*=numero
    print(total)
    return total
