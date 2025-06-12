menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R${valor}\n'

def sacar(valor):
    if valor > saldo:
        print('Saldo insuficiente!')
    elif valor > limite:
        print('Valor excedeu o limite!')
    elif numero_saques > LIMITE_SAQUES:
        print('Número limite de saques excedido!')
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f'Saque: R${valor}\n'
    else:
        print('Valor inválido!')

def print_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input()

    if opcao == 'd':
        depositar(float(input('Digite o valor a ser depositado: ')))
    elif opcao == 's':
        sacar(float(input('Digite o valor a ser sacado: ')))
    elif opcao == 'e':
        print_extrato()
    elif opcao == 'q':
        break
    else:
        print('Opção inválida!')