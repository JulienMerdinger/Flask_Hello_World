from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

@app.route('/somme/<int:val1>/<int:val2>')
def somme(val1, val2):
    return "<h2>La somme de votre valeur est : </h2>" + str(val1 + val2)

@app.route('/parite/<int:val>')
def pair(val):
  if val % 2 == 0:
    return str(val) + "<p>est pair.</p>"
  else:
    return str(val) + "<p>est impaire.</p>"

@app.route('/somme_global/<string:valeurs>')
def somme_global(valeurs):
  lst = valeurs.split('/')
  somme = lst[0]
  for i in range (len(lst)-1):
    somme += lst[i+1]
  return "La somme des éléments est:" + str(somme)
  

                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)

