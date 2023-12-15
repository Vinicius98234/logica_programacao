def verifica_parenteses(expressao):
    pilha = []

    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return "Erro - Parênteses fechados sem serem abertos."
            pilha.pop()

    if not pilha:
        return "OK - Parênteses foram abertos e fechados corretamente."
    else:
        return "Erro - Parênteses abertos sem serem fechados."

expressao = input("Digite uma expressão com parênteses: ")

resultado = verifica_parenteses(expressao)
print(resultado)
