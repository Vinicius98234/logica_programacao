hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input("Digite a hora inicial, minuto inicial, hora final e minuto final separados por espaço: ").split())

tempo_inicial_em_minutos = hora_inicial * 60 + minuto_inicial
tempo_final_em_minutos = hora_final * 60 + minuto_final

duracao_em_minutos = max(1, tempo_final_em_minutos - tempo_inicial_em_minutos)

duracao_horas = duracao_em_minutos // 60
duracao_minutos = duracao_em_minutos % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
