import requests
import json
from tkinter import *

def ieskoti_filmo():
    filmo_pav = laukas1.get()
    url = f"http://www.omdbapi.com/?apikey=4a008e36&s={filmo_pav}"
    response = requests.get(url)
    data = json.loads(response.text)

    if data["Response"] == "False":
        rezultatas.config(text="Filmas nerastas.")
    else:
        rezultatas_str = ""
        for filmai in data["Search"]:
            rezultatas_str += f"{filmai['Title']} ({filmai['Year']})\n"
        rezultatas.config(text=rezultatas_str)

langas = Tk()

uzrasas1 = Label(langas, text="Įveskite filmo pavadinimą:")
laukas1 = Entry(langas)
mygtukas = Button(langas, text="Ieškoti", command=ieskoti_filmo)
rezultatas = Label(langas, text="")

uzrasas1.grid(row=0, column=0)
laukas1.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
rezultatas.grid(row=1, columnspan=3)

langas.mainloop()