menu = '''
 ******* MENU *******
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
 *********************

'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
cont = 0

def deposito(valor):
     global saldo, extrato, cont
     if valor <= 0:
          print(' Digite um valor positivo!')
     else:
        saldo += valor
        extrato += f'\n Depósito: +R${valor:.2f}'
        cont += 1
        print(f'\n Depósito no valor de R${valor:.2f} realizado com sucesso!\n')

def saque(valor):
    global saldo, extrato, numero_saques, limite
    if numero_saques >= limite_saques:
        print('\n Você excedeu o limite de saques diários. Tente novamente amanhã!')
       
    elif valor > limite:
        print('\n ERRO! Valor máximo para saque é de R$500.00 reais')
    elif valor > saldo:
         print('\n Saldo insuficiente!')
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f'\n Saque: -R${valor:.2f}'
        print(f'\n Saque no valor de R${valor:.2f} realizaado com sucesso!\n')

def exibir_extrato():
    global saldo, extrato
    print('\n **************** EXTRATO ****************')
    print(extrato if extrato else 'Nenhuma movimentação realizada')
    print(f' Quantidade de depósitos realizados: {cont}')
    print(f' Quantidade de saques realizados: {numero_saques}')
    print(f' Saldo atual: R${saldo:.2f}\n')
    print(" ******************************************")

while True:
    opcao = input(menu)
    if opcao == '1':
        valor_deposito = float(input('\n Informe o valor que deseja depositar\n > R$'))
        deposito(valor_deposito)


    elif opcao == '2':
        valor_saque = float(input('\n Informe o valor que deseja sacar\n > R$'))
        saque(valor_saque)


    elif opcao == '3':    
        
       exibir_extrato()

    elif opcao == '0':
        print('Saindo do sistema...')
        break

    else:
        print(' Operação inválida, por favor selecione novamente a operação desejada.')
