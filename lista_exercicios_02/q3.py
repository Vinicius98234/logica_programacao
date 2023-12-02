consumo_kwh = float(input("Digite a quantidade de kWh consumida: "))
tipo_instalacao = input("Digite o tipo de instalação (R para residências, I para indústrias, C para comércios): ").upper()

if tipo_instalacao == 'R':
     if consumo_kwh <= 500:
        preço = 0.40
     else:
        preço = 0.65

elif tipo_instalacao == 'C':
    if consumo_kwh <= 1000:
        preço =   0.55
    else:
        preço =   0.60

elif tipo_instalacao == 'I':
    if consumo_kwh <= 5000:
        preço =  0.60
    else:
        preço =   0.65
else:
    print("Tipo de instalação inválido. Por favor, digite R, I ou C.")

preco_pagar = consumo_kwh * preço

print(f"O preço a pagar pelo fornecimento de energia elétrica é: R$ {preco_pagar:.2f}")
