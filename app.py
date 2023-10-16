from flask import Flask, request,flash, render_template, jsonify,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
import requests
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///banco.db"
app.config["SECRET_KEY "] = "its privace man"
db = SQLAlchemy(app)

class cadastro_cep(db.Model):
    __tablename__= "Cep"
    id = db.Column(db.Integer, primary_key=True)
    num_cep = db.Column(db.String(8))
    logradouro = db.Column(db.String(50))
    bairro = db.Column(db.String(30))
    cidade = db.Column(db.String(40))
    ddd = db.Column(db.String(5))
    uf = db.Column(db.String(4))

@app.route("/")
def index():
    return redirect("/busca")

@app.route("/busca", methods=["GET", "POST"])
def busca_cep():
    if request.method == "POST":
        cep = request.form["cep"]
        link_cep = f'https://viacep.com.br/ws/{cep}/json/'
        resp = requests.get(link_cep)
        try:
            dicta = resp.json()
            print(dicta)
            salv = cadastro_cep()
            salv.num_cep = dicta['cep']
            salv.cidade = dicta['localidade']
            salv.bairro = dicta['bairro']
            salv.logradouro = dicta['logradouro']
            salv.uf = dicta['uf']
            salv.ddd = dicta['ddd']
            db.session.add(salv)
            db.session.commit()
        except:
            print("Erro na requisição")
    else:
        print("Erro de conexão")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8500)