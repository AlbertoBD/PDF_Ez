from pdf_template import Deviz as pdf
import json
import tkinter as tk
from tkinter import filedialog
from tkinter.constants import END
import os


directory_path = os.getcwd()

screen = tk.Tk()
screen.geometry("800x600")
screen.title("Deviz Service")


# descriere defectiune piesa
deviz_text = tk.Label(text="DESCRIERE DEFECTIUNE: ", bg = "grey", fg = "white")
deviz_text.place(x = 5, y = 5)
deviz_entry = tk.Text(screen)
deviz_entry.place(x = 5, y = 25, width = "300", height = "100")


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


def make_pdf():
    descriere_deviz = deviz_entry.get(1.0, END)
    json_name = select_file()

    json_data = {
             "descriere_defectiune_deviz": descriere_deviz
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
        componenete = [x for x in ex_data["product_name"]]
        pret = [x for x in ex_data["product_price"]]
        ok_n = [x for x in ex_data["ok/nok"]]
        cantitate = [x for x in ex_data["cantitate"]]
        disponibilitate = [x for x in ex_data["disponibilitate"]]
        nume_electric = [x for x in ex_data["nume_electric"]]
        ok_electric = [x for x in ex_data["ok_electric"]]
        obs_electric = [x for x in ex_data["obs_electric"]]
        ore = [x for x in ex_data["product_manopera"]]
        descriere = ex_data["descriere_defectiune_deviz"]
        observatii = [x for x in ex_data["observatii"]]

        tm = pdf(nume_lucrator, rma, client, seria, echipament, data, nume_electric, ok_electric, obs_electric, garantie)
        tm.add_page()
        tm.deviz_layout(ok_n, componenete, pret, cantitate, disponibilitate, ore, descriere, observatii)
        
        try:
            tm.output(f"pdf_facute\{seria}_{client}\{data}_Deviz_Service.pdf")
        except FileNotFoundError:
            tm.output(f"pdf_facute\{data}_{client}_Deviz_Service.pdf")


def go_fisa():
    screen.destroy()
    import fisa_service

submit = tk.Button(text = "MAKE PDF", width="30", height="2", bg ="blue", command=make_pdf)
submit.place(x = 5, y = 550)

submit = tk.Button(text = "FISA SERVICE", width="30", height="2", bg ="blue", command=go_fisa)
submit.place(x = 350, y = 550)

screen.mainloop()