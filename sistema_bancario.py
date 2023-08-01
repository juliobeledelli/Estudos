#SISTEMA BANCARIO

#FUNÇÕES:
    # SACAR:
    #     Permitir 3 saques diarios
    #     Ate $500 por saque
    #     validar se existe saldo, informar msg por falta de saldo
    #     ser visualizado no extrato
    # DEPOSITAR:
    #     Depositar valores positivos
    #     apenas um usuario
    #     ser visualizado no extrato
    # VISUALIZAR EXTRATO
    #     Listar todos as movimentações da conta
    #     no final, mostar o valor total da conta

import datetime

def extrato(valor,operacao):
    data = {
        'Operação': operacao,
        'Valor': valor,
        'Data': datetime.date.today()
    }

    historico_extrato.append(data)

def sacar(saldo, limite_diario, ultimo_saque):
    print('Saque')

    if not ultimo_saque == datetime.date.today():
        limite_diario = 3

    valor = float(input('Digite o valor a ser sacado: '))
    if valor > 500:
        print('Valor máximo por saque é de R$500\n')
        sacar(saldo, limite_diario, ultimo_saque)
    elif valor > saldo:
        print('Saldo insuficiente')
        sacar(saldo, limite_diario, ultimo_saque)
    else:
        if limite_diario > 0:
            ultimo_saque = datetime.date.today()
            limite_diario -= 1
            saldo -= valor
            print('Saque realizado com sucesso\n')
            print('Seu saldo atual é de R${}\n'.format(saldo))
            extrato(valor, operacao='Saque')
            print('Deseja realizar outra operação?\n')
            menu(saldo, limite_diario, ultimo_saque)
        else:
            print('Limite de saques diários atingido\n')
            menu()

def depositar(saldo):
    print('Deposito')
    valor = float(input('Digite o valor a ser depositado: '))
    if valor > 0:
        saldo += valor
        print('Deposito realizado com sucesso\n')
        print('Seu saldo atual é de R${}\n'.format(saldo))
        extrato(valor, operacao='Deposito')
        print('Deseja realizar outra operação?\n')
        menu(saldo, limite_diario, ultimo_saque)
    else:
        print('Valor inválido\n')
        depositar()

def menu(saldo, limite_diario, ultimo_saque):

    print('Bem vindo ao Banco DIO')
    print('Escolha uma das opções abaixo:')
    print('''
    1 - Sacar
    2 - Depositar
    3 - Extrato
    4 - Sair''')

    opcao = int(input('Escolha uma das opções acima: '))
    if opcao == 1:
        sacar(saldo, limite_diario, ultimo_saque)
    elif opcao == 2:
        depositar(saldo)
    elif opcao == 3:
        print(historico_extrato)
    elif opcao == 4:
        print('Obrigado por utilizar o Banco DIO')
        exit()
    else:
        print('Opção inválida')
        menu()

historico_extrato = []
saldo = 1000.00
limite_diario = 3
ultimo_saque = datetime.date.today()
menu = menu(saldo,limite_diario,ultimo_saque)
