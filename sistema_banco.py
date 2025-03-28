saldo = 0
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

deposito (90,0)

