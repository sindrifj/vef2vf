from flask import Flask, render_template #fá render template
from markupsafe import escape
from flask import Flask, json
from jinja2 import ext # etta er svo hægt sé að nota do 
import urllib.request #importa url fyrir python til að sækja json url
#Listi fyrir frettir á fréttasíðu

app = Flask(__name__)

app.jinja_env.add_extension(ext.do) # þetta segir að við ætlum að nota do úr ext

with urllib.request.urlopen("http://apis.is/petrol/") as url:
    data = json.loads(url.read().decode())

#comp = data["results"][0]["company"] # finna fyrirtæki þar sem þetta er dictunary með nested lista af dictunary
#print(comp)

@app.route("/")
def home():
    return render_template("index.html", data=data) #senda data sem data í index skjalið

@app.route("/company/<company>") #sækjum company eins og {{item.comany }} í html
def comp(company): # company er færibreytan hér fyrir ofan
    return render_template("company.html", data=data, com=company) #senda data sem data í company skjalið og company sem com

@app.route("/moreinfo/<key>") #sækjum key eins og {{item.key }} í html
def more(key): # key er færibreytan hér fyrir ofan
    return render_template("moreinfo.html", data=data, k=key) #senda data sem data í company skjalið og company sem com

@app.route("/eldsneyti")
def eldsneyti():
    return render_template("eldsneyti.html", data=data) #senda data sem data í index skjalið

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("pagenotfound.html"), 404

@app.errorhandler(500)
def servererror(error):
    return render_template("servererror.html"), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
