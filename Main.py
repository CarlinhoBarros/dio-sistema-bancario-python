def menu():
    """Exibe o menu de opções"""
    print("""
-------Menu-------
          
1 - Depósito
2 - Saque
3 - Extrato
    
0 - Sair"""
    )

def depositar(valor):
    if(valor <= 0):
        print("Valor inválido!")
    else:
        print(f"R$ {valor: .2f} depositado com sucesso!")
        global saldo, movimentos
        saldo += valor
        movimentos += f"Depósito: R$ {valor: .2f}\n"

def sacar(valor):
    global saldo, movimentos, LIMITE_SAQUES, VALOR_LIMITE
    if(valor <= 0):
        print("Valor inválido!")
    elif(valor > saldo):
        print("Saldo insuficiente!")
    elif(valor > VALOR_LIMITE):
        print(f"O valor excede o valor limite de saque por operação! (Limite: R$ {VALOR_LIMITE: .2f})")
    elif(saques >= LIMITE_SAQUES):
        print(f"Limite de saques diários atingido! (Limite: {LIMITE_SAQUES})")
    else:
        print(f"Saque de R$ {valor: .2f} realizado com sucesso!")
        saldo -= valor
        movimentos += f"Saque: R$ {valor: .2f}\n"

def extrato():
    print("##### EXTRATO #####")
    if(movimentos == ""):
        print("A conta não possui movimentações.")
    else:
        print(movimentos)
        print(f"Saldo: R$ {saldo: .2f}")

saldo = 0.
movimentos = ""
saques = 0
LIMITE_SAQUES = 3
VALOR_LIMITE = 500.


while(1):
    menu()
    opcao = int(input("Opção: "))

    if(opcao == 0):
        break
    elif(opcao == 1):
        valor = float(input("Informe o valor: "))
        
        depositar(valor)
    elif(opcao == 2):
        valor = float(input("Informe o valor: "))
        
        sacar(valor)
    elif(opcao == 3):
        extrato()
    else:
        print("Opção Inválida!")