nota1 = float(input("Digite a nota 1 (de 0 a 10.0): "))
nota2 = float(input("Digite a nota 2 (de 0 a 10.0): "))
nota3 = float(input("Digite a nota 3 (de 0 a 10.0): "))
peso_nota1 = 2
peso_nota2 = 3
peso_nota3 = 5
media_ponderada = (nota1 * peso_nota1 + nota2 * peso_nota2 + nota3 * peso_nota3) / (peso_nota1 + peso_nota2 + peso_nota3)
print(f"A média ponderada do aluno é: {media_ponderada:.2f}")
