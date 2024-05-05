menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair


"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("""

     """)
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
             saldo += valor 
             extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
             print("Operacão falhou! O valor informado é invalido.")
             print("""

     """)
    elif opcao == 2:
        print("""

     """)
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
             print("Operacão falhou! Você não tem saldo suficiente.")
             print("""

     """)
        elif excedeu_limite:
             print("Operação falhou! O valor do saque excede o limite.")
             print("""

     """)
        elif excedeu_saques:
             print("Operação falhou! Número máximo de saques excedidos.")
             print("""

     """)
        elif valor > 0:
             saldo -= valor
             extrato += f"Saque: R$ {valor:.2f}\n"
             numero_saques += 1
        else:
            print("Operacão falhou! O valor informado é invalido.")
            print("""

     """)
    elif opcao == 3:
          print("\n ===================EXTRATO===========")
          if extrato:
               print(extrato)
          else:
               print("Não foram realizadas movimentações.")

          print(f"\nSaldo: R$ {saldo:.2f}")
          print("========================================")
          print("""

     """)
    elif opcao == 0:
        break
    else:
        print("Operação inválida, por favor selecione a operação novamente.")
        print("""

""")