while True:

    def linha():
        print('-'*40)
        return
    
    numero_1 = input('Digite o primeiro número: ')
    linha()
    numero_2 = input('Digite o segundo número: ')
    linha()
    operador = input('Digite o operador (+-/*): ')
    linha()

    numero_valido = None
    try:
        numero_1_float= float(numero_1)
        numero_2_float= float(numero_2)
        numero_valido = True

    except:
        numero_valido = None
    
    if numero_valido is None:
        print('Um ou ambos números digitados não é válido :( ')
        linha()
        continue
    
    operadores_validos='+-/*'

    if operador not in operadores_validos:
        print('Operador não listado, por favor digite novamente. ')
        linha()
        continue
    
    if len(operador)>1:
        print('Digite apenas um operador, por favor tente novamente. ')
        linha()
        continue
        
    print('Vamos as contas!')
    if operador =='+':
        print(numero_1_float+numero_2_float)
        linha()

    elif operador =='-':
        print(numero_1_float-numero_2_float)
        linha()
    elif operador =='*':
        print(numero_1_float*numero_2_float)
        linha()
    elif operador =='/':
        print(numero_1_float/numero_2_float)
        linha()

    sair = input('Deseja sair? [S]im: ').lower().startswith('s')


    if sair:
        break
    else:
        continue
