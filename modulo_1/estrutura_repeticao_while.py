opcao = -1
saque = 0.0
saldo = 2000.0

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0]Sair do programa \n: "))

    if opcao == 1:
        saque = float(input("Digite o valor do saque: R$"))
        if saldo >= saque:
            saldo -= saque
            print(f"saque de R${saque} realizado com sucesso!")
        else:
            print("Saldo Insuficiente!")
    elif opcao == 2:
        print(f"Seu saldo é de R${saldo}")
    elif opcao == 0:
        print("Obrigado por usar nosso sistema!")
    else:
        print("Opção Inválida!")
