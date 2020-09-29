# Þurfum þennan
from flask import Flask, json
1
# Tengjum skrána bekkur.json (verður að vera absolute url c:/Users/gjg/Desktop/Verkefni-2-json/json-daemi/)
with open("/home/sindri/Documents/skoli2020/vef2vf/Verkefni-2 - json//json-daemi/bekkur.json","r") as skra:
    bekkur = json.load(skra)

# Kíkjum i breytuna 
print(bekkur)




