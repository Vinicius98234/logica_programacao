valor = float(input("Digite o valor monetário: "))
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
print("NOTAS:")
for nota in notas:
    quantidade_notas = int(valor // nota)
    valor %= nota
    print(f"{quantidade_notas} nota(s) de R$ {nota:.2f}")
print("MOEDAS:")
for moeda in moedas:
    quantidade_moedas = int(valor // moeda)
    valor %= moeda
    print(f"{quantidade_moedas} moeda(s) de R$ {moeda:.2f}")