from .historico import Historico


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    @property
    def saldo(self) -> int:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self) -> Historico:
        return self._historico

    def sacar(self, valor) -> bool:
        excedeu_saldo = valor > self._saldo

        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Valor inválido.")

        return False

    def depositar(self, valor) -> bool:
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        else:
            print("Valor inválido.")
            return False
