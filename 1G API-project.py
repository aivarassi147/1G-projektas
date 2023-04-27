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
        
       
    
    
  ------------------------------------------------
from tkinter import *
langas = Tk()


def spausdinti():
    ivesta = laukas1.get()
    rezultatas["text"] = f"visi filmai su tavo zodziu"

uzrasas1 = Label(langas, text="ivesk zodi")
laukas1 = Entry(langas)
mygtukas = Button(langas, text="ziurim ka turim", command=spausdinti)
rezultatas =Label(langas, text="")

uzrasas1.grid(row=0, column=0)
laukas1.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
rezultatas.grid(row=1, columnspan=3)

langas.mainloop()
