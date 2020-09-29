from flask import Flask, render_template #fá render template
from markupsafe import escape
from flask import Flask, json
import urllib.request #importa url fyrir python til að sækja json url
#Listi fyrir frettir á fréttasíðu
app = Flask(__name__)

with urllib.request.urlopen("http://apis.is/petrol/") as url:
    data = json.loads(url.read().decode())

@app.route("/")
def home():
    return render_template("index.html", data=data) #senda data sem data í index skjalið

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
