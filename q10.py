from flask import Flask, render_template, request

import random

app = Flask(__name__)

numero_secreto = random.randint(0, 100)
@app.route("/", methods=['GET', 'POST'])
def checar_palpite():

    mensagem = ''
    if request.method == 'POST':
        palpite = request.form['palpite']

        palpite= int(palpite)
        print(type(palpite))

        if palpite > numero_secreto:
            mensagem= ("tente um numero menor")
        elif palpite < numero_secreto:
            mensagem= ("tente um numero maior")
        else:
            mensagem= (f"Parabéns!! Você acertou o numero {numero_secreto}")

    return render_template('adivinhar_numero.html', mensagem=mensagem)