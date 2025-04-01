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
            valor = int(input('Digite o índice que deseja apagar: '))
            try:
                  del lista[valor]
            except:
                  print('Indice inexistente')

        elif opcao_cliente == 'l':
                os.system('cls')
                for indice, item in enumerate(lista, start = 1):
                      print(indice, item)
        
        else: 
              os.system('cls')
              print('Está opção não existe, tente novamente ')
              continue
        ...
                
        ...