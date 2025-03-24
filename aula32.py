"""
 Faça um programa que peça ao usuário para digitar um número inteiro,
 informe se este número é par ou ímpar. Caso o usuário não digite um número
 inteiro, informe que não é um número inteiro.
 """
# try:
#    numero_inteiro = input('Digite um número: ')
#    if numero_inteiro % 2 == 0:
#      print(f'O número que você escolheu: {numero_inteiro} é par')
#    else:
#         print(f'O número que você escolheu: {numero_inteiro} é impar')
     
# except:
#    print(f'O número que você escolheu: {numero_inteiro} não é válido')
    
"""
 Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
 descrito, exiba a saudação apropriada. Ex. 
 Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
 """
# try:
#    hora_usuario = int(input('Digite a hora: '))

#    manha = hora_usuario >=0 and hora_usuario <= 11
#    tarde = hora_usuario >=12 and hora_usuario <= 17
#    noite = hora_usuario >=18 and hora_usuario <= 23

#    if manha:
#       print(f'Olá, bom dia! São {hora_usuario} horas!')

#    elif tarde:
#       print(f'Olá, boa tarde! São {hora_usuario} horas!')

#    elif noite:
#       print(f'Olá, boa noite! São {hora_usuario} horas!')     

#    else:
#         print('Hora inválida! Digite um valor entre 0 e 23.')

# except:
#     print('O valor digitado não corresponde a uma hora')
    
 
"""
 Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
 menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
 "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
 """

try:
    nome_usuario = input('Digite seu nome: ')
    converter_inteiro = int(nome_usuario)
    
    print('Isso não é um nome, você digitou um número!')
    ...
except ValueError:
    tamanho_nome = len(nome_usuario)
 
    curto = tamanho_nome > 0 and tamanho_nome <= 4
 
    normal = tamanho_nome >= 5 and tamanho_nome <= 6
 
    longo = tamanho_nome >6 

    if curto:
        print(f'Seu nome: {nome_usuario}, é considerado curto')
    if normal:
        print(f'Seu nome: {nome_usuario}, é considerado normal')
    if longo:
        print(f'Seu nome: {nome_usuario}, é considerado longo')


    ... 