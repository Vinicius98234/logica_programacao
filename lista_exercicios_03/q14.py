#Passagem por valor
def passagem_por_valor(x):
    x += 10
    print("Dentro da função (passagem por valor):", x)
#Passagem por referencia
def passagem_por_referencia(lista):
    lista.append(4)
    print("Dentro da função (passagem por referência):", lista)


