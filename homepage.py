import tkinter as tk
from tkinter import messagebox
import json

screen = tk.Tk()
screen.title("PetreDumitruFlorin")
screen.geometry("800x600")

# RMA
rma_text = tk.Label(text = "RMA", bg = "grey", fg ="white")
rma_text.place(x = 5, y = 20)
rma_get = tk.StringVar()
rma_entry = tk.Entry(textvariable = rma_get)
rma_entry.place(x = 120, y = 23)

# data
data_text = tk.Label(text="DATA: ", bg = "grey", fg = "white")
data_text.place(x = 5, y = 60)
data_get = tk.StringVar()
data_entry = tk.Entry(textvariable = data_get)
data_entry.place(x = 120, y = 63)

# seria
seria_text = tk.Label(text="SERIA: ", bg = "grey", fg = "white")
seria_text.place(x = 5, y = 100)
seria_get = tk.StringVar()
seria_entry = tk.Entry(textvariable = seria_get)
seria_entry.place(x = 120, y = 103)

# nume lucrator
name_text = tk.Label(text = "NUME LUCRATOR: ", bg = "grey", fg = "white")
name_text.place(x = 5, y = 140)
name_get = tk.StringVar()
name_entry = tk.Entry(textvariable = name_get, width= "30")
name_entry.place(x = 120, y = 143)

# echipament
echipament_text = tk.Label(text = "ECHIPAMENT: ", bg = "grey", fg = "white")
echipament_text.place(x = 5, y = 180)
echipament_get = tk.StringVar()
echipament_entry = tk.Entry(textvariable = echipament_get)
echipament_entry.place(x = 120, y = 183)

# client
client_text = tk.Label(text = "CLIENT: ", bg = "grey", fg = "white")
client_text.place(x = 5, y = 220)
client_get = tk.StringVar()
client_entry = tk.Entry(textvariable = client_get)
client_entry.place(x = 120, y = 220)

# garantie
garantie_text = tk.Label(text = "GARANTIE: ", bg = "grey", fg = "white")
garantie_text.place(x = 5, y = 260)
garantie_get = tk.StringVar()
garantie_entry = tk.Entry(textvariable = garantie_get)
garantie_entry.place(x = 120, y = 263)


def get_input():
    name = name_get.get()
    rma = rma_get.get()
    data = data_get.get()
    seria = seria_get.get()
    echipament = echipament_get.get()
    client = client_get.get()
    garantie = garantie_entry.get()

    messagebox.showinfo("DONE", f"A fost salvat {seria}_{client}.json")

    json_data = {
              "nume_lucrator": name,
              "RMA": rma,
              "data": data,
              "seria": seria,
              "echipament": echipament,
              "client": client,
              "garantie": garantie
       }

    with open(f"json\{seria}_{client}.json", "w") as f:
        json.dump(json_data, f, indent=1)

submit = tk.Button(text = "OK", width="30", height="2", bg ="blue", command=get_input)
submit.place(x = 5, y = 310)

#CONTROL ELECTRIC
def electric_page():
    screen.destroy()
    import control_electric

      
buttonExample = tk.Button(screen, 
              text="CONTROL ELECTRIC",
              width="30", height="2",
              bg="blue",
              command=electric_page)
buttonExample.place(x = 5, y = 350)

# schimba pagina
def go_constatare():
    screen.destroy()
    import constatare_service


def go_deviz():
    screen.destroy()
    import deviz

def go_fisa():
    screen.destroy()
    import fisa_service


constatare = tk.Button(text = "Constatare Service", width="30", height="2", bg="#ffdd91", command=go_constatare)
constatare.place(x = 350, y = 70)

constatare = tk.Button(text = "Deviz Service", width="30", height="2", bg="#ffdd91", command=go_deviz)
constatare.place(x = 570, y = 70)

service_fisa= tk.Button(text = "Fisa Service", width="30", height="2", bg ="#ffdd91", command=go_fisa)
service_fisa.place(x = 420, y = 120)

info = tk.Label(text = "Introduci datele si apesi OK, dupa care apesi Control Electric", fg="red")
info.place(x = 5, y = 400)

screen.mainloop()