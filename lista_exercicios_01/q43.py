materia1 = float(input("Digite a nota da matéria 1: "))
materia2 = float(input("Digite a nota da matéria 2: "))
materia3 = float(input("Digite a nota da matéria 3: "))
faltas_totais = int(input("Digite o número total de faltas: "))
aulas_por_materia = 10
total_aulas = 3 * aulas_por_materia
frequencia = ((total_aulas - faltas_totais) / total_aulas) * 100
resultado = materia1 > 7 and materia2 > 7 and materia3 > 7 and frequencia >= 75
print("Aluno aprovado?", resultado)