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

    


    ...