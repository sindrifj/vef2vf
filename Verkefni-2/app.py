from flask import Flask, render_template #fá render template
from markupsafe import escape
#Listi fyrir frettir á fréttasíðu
frettir = [
    ["0","Latur og kæru­laus","Wim Kieft, fyrr­ver­andi landsliðsmaður Hol­lands í knatt­spyrnu, skaut föst­um skot­um að Virgil van Dijk, varn­ar­manni Li­verpool, í viðtali við hol­lenska miðil­inn De Tel­egra­af á dög­un­um. Kieft er 57 ára gam­all í dag  en hann lék með liðum á borð við Ajax, Tor­ino, PSV og Bordeaux á sín­um ferli og þá lék hann 42 lands­leiki fyr­ir Hol­land frá 1981 til 1993. Van Dijk virk­ar eins og hann sé með haus­inn ein­hversstaðar allt ann­arsstaðar en hann á að vera,“ sagði Kieft í sam­tali við hol­lenska miðil­inn.\nHann hag­ar sér eins og út­brunn­in stjarna, bæði með Li­verpool og hol­lenska landsliðinu og mér finnst hann ekki leggja nærri því jafn mikið á sig og liðsfé­lag­ar hans gera í leikj­um. Hann er latur og kæru­laus í þokka­bót og hleyp­ur oft á tíðum frá bolta­mann­in­um í stað þess að gefa sig all­an í tæk­ling­arn­ar.\nÞað tók miðvörðinn lang­an tíma að kom­ast í fremstu röð en hann hef­ur verið einn sá besti und­an­far­in tvö tíma­bil. Hann má ekki hætta núna og þarf að halda áfram að vera gagn­rýn­inn á sjálf­an sig. Hann þarf að stíga upp og það þarf að hrista hann dug­lega því hann hef­ur verið langt frá sínu besta í fyrstu tveim­ur leikj­um tíma­bils­ins með Li­verpool,“ bætti Kieft við.","Höfundur"],
    ["1","Helgi Björns tek­ur við Borg­inni","Þau stórtíðindi ber­ast úr veit­inga­geir­an­um að sjálf­ur Helgi Björns sé að taka við rekstri á veit­inga­rými Hót­els Borg­ar en þar er meðal ann­ars að finna hinn forn­fræga Gyllta sal. Helgi grein­ir frá þessu í helgar­blaði Frétta­blaðsins en þar seg­ist hann ekki hafa geta skor­ast und­an þegar tæki­færið bauðst. Hann hyggst, að eig­in sögn, hefja Borg­ina aft­ur til fyrri dýrðar ásamt Guðfinni Karls­syni veit­inga­manni. Það verði dansað á ný í Gyllta saln­um og vænt­an­lega boðið upp á ít­alsk­an mat með.","Höfundur"],
    ["2","Safn­plata með lög­um Ragga Bjarna kom­in út","Í dag kom út safn­plata sem inni­held­ur 45 lög í flutn­ingi Ragn­ars Bjarna­son­ar frá glæsi­leg­um 65 ára ferli hans. Plat­an ber titil­inn Þannig týn­ist tím­inn: Vin­sæl­ustu lög Ragga Bjarna. 22. sept­em­ber er fæðing­ar­dag­ur Ragn­ars en hann hefði orðið 86 ára í dag. Ragn­ar lést þann 25. fe­brú­ar á þessu ári 85 ára að aldri. Plat­an verður fyrst um sinn aðgengi­leg á Spotify og öðrum streym­isveit­um en þegar nær dreg­ur jól­um kem­ur hún út á vínyl og geisladiski.","Höfundur"],
    ["3","Karl kall­ar eft­ir Mars­hall-aðstoð við um­hverfið","Karl Bretaprins kall­ar eft­ir því að heim­ur­inn setji sig í stríðsstell­ing­ar til þess að tak­ast á við lofts­lags­vána. Í ávarpi sínu á lofts­lagsviku New York-borg­ar sagði Karl að sú yf­ir­vof­andi hætta sem lofts­lags­vá­in skapaði, sem og tap líf­fræðilegs fjöl­breyti­leika, myndi áhrif kór­ónu­veirufar­ald­urs­ins að engu gera.","Höfundur"]
]
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/a-hluti")
def ahluti():
    return render_template("kennitala.html")

@app.route("/b-hluti")
def bhluti():
    return render_template("frettir.html", frettir=frettir)

@app.route("/frett/<int:id>")
def frett(id):
    return render_template("frett.html",frett=frettir[id],nr=id)

@app.route("/ktala/<kt>") #seinni kt kemur fra kennitala template 
def ktalan(kt): # setjum kt inn i þettana streng
    summa = 0
    for item in kt:
        summa = summa + int(item) #þurfum að breita í int því allt er strengur enþá
    return render_template("ktsum.html",kt=kt,summa=summa) # skilar bæði kt og summu 

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("pagenotfound.html"), 404

@app.errorhandler(500)
def servererror(error):
    return render_template("servererror.html"), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
