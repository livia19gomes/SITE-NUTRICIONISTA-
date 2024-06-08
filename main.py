# from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__,template_folder='Templates')


@app.route('/')
def index():
    return render_template(template_name_or_list='index.html')

@app.route('/calculadora')
def calculadora():
    return (render_template('calculadora.html', resultado=""))

@app.route('/resultado', methods=['POST'])
def resultado():
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    alt = altura ** 2
    imc = peso / alt
    if (imc < 18.5):
        tabela = 'Magreza'
    elif (imc >= 18.5) and (imc < 25):
        tabela = 'Normal'
    elif (imc >= 25) and (imc < 30):
        tabela = 'Sobrepeso'
    elif (imc >= 30) and (imc < 35):
        tabela = 'Obesidade Grau I'
    elif (imc >= 35) and (imc < 40):
        tabela = 'Obesidade Grau II'
    else:
        tabela = 'Obesidade Grau III'

    return render_template('calculadora.html', resultado=f'Seu IMC é: {imc} - {tabela}')

@app.route('/contato')
def contato():
    return (render_template('contato.html'))

@app.route('/botoes')
def botoes():
    return (render_template('botoes.html'))

@app.route('/blog')
def blog():
    return (render_template('blog.html'))

if __name__ == '__main__':
    app.run(debug=True)
