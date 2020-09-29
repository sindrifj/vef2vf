from flask import Flask, render_template #fá render template
from markupsafe import escape
from flask import Flask, json
import urllib.request #importa url fyrir python til að sækja json url
#Listi fyrir frettir á fréttasíðu
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/a-hluti")
def ahluti():
    return render_template("kennitala.html")

with open("/home/sindri/Documents/skoli2020/vef2vf/Verkefni-2 - json/static/frettirj.json",encoding="utf-8") as skra:
    frettirj = json.load(skra)
    print(frettirj)

@app.route("/b-hluti")
def bhluti():
    return render_template("frettir.html", frettirj=frettirj)

@app.route("/frett/<id>")
def frett(id):
    return render_template("frett.html",frettirj=frettirj,id=id) # fyrri er nafið í jason skjali

@app.route("/ktala/<kt>") #seinni kt kemur fra kennitala template 
def ktalan(kt): # setjum kt inn i þettana streng
    summa = 0
    for item in kt:
        summa = summa + int(item) #þurfum að breita í int því allt er strengur enþá
    return render_template("ktsum.html",kt=kt,summa=summa) # skilar bæði kt og summu

@app.route("/gengi")
def frett(id):
    return render_template("frett.html",frettirj=frettirj,id=id) # fyrri er nafið í jason skjali

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("pagenotfound.html"), 404

@app.errorhandler(500)
def servererror(error):
    return render_template("servererror.html"), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
