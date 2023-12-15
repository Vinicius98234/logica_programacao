def grito_de_natal(felicidade):
    if felicidade > 1:
        grito = "Feliz Nata" + "a" * (felicidade - 1) + "l!!"
        return grito
    else:
        return "A felicidade precisa ser maior que 1 para gritar 'Feliz Natal!!'"


