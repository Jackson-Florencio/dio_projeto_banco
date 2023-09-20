def exibir_menu():
    print(menu)

def realizar_saque(saldo, saques_diarios, extrato):
    if saques_diarios == 0:
        print("Limite de saques diários atingido!")
        return saldo, saques_diarios, extrato

    saque = input("Digite o valor que deseja sacar: ")

    if not saque.isdigit():
        print("Digite apenas números!")

    saque = int(saque)

    if saque > saldo:
        print("Valor de saque maior que o saldo da conta!")

    elif saque > 500:
        print("Permitido apenas R$ 500.00 por saque!")
    
    else:
        saldo -= saque
        saques_diarios -= 1
        extrato += f"Você sacou {saque}\n"

    return saldo, saques_diarios, extrato

def realizar_deposito(saldo, extrato):
    deposito = input("Digite o valor de depósito: ")

    if not deposito.isdigit():
        print("Digite apenas números!")
    
    else:
        deposito = int(deposito)
        saldo += deposito
        extrato += f"Você depositou {deposito}\n"

    return saldo, extrato

menu = """
Selecione uma opção:
1 - Saque
2 - Depósito
3 - Ver extrato
4 - Sair
"""
saldo = 0
saques_diarios = 3
extrato = ""

while True:
    exibir_menu()
    opcao = input()

    if opcao == '4':
        print("Obrigado por utilizar nosso sistema!")
        break

    if not opcao.isdigit() or int(opcao) not in [1, 2, 3]:
        print("Opção inválida! Digite um número válido (1, 2, ou 3).")
    else:
        opcao = int(opcao)

        if opcao == 1:
            saldo, saques_diarios, extrato = realizar_saque(saldo, saques_diarios, extrato)
        elif opcao == 2:
            saldo, extrato = realizar_deposito(saldo, extrato)
        elif opcao == 3:
            print(extrato + f"R$ {saldo}\n")
