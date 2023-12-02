import random

opcao_computador = random.randint(0, 2)

if opcao_computador == 0:
    opcao_computador = 'pedra'
elif opcao_computador == 1:
    opcao_computador = 'papel'
else:
    opcao_computador = 'tesoura'

opcao_jogador = input("Escolha pedra, papel ou tesoura: ").lower()

if (opcao_jogador == 'pedra' and opcao_computador == 'tesoura') or \
   (opcao_jogador == 'tesoura' and opcao_computador == 'papel') or \
   (opcao_jogador == 'papel' and opcao_computador == 'pedra'):
    print("Jogador venceu!")
elif opcao_jogador == opcao_computador:
    print("Empate!")
else:
    print("Computador venceu!")

print(f"Jogador escolheu: {opcao_jogador}")
print(f"Computador escolheu: {opcao_computador}")
