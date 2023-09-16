while True:
    print("Menu de opções:")
    print("1 – Novo salário")
    print("2 – Férias")
    print("3 – Décimo terceiro")
    print("4 – Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == '1':
        salario = float(input("Digite o salário atual: "))
       
        if salario <= 210:
            novo_salario = salario * 1.15
       
        elif salario <= 600:
            novo_salario = salario * 1.10
       
        else:
            novo_salario = salario * 1.05
        print(f"Novo salário: R$ {novo_salario:.2f}")
    
    elif opcao == '2':
        salario = float(input("Digite o salário atual: "))
        valor_ferias = salario + (salario / 3)
        print(f"Valor das férias: R$ {valor_ferias:.2f}")
    
    elif opcao == '3':
        salario = float(input("Digite o salário atual: "))
        meses_trabalhados = int(input("Digite o número de meses de trabalho (até 12): "))
        if meses_trabalhados <= 12:
            decimo_terceiro = (salario * meses_trabalhados) / 12
            print(f"Valor do décimo terceiro: R$ {decimo_terceiro:.2f}")
        else:
            print("Número de meses de trabalho inválido. Deve ser no máximo 12.")
   
    elif opcao == '4':
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1, 2, 3 ou 4).")