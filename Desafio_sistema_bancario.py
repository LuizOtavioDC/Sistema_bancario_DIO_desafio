menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
continuar_operacao = "sim"



while continuar_operacao == "sim":
    opcao = input(menu)
    valor = 0

    if opcao == "d":
        valor = float(input("Digite o valor que sera depositado: "))
        saldo += valor
        print("Valor depositado com sucesso")
        extrato += f"Deposito: R$ {valor:.2f}\n"
    
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
                saldo -= valor
                print("Saque realizado com sucesso!")
                extrato += f"Saque: R$ {valor:.2f}\n"

    elif opcao == "e":
        print(extrato)
        print()
        print(f"Valor atual na conta é de: R$ {saldo:.2f}")
    
    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")

    print()
    continuar_operacao = input("Deseja continuar mechendo no banco?: ")