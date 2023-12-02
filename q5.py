numero_mes = int(input("Digite um número de 1 a 12: "))
if 1 <= numero_mes <= 12:
    meses_do_ano = [
        "Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    nome_mes = meses_do_ano[numero_mes - 1]
    print(f"O mês correspondente ao número {numero_mes} é: {nome_mes}")
else:
    print("Número inválido. Digite um valor de 1 a 12.")
