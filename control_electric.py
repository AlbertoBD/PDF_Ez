import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import ttk, filedialog, messagebox
import os
import json

directory_path = os.getcwd()

screen = tk.Tk()
screen.geometry("350x600")
screen.title("Control Electric")

#
trucam1 = ["Pornire si autotestare", "Iluminarea ecranului LED", "Unitatea de semnal audio", "Functionare tastatura cauciuc", "Functionare tastataura digitala", "Aliniere ecran LED"]
aq = ["Pornire si autotestare", "Iluminarea ecranului LED", "Unitatea de semnal audio", "Led-urile de avertizare luminoasa", "Functionare tastatura", "Acumulatorii Litiu/bateriile", "Placa de baza pentru imprimare"]

v = tk.IntVar()
tk.Radiobutton(screen, 
               text="TruCAM 1 & 2",
               padx = 20, 
               variable=v,
               bg="yellow",
               value=1).place(x = 5, y = 20)

tk.Radiobutton(screen, 
               text="AQ",
               padx = 20, 
               variable=v,
               bg="yellow",
               value=2).place(x = 200, y = 20)
total  = 1
if v == 1:
    for items in trucam1:
        total += 1
        tk.Label(screen, text = items).grid(row=total, column = 0)

# LISTE        
ok = []
obs = []
# inca liste
ok_list = []
obs_list = []


def show_data():
    total  = 1
    if v.get() == 1:
        for items in trucam1:
            total += 1

            tk.Label(screen, text = items).place(x = 100, y = 20 + total * 57)

            ok_entry = Combobox(screen, values=["OK", "NOK"])
            ok_entry.place(x = 20, y = 50 + total * 57)
            ok.insert(0, ok_entry)

            obs_entry = tk.Entry(screen)
            obs_entry.place(x = 200, y = 50 + total * 57)
            obs.insert(0, obs_entry)
    elif v.get() == 2:
        for things in aq:
            total += 1

            tk.Label(screen, text = things).place(x = 100, y = 20 + total * 57)

            ok_entry = Combobox(screen, values=["OK", "NOK"])
            ok_entry.place(x = 20, y = 50 + total * 57)
            ok.insert(0, ok_entry)

            obs_entry = tk.Entry(screen)
            obs_entry.place(x = 200, y = 50 + total * 57)
            obs.insert(0, obs_entry)



def get_input():
    for x in ok:
        ok_list.append(x.get())
    for y in obs:
        obs_list.append(y.get())
    
    ok.clear()
    obs.clear()

    ok_list.reverse()
    obs_list.reverse()


def select_file():
    filetypes = (
        ('json files', '*.json'),
        ('All files', '*.*')
    )

    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir=f"{directory_path}\Json",
        filetypes=filetypes)

    return filename 

def add_to_json():
    get_input()
    json_name = select_file()

    messagebox.showinfo("DONE", "DONE")

    if len(ok_list) == 6:
        json_data = {
            "nume_electric": [x for x in trucam1],
            "ok_electric": [x for x in ok_list],
            "obs_electric": [x for x in obs_list]
        }
    elif len(ok_list) == 7:
        json_data = {
            "nume_electric": [x for x in aq],
            "ok_electric": [x for x in ok_list],
            "obs_electric": [x for x in obs_list]
    }
   
    with open(f"{json_name}", "r") as ex:
        ex_data = json.load(ex)
    json_data.update(ex_data)

    with open(f"{json_name}", "w") as f:
        json.dump(json_data, f, indent=1)



# BUTTONS
afiseaza = tk.Button(screen, text = "Afiseaza", command=show_data).place(x = 140, y = 50)
save = tk.Button(screen, text = "SAVE", command=add_to_json).place(x = 80, y = 550, width= 80, height=40)

def createNewWindow():
    screen.destroy()
    import constatare_service

      
buttonExample = tk.Button(screen, 
              text="NEXT",
              width="10", height="2",
              bg="orange",
              command=createNewWindow)
buttonExample.place(x = 200, y = 550)


screen.mainloop()