from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/a-hluti")
def ahluti():
    return render_template("kennitala.html")

@app.route("/kt/<kt>") #seinni kt kemur fra kennitala template 
def ktalan(kt): # setjum kt inn þarna til að vinna með það 
    summa = 0
    for item in kt:
        summa = summa + int(item) #þurfum að breita í int því allt er strengur enþá
    return render_template("ktsum.html",kt=kt,summa=summa) # skilar bæði kt og summu 


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
