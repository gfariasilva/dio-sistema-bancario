from datetime import datetime
import textwrap
from classes.cliente import Cliente
from classes.pessoa_fisica import PessoaFisica
from classes.conta_corrente import ContaCorrente
from classes.deposito import Deposito
from classes.saque import Saque
from classes.contas_iterador import ContasIterador

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Criar novo usuário
[nc] Criar nova conta
[lc] Listar contas
[q] Sair

=> """

clientes = []
contas = []

def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f'{datetime.now()}: {func.__name__.upper()}')
        return resultado
    
    return envelope

def filtrar_cliente(clientes, cpf):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente, numero_conta):
    if not cliente.contas:
        print('Cliente não tem nenhuma conta registrada.')
        return
    else:
        conta = [conta for conta in cliente.contas if conta.numero == numero_conta]
        if conta:
            return conta[0]
        else:
            print('Número de conta não identificada')
            return

@log_transacao
def depositar(clientes, cpf, valor, numero_conta):
    cliente =  filtrar_cliente(clientes, cpf)
    if not cliente:
        print('Cliente não encontrado.')
        return

    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente, numero_conta)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

@log_transacao
def sacar(clientes, cpf, valor, numero_conta):
    cliente =  filtrar_cliente(clientes, cpf)
    if not cliente:
        print('Cliente não encontrado.')
        return

    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente, numero_conta)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def print_extrato(clientes, cpf, numero_conta, tipo=None):
    cliente = filtrar_cliente(clientes, cpf)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente, numero_conta)
    if not conta:
        return

    print("\n================ EXTRATO ================")

    extrato = ""
    vazio = True
    
    for transacao in conta.historico.gerar_relatorio(tipo_transacao=tipo):
        vazio = False
        extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    if vazio:
        extrato = "Não foram realizadas movimentações."

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

@log_transacao
def criar_usuario(clientes, nome, data, cpf, endereco):
    cliente = filtrar_cliente(clientes, cpf)
    if cliente:
        print('Cliente já existente.')
        return
    
    cliente = PessoaFisica(endereco, cpf, nome, data)
    clientes.append(cliente)

    print('Cliente criado com sucesso!')

@log_transacao
def criar_conta_corrente(clientes, numero_conta, contas, cpf):
    cliente = filtrar_cliente(clientes, cpf)
    if not cliente:
        print('Cliente não encontrado.')

    conta = ContaCorrente.nova_conta(numero_conta, cliente)
    contas.append(conta)
    cliente.contas.append(conta)

    print('Conta corrente criada com sucesso!')

def listar_contas(contas):
    for conta in ContasIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

while True:
    opcao = input(menu)

    if opcao == 'd':
        depositar(clientes, input('Informe o CPF do usuário: '), float(input('Digite o valor a ser depositado: ')), int(input('Digite o número da conta ')))
    elif opcao == 's':
        sacar(clientes, input('Informe o CPF do usuário: '), float(input('Digite o valor a ser sacado: ')), int(input('Digite o número da conta ')))
    elif opcao == 'e':
        print_extrato(clientes, input('Informe o CPF do usuário: '), int(input('Digite o número da conta ')))
    elif opcao == 'nu':
        nome = input('Digite seu nome: ')
        cpf = input('Insira seu CPF (somente números): ')
        data = input('Informe a data de nascimento (dd-mm-aaaa): ')
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        criar_usuario(clientes, nome, data, cpf, endereco)
    elif opcao == 'nc':
        cpf = input('Informe o CPF do usuário: ')
        criar_conta_corrente(clientes, len(contas) + 1, contas, cpf)
    elif opcao == 'lc':
        listar_contas(contas)
    elif opcao == 'q':
        break
    else:
        print('Opção inválida!')