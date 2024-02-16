def depositar(saldo, valor, extrato):
    saldo += valor
    print("Valor depositado com sucesso")
    extrato += f"Deposito: R$ {valor:.2f}\n"
    return saldo, extrato

def sacar(saldo, extrato): 
    saldo -= valor
    print("Saque realizado com sucesso!")
    extrato += f"Saque: R$ {valor:.2f}\n"
    return saldo, extrato

def extrato_atual(extrato):
    print(extrato)
    print()
    print(f"Valor atual na conta é de: R$ {saldo:.2f}")
    return

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    if usuario:
        return "Não"
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    return "Sim"

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    if usuario:  
        print("Usuario cadastrado com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuario não encontrado")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuario
[c] Criar Conta
[q] Sair

=>"""

AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
continuar_operacao = "sim"
usuarios = []
contas = []
feito_com_sucesso = "Sim"


while continuar_operacao == "sim":
    opcao = input(menu)
    valor = 0

    if opcao == "d":
        valor = float(input("Digite o valor que sera depositado: ")) 
        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite maximo de saques diarios atingidos, por favor tente outro dia")
        elif saldo == 0:
            print("Você não possui saldo suficiente na conta para realizar esta operação")
        else:
            valor = float(input("Digite o valor que sera sacado: "))
            if valor>500:
                print("Valor de saque desejado é maior do que o limite maximo de saque que é de R$500.00")
            elif valor>saldo:
                print("Valor de saque desejado é maior do que o valor disponivel na conta")
            else:
                saldo, extrato = sacar(saldo, extrato)
        

    elif opcao == "e":
        extrato_atual(extrato)
    
    elif opcao == "u":
        feito_com_sucesso = criar_usuario(usuarios)
        if feito_com_sucesso == "Sim":
            print("Você cadastrou o usuario com sucesso!")
        else:
            print("O usuario deste cpf já esta cadastrado")

    elif opcao == "c":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)


    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")

    print()
    continuar_operacao = input("Deseja continuar mechendo no banco?: ")