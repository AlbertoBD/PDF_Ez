import tkinter as tk
from tkinter.constants import END, MULTIPLE
from tkinter.ttk import Combobox
from tkinter import ttk, filedialog
from tkinter.messagebox import showinfo
import pandas as pd
import json
from pdf_template import Template as pdf
import os
from tkinter import ttk


directory_path = os.getcwd()

screen = tk.Tk()
screen.title("PetreDumitruFlorin")
screen.geometry("800x800")


#add menu items
my_menu = tk.Menu(screen)
screen.config(menu=my_menu)

# gen canvas
wrapper2 = tk.Frame(screen)
wrapper2.place(x=1, y=1, width=790, height=700)

my_canvas = tk.Canvas(wrapper2)
my_canvas.pack(side="left", fill="both", expand="yes")

items_frame = tk.Frame(my_canvas)

# scroll bar
yscroll = ttk.Scrollbar(wrapper2, orient="vertical", command=my_canvas.yview)
yscroll.pack(side="right", fill="y")

my_canvas.configure(yscrollcommand=yscroll.set)
my_canvas.create_window((0,0), window=items_frame, anchor="nw")

my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# for background view of  selected item
for thing in range(300):
       tk.Label(items_frame, text="                                                                                                                                                                                                                                                            ").grid(row = thing, column = 0)


piese = []
options = ["Stare echipament:", "Alte constatari:", "Trebuie trimis la producator:"]

# afisare excel
def show_data():
       total = 0
       try:
              for x in range(0, len(piese)):
                     quantity_entry = tk.Entry(items_frame)
                     quantity_entry.place(x = 10, y = 50 + x * 57, width=30)
                     cantiate.append(quantity_entry)

                     ok_entry = Combobox(items_frame, values=["OK", "NOK"])
                     ok_entry.place(x = 100, y = 50 + x * 57)
                     ok.append(ok_entry)
                     
                     disponibilitate_entry = Combobox(items_frame, values=["Comanda", "Stoc"])
                     disponibilitate_entry.place(x = 300, y = 50 + x * 57)
                     disponibilitate.append(disponibilitate_entry)

                     obs_entry = tk.Entry(items_frame)
                     obs_entry.place(x = 500, y = 50 + x * 57, width=240)
                     obs.append(obs_entry)
                     
              for y in piese:
                     total += 1
                     names = tk.Label(items_frame, text = y[0], bg = "grey", fg = "white", width = 100)
                     names["text"] = y[0]
                     names.place(x = 5, y = -30 + total * 57)
                     number = tk.Label(items_frame, text = total, bg = "grey", fg = "white")
                     number.place(x = 5, y = -30 + total * 57)
              
              for each in list(options):
                     total += 1
                     names = tk.Label(items_frame, text = each, bg = "grey", fg = "white", width = 100)
                     names.place(x = 5, y = -30 + total * 57)
                     number = tk.Label(items_frame, text = total, bg = "grey", fg = "white")
                     number.place(x = 5, y = -30 + total * 57)

                     ok_entry = Combobox(items_frame, values=["OK", "NOK"])
                     ok_entry.place(x = 100, y =  total * 57)
                     ok_producator.append(ok_entry)

                     obs_entry = tk.Entry(items_frame)
                     obs_entry.place(x = 500, y = total * 57, width=240)
                     obs_producator.append(obs_entry)

       except IndexError:
              pass


def file_open():
       filename = filedialog.askopenfilename(
              initialdir=f"{directory_path}/ExcelRadar",
              title = "Open A File",
              filetype=(("xlsx files", "*.xlsx"), ("All files", "*.*"))
       )

       if filename:
              try:
                     filename = r"{}".format(filename)
                     df = pd.read_excel(filename)
              except ValueError:
                     my_label.config(text="Nu a putut fi deschis!, Incearca din nou")
              except FileNotFoundError:
                     my_label.config(text="Nu a putut fi gasit! Incearca din nou")

       # adaugare fiecare row din excel in lista
       df_rows = df.to_numpy().tolist()
       for row in df_rows:
              piese.append(row)

       cantitate_label = tk.Label(screen, text = "Cantitate")
       cantitate_label.place(x = 5, y = 5)

       disponibilitate_label = tk.Label(screen, text = "Disponibilitate")
       disponibilitate_label.place(x = 340, y = 5)

       stare_label = tk.Label(screen, text = "Stare")
       stare_label.place(x = 140, y = 5)

       observatii_label = tk.Label(screen, text = "Observatii")
       observatii_label.place(x = 540, y = 5)
       show_data()
       


my_label = tk.Label(screen, text = "")
my_label.grid(row = 10, column = 10)
file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Open", menu=file_menu)
file_menu.add_command(label="Open", command=file_open)


# liste prelucrare input (f_ = final result)
cantiate = []
disponibilitate = []
ok = []
obs = []
ok_producator = []
obs_producator = []

entry_list = []
disponibilitate_list = []
ok_list = []
obs_list = []
ok_producator_list = []
obs_producator_list = []

f_entry_list = []
f_disp_list = []
f_ok_list = []
f_obs_list = []
f_ok_producator = []
f_obs_producator = []

piese = []


def clear_list():
       entry_list.clear()
       disponibilitate_list.clear()
       ok_list.clear()
       obs_list.clear()
       ok_producator_list.clear()
       obs_producator_list.clear()


def get_input():
       clear_list()
       for name in cantiate:
              entry_list.append(name.get())
       for disponibil in disponibilitate:
              disponibilitate_list.append(disponibil.get())
       for oknok in ok:
              ok_list.append(oknok.get())
       for observatii in obs:
              obs_list.append(observatii.get())
       for x in ok_producator:
              ok_producator_list.append(x.get())
       for y in obs_producator:
              obs_producator_list.append(y.get())

           
def oberv_list():
       count = 0
       zcount = 0
       final_list = []

       for x in piese:
              final_list.append(x[4])
       
       obs = obs_list[:len(piese)]

       ok = ok_list[:len(piese)]


       try:
              for y in obs:
                     if y != "":
                            final_list[count] = y
                     count += 1
              for x in ok:
                     if x == "OK":
                            final_list[zcount] = " "
                     zcount += 1
       except IndexError:
              pass

       return final_list, ok


# select json
def select_file():
    filetypes = (
        ('json files', '*.json'),
        ('All files', '*.*')
    )

    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir= f"{directory_path}\Json",
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
    return filename   


def make_pdf():
       get_input()
       json_name = select_file()
       names = []

       for a in piese:
              names.append(a[0])

       obsl, ok = oberv_list()
       

       quant = entry_list[:len(piese)]
       disp = disponibilitate_list[:len(piese)]

       # only selected with ok or nok
       indexes = []
       count = 0
       for x in ok:
            if x == "OK":
                indexes.append(count)
            elif x == "NOK":
                indexes.append(count)
            count += 1

       selected_component = []
       selected_quant = []
       selected_disp = []
       selected_ok = []
       selected_observatii = []
       for y in indexes:
            selected_component.append(piese[y])
            selected_quant.append(quant[y])
            selected_disp.append(disp[y])
            selected_ok.append(ok[y])
            selected_observatii.append(obsl[y])
       
       ed = {}
       
       json_data = {
              "product_name": [x[0] for x in selected_component],
              "product_price": [x[1] for x in selected_component],
              "product_manopera": [x[2] for x in selected_component],
              "cantitate": selected_quant,
              "disponibilitate": selected_disp,
              "ok/nok": selected_ok,
              "observatii": selected_observatii,
              "alte_constatari": options,
              "alte_ok": ok_producator_list,
              "alte_obs": obs_producator_list

       }

       with open(f"{json_name}", "r") as ex:
              ex_data = json.load(ex)
              json_data["nume_lucrator"] = ex_data["nume_lucrator"]
              json_data["RMA"] = ex_data["RMA"]
              json_data["data"] = ex_data["data"]
              json_data["seria"] = ex_data["seria"]
              json_data["echipament"] = ex_data["echipament"]
              json_data["client"] = ex_data["client"]
              json_data["garantie"] = ex_data["garantie"]
              json_data["nume_electric"] = [x for x in ex_data["nume_electric"]]
              json_data["ok_electric"] = [x for x in ex_data["ok_electric"]]
              json_data["obs_electric"] = [x for x in ex_data["obs_electric"]]



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
              ok_n = [x for x in ex_data["ok/nok"]]
              observatii = [x for x in ex_data["observatii"]]
              nume_electric = [x for x in ex_data["nume_electric"]]
              ok_electric = [x for x in ex_data["ok_electric"]]
              obs_electric = [x for x in ex_data["obs_electric"]]
              alte_constatari = [x for x in ex_data["alte_constatari"]]
              alte_ok = [x for x in ex_data["alte_ok"]]
              alte_obs = [x for x in ex_data["alte_obs"]]

       tm = pdf(nume_lucrator, rma, client, seria, echipament, data, nume_electric, ok_electric, obs_electric, garantie)
       tm.add_page()
       tm.constatare_layout(componenete, ok_n, observatii, alte_constatari, alte_ok, alte_obs)

       try:
              directory = f"{seria}_{client}"
              parent_dir = f"{directory_path}\pdf_facute"
              path = os.path.join(parent_dir, directory)
              os.mkdir(path)
       except FileExistsError:
              directory = f"{seria}_{client}(Copy)"
              parent_dir = f"{directory_path}\pdf_facute"
              path = os.path.join(parent_dir, directory)
              os.mkdir(path)
       


       tm.output(f"pdf_facute\{directory}\{data}_Constatare_Service.pdf")
       print("DONE")


def go_back():
       screen.destroy()
       import homepage


make_pdfs = tk.Button(text = "Make PDF", width="30", height="2", command=make_pdf)
make_pdfs.place(x = 380, y = 750)

back = tk.Button(text = "BACK", width="30", height="2", command=go_back)
back.place(x = 180, y = 750)


#CONTROL ELECTRIC
def go_deviz():
       screen.destroy()
       import deviz

      
       
buttonExample = tk.Button(screen, 
              text="DEVIZ",
              command=go_deviz)
buttonExample.place(x = 50, y = 750, width="100", height="40")

screen.mainloop()