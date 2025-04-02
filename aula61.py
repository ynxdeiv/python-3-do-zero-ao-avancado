'''
Cálculo Primeiro Dígito CPF

Verificar se é válido.

'''

novo_cpf = ''

while True:

    cpf_inserido = input('Digite seu CPF: ')
    
    for digito in cpf_inserido:
        if digito.isdigit():
            novo_cpf += digito
    try:
        nove_digitos = int(novo_cpf[:9])
        print(nove_digitos)
    except ValueError:
        print('NÃO PODE SER UM CPF')
        continue


    ...