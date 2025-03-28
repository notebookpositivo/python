saldo = 0
limite_saldo = 500
numero_saques = 0 
limites_saques = 3
usuarios=[] #lista vazia para adicionar valores futuramente
contas = []
agencia='0001'


def menu():
    print('''
        *******Menu*******
        (1) Criar Usuário
        (2) Criar Conta
        (3) Listar contas
        (d) Depositar
        (s) Sacar
        (e) Extrato
        (q) Sair
    ''')
    return input('Qual opção deseja?')


def deposito(valor,saldo):
    # vou receber o valor do deposito e somar o valor ao saldo
    if valor > 0 :
        saldo +=valor
        #print mostrando o valor depositado
        print(f'Você depositou R${valor}')
    
    else:
        print('Valor do deposito inválido. Verifique a quantia digitada.')


    return (saldo)


def saque (saque,saldo):
    if numero_saques >= limites_saques:
        print('Você atingiu o limite de saques da sua conta, tente novamente em outro dia útil')
    else:
        if saque <= 0 :
            print('Saque invalido. Verifique o valor e tente novamente.')
        elif saque > limite :
            print('Valor limite excedido. Verifique o valor e tente novamente.')
        elif saque > saldo :
            print('Saldo insuficiente. Verifique o valor e tente novamente.')
        else:
            saldo -= saque
            numero_saques +=1
    return (saldo)            


