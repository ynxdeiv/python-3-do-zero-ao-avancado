"""
criar uma lista de compras com enumerate, inserir, listar e apagar.
"""
import os
import time
lista = []
while True:
        print('Selecione uma opção:')
        opcao_cliente=input('\t[i]nserir [a]pagar [l]istar: ')
   
        opcao_cliente = opcao_cliente.lower()
        if opcao_cliente == 'i':
              os.system('cls')
              valor = input('Digite o item: ')
              lista.append(valor)
        
            
        elif opcao_cliente == 'a':
            os.system('cls')
            valor = input('Digite o índice que deseja apagar: ')
            lista.pop(valor)

        elif opcao_cliente == 'l':
                os.system('cls')
                print(lista,'\n')
        

        if opcao_cliente.isdigit():
            print('Dígitos não são aceitos, tente novamente!')
            time.sleep(3)
            continue
            ...
                
        ...