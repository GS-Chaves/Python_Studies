saldo = 2000.0
opcao = int(input("informe uma opção: \n[1] Sacar \n[2] Extrato\n "))

if opcao == 1:
    saque = float(input("Digite o valor do saque: R$"))
    if saldo >= saque:
        saldo -= saque
        print(f"saque de R${saque} realizado com sucesso!")
    else:
        print("Saldo Insuficiente!")
elif opcao == 2:
    print(f"Seu saldo é de R${saldo}")
else:
    print("Opção Inválida!")
