nome_vendedor1 = input("Digite o nome do vendedor 1: ")
salario_fixo1 = float(input("Digite o salário fixo do vendedor 1: "))
vendas1 = float(input("Digite o valor total de vendas do vendedor 1: "))
nome_vendedor2 = input("Digite o nome do vendedor 2: ")
salario_fixo2 = float(input("Digite o salário fixo do vendedor 2: "))
vendas2 = float(input("Digite o valor total de vendas do vendedor 2: "))
comissao1 = vendas1 * 0.15
total_receber1 = salario_fixo1 + comissao1
comissao2 = vendas2 * 0.15
total_receber2 = salario_fixo2 + comissao2
print(f"TOTAL = R$ {total_receber1:.2f}")
print(f"TOTAL = R$ {total_receber2:.2f}")