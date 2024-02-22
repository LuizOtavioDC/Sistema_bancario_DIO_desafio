from abc import ABC, abstractproperty, abstractclassmethod

class transacao (ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, conta):
        pass

class cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.conta = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar

    def adicionar_conta(self, conta):
        self.conta.append(conta)

class conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = historico()
    
    @property
    def saldo(self):
        return self._saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls (numero, cliente)

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        
        if saldo == 0:
            print("Você não possui saldo suficiente na conta para realizar esta operação")
        else:
            if valor>500:
                print("Valor de saque desejado é maior do que o limite maximo de saque que é de R$500.00")
            elif valor>saldo:
                print("Valor de saque desejado é maior do que o valor disponivel na conta")
            else:
                self._saldo -= valor
                print("Saque feito com sucesso")
                return True
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Valor depositado com sucesso")
        else:
            print("Erro ao depositar o valor")
            return False

        return True

class PessoaFisica(cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco): 
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        super().__init__(endereco)

class ContaCorrente(conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == saque.__name__]
        )

        if valor > self.limite:
            print("Seu limite de saque diario foi excedido")

        elif saques >= self.limite_saques:
            print("O seu limite de saque diarios foi atingido")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Sua Agencia é:{self.agencia}
            Sua conta é:{self.numero}
            Cliente:{self.cliente.nome}
        """
    
class saque(transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)

class deposito(transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)

class historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": transacao.data
            }
        )


def depositar(usuarios):
    cpf = input("Qual o seu CPF?: ")
    cliente = [cliente for cliente in usuarios if cliente.cpf == cpf]

    if not cliente:
        print("Nenhum cliente com este CPF")
        return

    valor = float(input("Qual o valor que sera depositado?: "))
    transacao = deposito(valor)

    if not cliente.contas:
        print("Cliente não possui conta")
        return

    cliente.realizar_transacao(conta, transacao)

def sacar(usuarios):
    cpf = input("Qual o seu CPF?: ")
    cliente = [cliente for cliente in usuarios if cliente.cpf == cpf]

    if not cliente:
        print("Nenhum cliente com este CPF")
        return

    valor = float(input("Qual o valor que sera depositado?: "))
    transacao = saque(valor)

    if not cliente.contas:
        print("Cliente não possui conta")
        return

    cliente.realizar_transacao(conta, transacao)

def extrato_atual(usuarios):
    cpf = input("Qual o seu CPF?: ")
    cliente = [cliente for cliente in usuarios if cliente.cpf == cpf]

    if not cliente:
        print("Nenhum cliente com este CPF")
        return

    if not cliente.contas:
        print("Cliente não possui conta")
        return

    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Extrato vazio"
    else:
        for transacao in transacoes:
            extrato += f"{transacao['tipo']}: R$ {transacao['valor']:.2f}"

    print()
    print(f"Saldo atual é de R${conta.saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Qual o seu CPF?: ")
    cliente = [cliente for cliente in usuarios if cliente.cpf == cpf]

    if cliente:
        print("Cliente com o seu cpf já tem um cadastro")
        return

    nome = input("Nome: ")
    data_nascimento = input("data de nascimento (dd-mm-aaaa): ")
    endereco = input("endereço (rua, numero - bairro - cidade/estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    usuarios.append(cliente)

def criar_conta(numero_conta, usuarios, contas):
    cpf = input("Qual o seu CPF?: ")
    cliente = [cliente for cliente in usuarios if cliente.cpf == cpf]

    if not cliente:
        print("Nenhum cliente com este CPF")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)



    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar Usuario
    [c] Criar Conta
    [q] Sair

    =>"""

    usuarios = []
    contas = []
    continuar_operacao = "sim"

    while continuar_operacao == "sim":
        opcao = input(menu)

        if opcao == "d":
            depositar(usuarios)
        
        elif opcao == "s":
            sacar(usuarios)

        elif opcao == "e":
            extrato_atual(usuarios)
        
        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero = len(contas) + 1
            criar_conta(numero, usuarios, contas)

        elif opcao == "q":
            break

        else:
            print("Operação invalida, por favor selecione novamente a operação desejada.")

        print()
        continuar_operacao = input("Deseja continuar mechendo no banco?: ")