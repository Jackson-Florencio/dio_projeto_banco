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
def cadastro_usuario():
    nome = input("Nome: ").split(" ")
    return nome

def calcular_primeiro_digito_verificador(cpf_base):
    soma = 0
    peso = 10

    for digito in cpf_base:
        soma += int(digito) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - resto

    return primeiro_digito

def calcular_segundo_digito_verificador(cpf_base):
    soma = 0
    peso = 11

    for digito in cpf_base:
        soma += int(digito) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - resto

    return segundo_digito

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if not cpf.isdigit() or len(cpf) != 11 or len(set(cpf)) == 1:
        return False  
    
    cpf_base = cpf[:9]
    primeiro_digito = calcular_primeiro_digito_verificador(cpf_base)
    cpf_base += str(primeiro_digito)
    segundo_digito = calcular_segundo_digito_verificador(cpf_base)
    cpf_base += str(segundo_digito)

    return cpf_base == cpf

def cpf_completo(cpf_base):
    primeiro_digito = calcular_primeiro_digito_verificador(cpf_base)
    segundo_digito = calcular_segundo_digito_verificador(cpf_base)
    cpf_completo = cpf_base + str(primeiro_digito) + str(segundo_digito)
    return cpf_completo

def data_nascimeto():   
    nascimento = input("Digite a data de nascimeto DD/MM/AAAA: ")
    nascimento = nascimento.replace("/", "")

    if not nascimento.isdigit() or len(nascimento) != 8:
        print("Entrada inválida, por favor digite a data no formato DD/MM/AAAA")

    else:
        dia = int(nascimento[:2])
        mes = int(nascimento[2:4])
        ano = int(nascimento[4:])

        if (1 <= dia <= 31) and (1 <= mes <= 12) and (1900 <= ano <= 2023):
            nascimento_formatado = f"{dia:02d}/{mes:02d}/{ano:04d}"
            return nascimento_formatado
        else:
            print("Valores de dia, mês ou ano fora da faixa aceitável.")
    return nascimento

def cadastro_endereco():
    endereco = ""
    logradouro = input("Digite o logradouro: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite a sigla do estado: ")
    endereco += f"Logradouro: {logradouro}, bairro: {bairro}, cidade: {cidade}/{estado}"
    return endereco

    
menu = """
Selecione uma opção:
1 - Saque
2 - Depósito
3 - Ver extrato
4 - Cadastrar usuário
5 - Sair
"""
saldo = 0
saques_diarios = 3
extrato = ""
cpf = ""
usuarios_cadastrados = []
conta = 0
endereco = ""


while True:
    exibir_menu()
    opcao = input()

    if opcao == '5':
        print("Obrigado por utilizar nosso sistema!")
        break

    if not opcao.isdigit() or int(opcao) not in [1, 2, 3, 4]:
        print("Opção inválida! Digite um número válido (1, 2, 3, 4 ou 5!).")
    else:
        opcao = int(opcao)

        if opcao == 1:
            saldo, saques_diarios, extrato = realizar_saque(saldo, saques_diarios, extrato)
        elif opcao == 2:
            saldo, extrato = realizar_deposito(saldo, extrato)
        elif opcao == 3:
            print(extrato + f"R$ {saldo}\n")
        elif opcao == 4:
            nome = cadastro_usuario()
            cpf_digitado = input("Digite o CPF: ")
            
            cpf_existente = False
            
            for usuario in usuarios_cadastrados:
                if usuario["cpf"] == cpf_digitado:
                    cpf_existente = True
                    print("CPF já cadastrado")
                    break
                
            if not cpf_existente:
                if not validar_cpf(cpf_digitado):
                    print("CPF Inválido")
                else:
                    data_nascimeto = data_nascimeto()
                    endereco = cadastro_endereco()
                    conta +=1
                    usuario = {
                        "nome": nome,
                        "cpf": cpf_digitado,
                        "data_nascimeto": data_nascimeto,
                        "edereco": endereco,
                        "conta": conta,
                        "agencia": "0001"
                    }
                    usuarios_cadastrados.append(usuario)
                    print(usuario)
                    print("Usuário cadastrado com sucesso!")
           
