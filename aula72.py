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

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    try:
        if numero%2 ==0:
            return 'Par'
        else:
            return 'Ímpar'
    except TypeError:
        print('O valor digitado não é um número')


resultado = par_impar(1)
print(resultado)