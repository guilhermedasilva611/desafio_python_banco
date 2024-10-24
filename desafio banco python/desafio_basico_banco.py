import textwrap

def menu():
    menu = """
    =====MENU=====
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [nu]\tNovo usuário
    [s]\tSair
    ==>"""
    return input(textwrap.dedent(menu))#textwrap melhora a visualização

def sacar(*, saldo, valor, extrato, limite, numero_saques, excedeu_saques, excedeu_saldo, excedeu_limite, limite_saques):#tirar valor disponivel
    valor = (input("Digite o valor para sacar!"))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:#verifica se é verdadeiro
        print("\n!ERRO! Operação falhou, saldo insuficiente!")
    
    elif excedeu_limite:
        print("\n!ERRO! Operação falhou, o valor excedeu o limite!")
    
    elif excedeu_saques:
        print("\n!ERRO! Operação falhou, o limite de saques excedidos!")
    
    elif valor > 0:
        saldo -= valor
        extrato = f"Saque:\t\tR${valor:.2f}\n"
        numero_saques += 1
        print("Saque Realizado com sucesso!")
    
    else:
        print("O valor inforamado está inválido!")

    return saldo, extrato

def depositar(saldo, valor, extrato, /):#depositar não precisa especificar a atribuição do valor
        if valor > 0:
            saldo += valor
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\nDeposito realizado com sucesso!")
        else:
            print("\nO valor informado não pode ser inserido!")

        return saldo, extrato

def exibir_extrato(saldo, /, *,extrato):#exibir
    print("===============EXTRATO===============") 
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"Saldo:\t\t R$ {saldo:.2f}")
    print("=====================================")

def filtrar_usuario(cpf, usuarios):#filtrar usuario
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):#criar ususario
    cpf = input("Informe o CPF(SOMENTE NUMERO!):")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o endereço(logradouro, nro - bairro - cidade/sigla estado):")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):#vincular com usuario
    cpf = input("Digite o  CPF do usúario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n===Conta criada com sucesso!===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuario não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta('agencia')}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t\{conta['usuario']['nome']}        
        """
        print("=" + 100)
        print(textwrap.dedent(linha))

def main():

    #constantes
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []   
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor,  extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )


        elif opcao == "e":
           exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()