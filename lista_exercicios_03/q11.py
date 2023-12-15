def traduzir_plus2(entrada):
    traducoes = {
        "jqlg": "Hoje",
        "xqw": "vou",
        "rtqitcoct": "programar"
    }

    palavras = entrada.split(" ")

    traducao_portugues = []
    for palavra in palavras:
        traducao_portugues.append(traducoes.get(palavra, palavra))

    return " ".join(traducao_portugues)

comando_plus2 = 'rtkpv("jvvru://ujqtvwtn.cv/eDIPX")'
comando_traduzido = traduzir_plus2(comando_plus2)

print(comando_traduzido)
