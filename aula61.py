'''
Cálculo Primeiro Dígito CPF

Verificar se é válido.

'''
while True:
    novo_cpf = ''
    cpf_inserido = input('Digite seu CPF: ')
    
    for digito in cpf_inserido:
        if digito.isdigit():
            novo_cpf += digito
    if len(cpf_inserido) < 11:
        continue

    try:
        i=0
        calculo_soma_digitos = 0 

        nove_digitos = int(novo_cpf[:9])
        
        nove_digitos_str = str(nove_digitos)



        for contador in range (10, 1, -1):
            
            digito_convertido = int(nove_digitos_str[i])

            calculo_soma_digitos += digito_convertido*contador

            i+=1

        calculo_resultado = (calculo_soma_digitos*10)%11

        calculo_resultado = 0 if calculo_resultado >= 10 else calculo_resultado

        print(f'O valor do primeiro dígito é {calculo_resultado}')

        
        
    except ValueError:
        print('NÃO PODE SER UM CPF')
        continue


    ...