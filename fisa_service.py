from pdf_template import Template as pdf
import json
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import StringVar, filedialog
from tkinter.constants import END
import os


directory_path = os.getcwd()

screen = tk.Tk()
screen.geometry("800x600")
screen.title("Fisa Service")

# liste preluare input
cauza_defectiune = []
stare_iesire = []
ok = []
ok_f = []
operatiuni_list = []

# widgets
cauza_text = tk.Label(text="Cauza defectiune: ", bg = "grey", fg = "white")
cauza_text.place(x = 5, y = 5)
cauza_entry = tk.Text(screen)
cauza_entry.place(x = 5, y = 25, width = "300", height = "100")

ok_text = tk.Label(text="Produs reparat: ")
ok_text.place(x = 5, y = 130)
ok_entry = Combobox(screen, values=["DA", "NU"])
ok_entry.place(x = 150, y = 130)
ok.append(ok_entry)

garantii_text = tk.Label(text="Garantii 1 an:")
garantii_text.place(x = 5, y = 150)
garantii_entry = Combobox(screen, values=["DA", "NU"])
garantii_entry.place(x = 150, y = 150)
ok.append(garantii_entry)

repar_text = tk.Label(text="Se poate repara:")
repar_text.place(x = 5, y = 170)
repar_entry = Combobox(screen, values=["DA", "NU"])
repar_entry.place(x = 150, y = 170)
ok.append(repar_entry)

producator_text = tk.Label(text="Trb trimis la producator:")
producator_text.place(x = 5, y = 190)
producator_entry = Combobox(screen, values=["DA", "NU"])
producator_entry.place(x = 150, y = 190)
ok.append(producator_entry)

operatiuni_text = tk.Label(text="Operatiuni efectuate: ", bg = "grey", fg = "white")
operatiuni_text.place(x = 350, y = 5)
operatiuni_entry = tk.Text(screen)
operatiuni_entry.place(x = 350, y = 25, width = "300", height = "500")

iesire_data = tk.Label(text="Data iesire service:", bg = "grey", fg = "white")
iesire_data.place(x = 5, y = 230)
iesire_get = StringVar()
iesire_entry = tk.Entry(screen, textvariable=iesire_get)
iesire_entry.place(x = 150, y = 230)

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

def get_input():
        json_name = select_file()
        cause = cauza_entry.get("1.0", END)
        for line in cause.split("\n"):
                if not line.strip():
                        continue

                cauza_defectiune.append(line.lstrip())
        print(cauza_defectiune)

        for x in ok:
                ok_f.append(x.get())
        print(ok_f)

        operatiuni = operatiuni_entry.get("1.0", END)
        for line in operatiuni.split("\n"):
                if not line.strip():
                        continue

                operatiuni_list.append(line.lstrip())
        print(operatiuni_list)

        # add to json

        json_data = {
             "cauza_defectiune_service": cauza_defectiune,
             "stare_iesire_service": ok_f,
             "operatiuni_iesire_service": operatiuni_list,
             "data_iesire_service": iesire_get.get()
       }

        with open(f"{json_name}", "r") as ex:
                ex_data = json.load(ex)
        json_data.update(ex_data)

        with open(f"{json_name}", "w") as f:
                json.dump(json_data, f, indent=1)

        with open(f"{json_name}", "r") as ex:
                ex_data = json.load(ex)
                nume_lucrator = ex_data["nume_lucrator"]
                rma = ex_data["RMA"]
                data = ex_data["data"]
                seria = ex_data["seria"]
                echipament = ex_data["echipament"]
                client = ex_data["client"]
                garantie = ex_data["garantie"]
                nume_electric = [x for x in ex_data["nume_electric"]]
                ok_electric = [x for x in ex_data["ok_electric"]]
                obs_electric = [x for x in ex_data["obs_electric"]]
                cauza = [x for x in ex_data["cauza_defectiune_service"]]
                stare = [x for x in ex_data["stare_iesire_service"]]
                operatiuni_efectuate = [x for x in ex_data["operatiuni_iesire_service"]]
                data_iesire = ex_data["data_iesire_service"]

        
        tm = pdf(nume_lucrator, rma, client, seria, echipament, data, nume_electric, ok_electric, obs_electric, garantie)
        tm.add_page()
        tm.fisa_service(cauza, stare, operatiuni_efectuate, data_iesire)
        try:
            tm.output(f"pdf_facute\{seria}_{client}\{data}_Fisa_Service.pdf")
        except FileNotFoundError:
            tm.output(f"pdf_facute\{data}_{client}_Fisa_Service.pdf")


submit = tk.Button(text = "MAKE PDF", width="30", height="2", bg ="blue", command=get_input)
submit.place(x = 5, y = 550)




screen.mainloop()