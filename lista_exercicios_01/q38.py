idade_dias = int(input("Digite a idade em dias: "))
anos = idade_dias // 365
meses = (idade_dias % 365) // 30
dias = (idade_dias % 365) % 30
print(f"{anos} ano(s), {meses} mês(es) e {dias} dia(s)")