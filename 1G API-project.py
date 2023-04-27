import requests
import json

filmo_pav = input("Įveskite filmo pavadinimą: ")
url = "http://www.omdbapi.com/?apikey=4a008e36&s=" + filmo_pav

response = requests.get(url)
duomenys = json.loads(response.text)

if duomenys["Response"] == "False":
    print("Filmas nerastas.")
else:
    for filmai in duomenys["Search"]:
        print(filmai["Title"], "(", filmai["Year"], ")")