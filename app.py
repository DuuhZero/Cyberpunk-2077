from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')
@app.route("/comprar.html")
def comprar():
  return render_template('comprar.html')
@app.route("/contato.html")
def contatos():
  return render_template('contato.html')
@app.route("/index.html")
def index():
  return render_template('index.html')



app.run(debug=True)