from .conta import Conta
from .saque import Saque

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
        )

        excedeu_numero_saques = numero_saques >= self._limite_saques
        excedeu_limite = valor >= self._limite

        if excedeu_numero_saques:
            print('Número limite de saques excedido.')
        elif excedeu_limite:
            print('Valor limite excedido.')
        else:
            return super().sacar(valor)
    
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
    
    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self._agencia}', '{self._numero}', '{self.cliente._nome}')>"