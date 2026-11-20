saldo = 0.0

def ler_valor():
    while True:
        texto = input("Digite o valor: R$ ")
        try:
            valor = float(texto.replace(",", "."))
            if valor > 0:
                return valor
            print("O valor precisa ser maior que zero.")
        except ValueError:
            print("Valor inválido. Digite apenas números.")

def depositar(saldo):
    valor = ler_valor()
    saldo = saldo + valor
    print("Depósito feito com sucesso!")
    return saldo

def sacar(saldo):
    valor = ler_valor()
    if valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo = saldo - valor
        print("Saque feito com sucesso!")
    return saldo

def mostrar_saldo(saldo):
    print("Seu saldo é: R$", format(saldo, ".2f"))

while True:
    print()
    print("=== CAIXA ELETRÔNICO ===")
    print("1 - Saque")
    print("2 - Depósito")
    print("3 - Saldo")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        saldo = sacar(saldo)
    elif opcao == "2":
        saldo = depositar(saldo)
    elif opcao == "3":
        mostrar_saldo(saldo)
    elif opcao == "0":
        print("Obrigado por usar o caixa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
