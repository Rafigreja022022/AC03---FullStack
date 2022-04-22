
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/retorno", methods=["post"])
def api():
    json = request.get_json()
    nome = json['student_name']
    nome = nome.upper()
    email = json['student_e_mail']
    email = email.upper()
    json['student_name'] = nome
    json['student_e_mail'] = email
    json['nome_e_mail'] = 'NOME: ' + json['student_name'] + '  -  ' + 'E-MAIL: ' + json['student_e_mail']
    return jsonify(json)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
