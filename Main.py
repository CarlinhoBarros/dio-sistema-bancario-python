def menu():
    """Exibe o menu de opções"""
    print("""
-------Menu-------
          
1 - Depósito
2 - Saque
3 - Extrato
4 - Cadastrar usuário
5 - Cadastrar Conta
6 - Listar Contas
    
0 - Sair"""
    )

def depositar(valor, saldo, extrato, /):
    if(valor <= 0):
        print("Valor inválido!")
    else:
        print(f"R$ {valor: .2f} depositado com sucesso!")
        saldo += valor
        extrato += f"Depósito: R$ {valor: .2f}\n"
    
    return saldo, extrato

def sacar(*, valor, saldo, extrato, saques, limite_saques, valor_limite):
    if(valor <= 0):
        print("Valor inválido!")
    elif(valor > saldo):
        print("Saldo insuficiente!")
    elif(valor > valor_limite):
        print(f"O valor excede o valor limite de saque por operação! (Limite: R$ {valor_limite: .2f})")
    elif(saques >= limite_saques):
        print(f"Limite de saques diários atingido! (Limite: {limite_saques})")
    else:
        print(f"Saque de R$ {valor: .2f} realizado com sucesso!")
        saldo -= valor
        extrato += f"Saque: R$ {valor: .2f}\n"
        saques += 1
    
    return saldo, extrato, saques

def exibir_extrato(extrato, /, saldo):
    print("##### EXTRATO #####")
    if(extrato == ""):
        print("A conta não possui movimentações.")
    else:
        print(extrato)
        print(f"Saldo: R$ {saldo: .2f}")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    cpf = formatar_cpf(cpf)
    if(not(cpf_is_valido(cpf))):
        print("CPF Inválido!")
        return

    if(cpf_cadastrado(cpf=cpf, usuarios=usuarios)):
        print("Usuário já cadastrado!")
        return
    
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = cadastrar_endereco()

    usuario = {
        cpf: {
            "nome" : nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco
        }
    }

    print("Cadastro realizado com sucesso!")

    usuarios.update(usuario)

def cadastrar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF: ")
    cpf = formatar_cpf(cpf)
    
    if(not(cpf_is_valido(cpf))):
        print("CPF Inválido!")
        return

    if(not(cpf_cadastrado(cpf=cpf, usuarios=usuarios))):
        print("Usuário não cadastrado!")
        return
    
    numero_conta = gerar_numero_conta(contas)
    usuario = {}
    usuario.update(usuarios[cpf])
    conta = {
        "numero_conta": numero_conta,
        "agencia": agencia,
        "usuario": usuario,
    }

    print("Conta cadastrada com sucesso!")

    contas.append(conta)

def gerar_numero_conta(contas):
    numero_conta = len(contas) + 1
    
    return numero_conta

def listar_contas(contas):
    for item in contas:
        print(item)

def cpf_cadastrado(cpf, usuarios):
    return True if cpf in usuarios else False

def formatar_cpf(cpf):
    cpf = str(cpf)
    #caracteres especiais
    caracteres = ",.;:/'!@#$%*-=+ "
    #removendo os caracteres da string
    for char in caracteres:
        cpf = cpf.replace(char, "")
    
    return cpf

def cpf_is_valido(cpf):
    return True if(len(cpf) == 11) else False

def cadastrar_endereco():
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    endereco = {
        "logradouro": logradouro, 
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado
    }

    return endereco

def main():
    contas = []
    usuarios = {}
    saldo = 0.
    extrato = ""
    saques = 0
    LIMITE_SAQUES = 3
    VALOR_LIMITE = 500.
    AGENCIA = "0001"

    while(1):
        menu()
        opcao = int(input("Opção: "))

        if(opcao == 0):#sair
            break
        elif(opcao == 1):#depositar
            valor = float(input("Informe o valor: "))
            
            saldo, extrato = depositar(valor, saldo, extrato)
        elif(opcao == 2):#sacar
            valor = float(input("Informe o valor: "))
            
            saldo, extrato, saques = sacar(
                valor=valor, saldo=saldo, extrato=extrato,
                saques=saques, limite_saques=LIMITE_SAQUES,
                valor_limite=VALOR_LIMITE
            )
        elif(opcao == 3):#exibir_extrato
            exibir_extrato(extrato, saldo=saldo)
        elif(opcao == 4):#cadastrar_usuario
            cadastrar_usuario(usuarios=usuarios)#por ser um dicionario e não estar sendo enviado a cópia, pode ser modificado no próprio método
        elif(opcao == 5):#cadastrar_conta
            cadastrar_conta(AGENCIA, contas, usuarios)
        elif(opcao == 6):#listar_contas
            listar_contas(contas)
        else:
            print("Opção Inválida!")

main()
