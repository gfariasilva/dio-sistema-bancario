menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[nu] Criar novo usuário
[nc] Criar nova conta

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = {}
contas = {}
AGENCIA = '0001'
n_conta = 1

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R${valor}\n'
        print('Depósito realizado com sucesso!')
    else:
        print('Valor inválido!')
    return saldo, extrato

def sacar(*, valor, saldo, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print('Saldo insuficiente!')
    elif valor > limite:
        print('Valor excedeu o limite!')
    elif numero_saques > limite_saques:
        print('Número limite de saques excedido!')
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f'Saque: R${valor}\n'
        print('Saque realizado com sucesso!')
    else:
        print('Valor inválido!')
    return saldo, extrato

def print_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(nome:str, data:str, cpf:str, endereco:dict, usuarios:dict):
    cpf_formatado = int(''.join(c for c in cpf if c.isdigit()))
    if cpf_formatado not in usuarios.keys():
        usuarios[cpf_formatado] = {
            'nome': nome,
            'data': data,
            'cpf': cpf_formatado,
            'endereco': f'{endereco['logradouro']}, {endereco['n']} - {endereco['bairro']} - {endereco['cidade']}/{endereco['estado']}'
        }
        print('Usuário adicionado com sucesso!')
        return True
    else:
        print('Usuário já registrado!')
        return False

def criar_conta_corrente(agencia:str, numero:int, usuario:int, usuarios:dict, contas:dict):
    if usuario in usuarios.keys():
        contas[numero] = [
            agencia,
            numero,
            usuario
        ]

while True:
    opcao = input(menu)

    if opcao == 'd':
        saldo, extrato = depositar(saldo, float(input('Digite o valor a ser depositado: ')), extrato)
    elif opcao == 's':
        saldo, extrato = sacar(valor=float(input('Digite o valor a ser sacado: ')), saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
    elif opcao == 'e':
        print_extrato(saldo, extrato=extrato)
    elif opcao == 'nu':
        nome = input('Digite seu nome: ')
        cpf = input('Insira seu CPF (somente números): ')
        data = input('Informe a data de nascimento (dd-mm-aaaa): ')
        print('-- Endereço --')
        endereco = {
            'logradouro': input('Digite o logradouro: '),
            'n': input('Digite o número (caso houver): '),
            'bairro': input('Insira o bairro: '),
            'cidade': input('Insira a cidade: '),
            'estado': input('Insira o estado / sigla: ')
        }
        criar_usuario(nome, data, cpf, endereco, usuarios)
    elif opcao == 'nc':
        cpf = int(''.join(c for c in input('Informe o CPF do usuário: ') if c.isdigit()))
        if(criar_conta_corrente(AGENCIA, n_conta, cpf, usuarios, contas)):
            n_conta += 1
    elif opcao == 'q':
        break
    else:
        print('Opção inválida!')