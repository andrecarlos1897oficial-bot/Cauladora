from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
        # Obtém os dados do formulário enviado via POST
    n1 = float(request.form['n1'])
    n2 = float(request.form['n2'])
    operacao = request.form['operacao']

    resultado = None

    if operacao == 'soma':
        resultado = n1 + n2
    elif operacao == 'subtracao':
        resultado = n1 - n2
    elif operacao == 'multiplicacao':
        resultado = n1 * n2
    elif operacao == 'divisao':
        if n2 != 0:
            resultado = n1 / n2
        else:
            resultado = "Erro: Divisão por zero não permitida"

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)