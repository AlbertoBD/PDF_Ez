from fpdf import FPDF
import json

class Template(FPDF):
    def __init__(self, nume_lucrator, rma, ipj, seria, echipament, date, nume_electric, ok_electric, obs_electric, garantie):
        super().__init__("P", "mm", "A4")
        self.nume_lucrator = nume_lucrator
        self.rma = rma
        self.ipj = ipj
        self.seria = seria
        self.echipament = echipament
        self.date = date
        self.nume_electric = nume_electric
        self.ok_electric = ok_electric
        self.obs_electric = obs_electric
        self.garantie = garantie


    def constatare_layout(self, componente, ok_nok, observatii, alte_constatari, alte_ok, alte_obs):

        # PDF
        self.image("images\header.png", 10, 3, 190)
        self.image("images\logo_bg.png", 10, 80, 190, 190)
        

        # TITLUL SI SUBTITLUL
        self.ln(20)
        self.set_font("times", "U", 16)
        self.cell(0, 10, "NOTA DE CONSTATARE",ln=1, align="C")
        self.set_font("times", "", 12)
        self.multi_cell(0, 5, f"           Constatarea a fost efectuata de {self.nume_lucrator}, persoana autorizata de LASER TECHNOLOGY INC, pentru a efectua operatiuni de service si de mentenanta asupra echipamentelor tip LTI 20/20 TruCAM si TRUCAM II.")
        self.ln(1)

        # Tabel informatii client
        self.set_font("times", "U", 12)
        self.set_y(55)
        self.cell(0, 10, f"RMA: {self.rma}")
        self.ln(6)
        self.set_y(61)
        self.cell(0, 10, f"ECHIPAMENT: {self.echipament}")
        self.ln(6)
        self.set_y(67)
        self.cell(0, 10, f"CLIENT: {self.ipj}")
        self.set_y(55)
        self.set_x(130)
        self.cell(0, 10, f"DATA: {self.date}")
        self.ln(6)
        self.set_y(61)
        self.set_x(130)
        self.cell(0, 10, f"SERIA: {self.seria}")
        self.ln(6)
        self.set_y(67)
        self.set_x(130)
        self.cell(0, 10, f"GARANTIE: {self.garantie}")
        self.ln(15)


        # NUME COMPONENTE TABEL
        self.set_font("times", "", 14)
        self.cell(0, 5, "                       PARTE                                      OK     NOK                          OBS")
        self.ln(7)

        initial_pos = 90

        # DRAW FIRST HORIZONTAL LINES
        self.line(10, 81, 200, 81)
        self.line(10, 89, 200, 89)

        self.set_font("times", "", 10)
        self.set_auto_page_break(0)
        
        new_page = False
        skiped_elements = ["Aliniere camera foto/video cu luneta", "Calibrare", "Verificare metrologica", "Verificare functionare si aliniere"]

        for names, oks, obs in zip(componente, ok_nok, observatii):
            # second page create
            print(initial_pos)
            if names in skiped_elements:
                continue

            if initial_pos > 275:
                self.line(10, initial_pos, 200, initial_pos)
                # VERTICAL LINES
                self.line(10, 81, 10, initial_pos)
                self.line(15,  81, 15, initial_pos)
                self.line(100, 81, 100, initial_pos)
                self.line(113, 81, 113, initial_pos)
                self.line(128, 81, 128, initial_pos)
                self.line(200, 81, 200, initial_pos)
                new_page = True
                initial_pos = 35
                self.add_page()
                self.line(10, 34, 200, 34)    # prima linie a doua pagina
                self.image("images\header.png", 10, 3, 190)
                self.image("images\logo_bg.png", 10, 80, 190, 190)
            else:
                initial_pos += 1

            # NUME PIESA
            self.set_y(initial_pos)
            self.set_x(15)
            self.multi_cell(75, 4, names, align="L")
            self.ln(1)


            # CASUTA X pentru ok / nok
            if oks == "OK":
                self.set_y(initial_pos)
                self.set_x(13)
                self.multi_cell(0, 4, "X", align="C")
                self.ln(1)
                
            elif oks == "NOK":
                self.set_y(initial_pos)
                self.set_x(40)
                self.multi_cell(0, 4, "X", align="C")
                self.ln(1)
              
             # OBSERVATII    
            self.set_y(initial_pos)
            self.set_x(130)
            self.multi_cell(0, 4, obs, align="L")
            self.ln(1)

            if len(names) > 55:
                initial_pos += 10
                self.line(15, initial_pos, 200, initial_pos)
            else:
                initial_pos += 5
                self.line(15, initial_pos, 200, initial_pos)

            # linii a doua pagina in caz ca s 3 pagini
            if new_page and initial_pos < 90:
                self.line(10, 34, 10, initial_pos)
                self.line(15, 34, 15, initial_pos)
                self.line(100, 34, 100, initial_pos)
                self.line(113, 34, 113, initial_pos)
                self.line(128, 34, 128, initial_pos)
                self.line(200, 34, 200, initial_pos)


            
        # DRAW LAST VERTICAL LINE FOR INSPECTIA VIZUALA
        self.line(10, initial_pos, 200, initial_pos)

        # CONTROL ELECTRIC
        for names, ok, obs in zip(self.nume_electric, self.ok_electric, self.obs_electric):
            if initial_pos > 227 and not new_page:
                self.line(10, initial_pos, 200, initial_pos)

                # VERTICAL LINES
                self.line(10, 81, 10, initial_pos)
                self.line(15,  81, 15, initial_pos)
                self.line(100, 81, 100, initial_pos)
                self.line(113, 81, 113, initial_pos)
                self.line(128, 81, 128, initial_pos)
                self.line(200, 81, 200, initial_pos)
                new_page = True
                initial_pos = 35
                self.add_page()
                self.line(10, 34, 200, 34)    # prima linie a doua pagina
                self.image("images\header.png", 10, 3, 190)
                self.image("images\logo_bg.png", 10, 80, 190, 190)

            self.set_y(initial_pos + 1)
            self.set_x(15)
            self.cell(75, 4, names, align="L")
            self.set_x(10)

            #ok ok_electric
            if ok == "OK":
                self.set_y(initial_pos + 1)
                self.set_x(13)
                self.cell(0, 4, "X", align="C")
                
            elif ok == "NOK":
                self.set_y(initial_pos + 1)
                self.set_x(40)
                self.cell(0, 4, "X", align="C")

            self.set_y(initial_pos)
            self.set_x(130)
            self.cell(0, 4, obs, align="L")
            self.ln(1)

            if len(names) > 65:
                initial_pos += 10
                self.line(15, initial_pos, 200, initial_pos)
            else:
                initial_pos += 5
                self.line(15, initial_pos, 200, initial_pos)

        # SCRIS VERTICAL ELECTRIC
        self.image("images\electric.png", 10, initial_pos - 25, 4, 22)
        
        # alte constatari, stare echipament
        self.line(10, initial_pos, 200, initial_pos)
        for names, ok, obs in zip(alte_constatari, alte_ok, alte_obs):
            self.set_font("times", "B", 13)
            self.set_y(initial_pos + 1)
            self.set_x(15)
            self.cell(75, 4, names, align="L")
            self.set_x(10)

            #ok ok_electric
            self.set_font("times", "", 12)
            if ok == "OK":
                self.set_y(initial_pos + 1)
                self.set_x(13)
                self.cell(0, 4, "X", align="C")
                
            elif ok == "NOK":
                self.set_y(initial_pos + 1)
                self.set_x(40)
                self.cell(0, 4, "X", align="C")

            self.set_y(initial_pos)
            self.set_x(130)
            self.cell(0, 4, obs, align="L")
            self.ln(1)

            self.line(15, initial_pos, 200, initial_pos)
            initial_pos += 5


        # last horizontal line
        self.line(10, initial_pos, 200, initial_pos)

        # DRAW HORIZONTAL LINES
        self.line(10, initial_pos, 200, initial_pos)

        # VERTICAL LINES prima pagina
        self.line(10, 81, 10, initial_pos)
        self.line(15,  81, 15, initial_pos)
        self.line(100, 81, 100, initial_pos)
        self.line(113, 81, 113, initial_pos)
        self.line(128, 81, 128, initial_pos)
        self.line(200, 81, 200, initial_pos)

        # VERTICALE pentru a doua pagina
        if new_page:
            self.line(10, 34, 10, initial_pos)
            self.line(15, 34, 15, initial_pos)
            self.line(100, 34, 100, initial_pos)
            self.line(113, 34, 113, initial_pos)
            self.line(128, 34, 128, initial_pos)
            self.line(200, 34, 200, initial_pos)
            

    def footer(self):
        self.set_font("times", "", 15)
        self.set_y(-15)
        self.image("images\semnatura.png", 100, 280, 40, 15)
        self.cell(0, 15, "Semnatura:________________", align="C")


    def calculator(self, componente, cantitate):
        final_price = []
        product_price = [x for x in componente]
        qnt = [int(x) for x in cantitate]
        
        for x, y in zip(product_price, qnt):
            final_price.append(x * y)

        return final_price

    def fisa_service(self, cauze_defect, stare_iesire, operatiuni, data_iesire):

        with open(f"Json\{self.seria}_{self.ipj}.json", "r") as ex:
            ex_data = json.load(ex)
            nume_piesa = [x for x in ex_data["Piese_NOK"]]
            observatii = [x for x in ex_data["Observatii_NOK"]]
            cost_manopera = ex_data["cost_manopera"]
            cost_componente = ex_data["cost_componente"]
            total_ore = ex_data["total_ore"]

        # creare pdf
        self.image("images\header.png", 10, 3, 190)
        self.image("images\logo_bg.png", 10, 80, 190, 190)
        self.ln(20)
        self.set_font("times", "U", 16)
        self.cell(0, 10, "FISA DE SERVICE",ln=1, align="C")
        self.ln(10)

        # introducere 
        self.set_font("times", "", 13)
        self.multi_cell(0, 5, f"         Prezenta fisa s-a incheiat cu scopul de a certifica interventia de service asupra echipamentului cinemometru {self.echipament}, seria {self.seria}, apartinand: {self.ipj}", align="L")
        self.ln(7)

        self.cell(0, 10, f"Data intrarii/iesirii in service: {self.date} -- {data_iesire}")
        self.set_x(148)
        self.cell(0, 10, f"In perioada de garantie: {self.garantie}")
        self.ln(5)

        # afisare piese si observatii
        initial_pos = 80
        self.line(10, initial_pos - 2, 200, initial_pos - 2)

        self.set_auto_page_break(0)

        # DEFECT CONSTATAT
        self.set_font("times", "B", 13)
        self.set_y(90)
        self.set_x(15)
        self.cell(0, 5, "Defect constatat:")

        self.set_font("times", "", 13)
        
        for names, obs in zip(nume_piesa, observatii):
            if initial_pos > 275:
                self.add_page()
                initial_pos = 35
                self.image("images\header.png", 10, 3, 190)
                self.image("images\logo_bg.png", 10, 80, 190, 190)
                
            self.set_y(initial_pos)
            self.set_x(70)

            self.multi_cell(0, 5, f"{names} - {obs}")

            if len(names + obs) > 64:
                initial_pos += 12
            else:
                initial_pos += 6

        print(initial_pos)

        # linie despartitoare si verticale
        self.line(10, initial_pos, 200, initial_pos)
        self.line(10, 78, 10, initial_pos)
        self.line(70,  78, 70, initial_pos)
        self.line(200, 78, 200, initial_pos)

        self.set_font("times", "B", 12)
        self.set_y(initial_pos)
        self.set_x(15)
        self.cell(0, 5, "Cauze posibile defect:")


        self.set_font("times", "", 12)
        for cauze in cauze_defect:
            self.set_y(initial_pos)
            self.set_x(70)
            self.multi_cell(0, 5, f"{cauze}")

            initial_pos += 6
        print(initial_pos)


        self.line(10, initial_pos, 200, initial_pos)
        self.line(10, 78, 10, initial_pos)
        self.line(70,  78, 70, initial_pos)
        self.line(200, 78, 200, initial_pos)

        # FINAL TABEL SI LINII
        # STARE IESIRE

        pos_stare = initial_pos + 8
        self.set_y(initial_pos)
        self.ln(3)
        self.set_font("times", "B", 12)
        self.cell(0, 5, "STARE LA IESIRE DIN SERVICE", align="C")
        self.ln(6)

        self.set_font("times", "", 12)
        self.cell(0, 5, f"PRODUS REPARAT:   {stare_iesire[0]}")
        self.set_x(110)
        self.cell(0, 5, f"GARANTIE REPARATII 1 AN:                   {stare_iesire[1]}")

        self.ln(5)
        self.set_x(10)
        self.cell(0, 5, f"SE POATE REPARA:   {stare_iesire[2]}")
        self.set_x(110)
        self.cell(0, 5, f"TREBUIE TRIMIS LA PRODUCATOR:     {stare_iesire[3]}")

        # lini stare
        self.line(10, pos_stare, 200, pos_stare)
        self.line(10, pos_stare + 6, 200, pos_stare + 6)
        self.line(10, pos_stare + 11, 200, pos_stare + 11)

        # verticale stare
        self.line(10, pos_stare, 10, pos_stare + 11)
        self.line(100, pos_stare, 100, pos_stare + 11)
        self.line(200, pos_stare, 200, pos_stare + 11)


        # FINAL STARE
        # COSTURI

        self.ln(6)
        self.set_x(60)
        self.set_font("times", "B", 12)
        self.cell(0, 5, "COSTURI REPARATIE")
        self.set_font("times", "", 12)
        self.set_x(110)
        self.cell(0, 5, "(componenteurile nu includ TVA)")
        self.ln(6)

        self.cell(0, 5, f"Manopera 60 Euro/ora X {total_ore} ore = {cost_manopera} Euro")
        self.set_x(110)
        self.cell(0, 5, f"Componente/module inlocuite = {cost_componente} Euro")

        # linii costuri  
        self.line(10, pos_stare + 17, 200, pos_stare + 17)
        self.line(10, pos_stare + 23, 200, pos_stare + 23)

        # verticale costurile
        self.line(10, pos_stare + 17, 10, pos_stare + 23)
        self.line(100, pos_stare + 17, 100, pos_stare + 23)
        self.line(200, pos_stare + 17, 200, pos_stare + 23)


        # FINAL COSTURI
        # OPERATIUNI EFECTUATE

        self.ln(6)
        self.set_x(45)
        self.set_font("times", "B", 12)
        self.cell(0, 5, "OPERATIUNI EFECTUATE")
        self.set_font("times", "", 12)
        self.set_x(100)
        self.cell(0, 5, "(inclusiv componente/module înlocuite)")
        self.ln(6)

        operatiuni_pos = pos_stare + 30
        self.line(10, operatiuni_pos, 200, operatiuni_pos)

        self.set_auto_page_break(0)
        new_page = False

        for opr in range(len(operatiuni)):
            if operatiuni_pos > 273:
                operatiuni_pos = 35
                self.add_page()
                new_page = True
            else:
                pass

            self.set_y(operatiuni_pos)
            if opr % 1 == 1:
                self.set_x(10)
            elif opr % 2 == 1:
                self.set_x(101)
                operatiuni_pos += 6

            self.cell(0, 5, operatiuni[opr])

            if not new_page:
                if len(operatiuni) % 2 == 1:
                    if operatiuni_pos < 274:
                        # linii verticale
                        self.line(10, operatiuni_pos, 10, operatiuni_pos + 6)
                        self.line(100, operatiuni_pos, 100, operatiuni_pos + 6)
                        self.line(200, operatiuni_pos, 200, operatiuni_pos + 6)
                        
                        self.line(10, operatiuni_pos + 6, 200, operatiuni_pos + 6)

                        for x in range(pos_stare + 30, operatiuni_pos, 6):
                            self.line(10, x, 200, x)

                else:
                    for x in range(pos_stare + 30, operatiuni_pos + 6, 6):
                        self.line(10, x, 200, x)
                    self.line(10, pos_stare + 30, 10, operatiuni_pos)
                    self.line(100, pos_stare + 30, 100, operatiuni_pos)
                    self.line(200, pos_stare + 30, 200, operatiuni_pos)

                
        if new_page:
            self.line(10, 35, 200, 35)
            self.image("images\header.png", 10, 3, 190)
            self.image("images\logo_bg.png", 10, 80, 190, 190)

            self.line(10, 35, 10, operatiuni_pos)
            self.line(100, 35, 100, operatiuni_pos)
            self.line(200, 35, 200, operatiuni_pos)

            if len(operatiuni) % 2 == 1:
                self.line(10, operatiuni_pos, 10, operatiuni_pos + 6)
                self.line(100, operatiuni_pos, 100, operatiuni_pos + 6)
                self.line(200, operatiuni_pos, 200, operatiuni_pos + 6)
                
                # ultima linie 
                self.line(10, operatiuni_pos + 6, 200, operatiuni_pos + 6)

                #for x in range(35, operatiuni_pos, 6):
                    #self.line(10, x, 200, x)
            
            for x in range(35, operatiuni_pos + 6, 6):
                    self.line(10, x, 200, x)


        if not new_page and operatiuni_pos > 251:
            self.add_page()
            self.image("images\header.png", 10, 3, 190)
            self.image("images\logo_bg.png", 10, 80, 190, 190)
            self.ln(20)
            self.multi_cell(0, 5, f"         Interventia a fost efectuata de catre {self.nume_lucrator}, persoana autorizata si certificata de Laser Technology INC, pentru a efectua operatiuni de service si mentenanta asupra echipamentelor tip LTI 20/20 TruCAM si Trucam II.")
            self.ln(1)
            self.multi_cell(0, 5, f"         In urma reparatiilor, echipamentul este perfect functional si in parametrii. Echipamentul este in conformitate  cu specificatiile producatorului.")
        else:
            self.ln(7)
            self.multi_cell(0, 5, f"         Interventia a fost efectuata de catre {self.nume_lucrator}, persoana autorizata si certificata de Laser Technology INC, pentru a efectua operatiuni de service si mentenanta asupra echipamentelor tip LTI 20/20 TruCAM si Trucam II.")
            self.ln(1)
            self.multi_cell(0, 5, f"         In urma reparatiilor, echipamentul este perfect functional si in parametrii. Echipamentul este in conformitate  cu specificatiile producatorului.")



class Deviz(FPDF):
    def __init__(self, nume_lucrator, rma, ipj, seria, echipament, date, nume_electric, ok_electric, obs_electric, garantie):
        super().__init__("P", "mm", "A4")
        self.nume_lucrator = nume_lucrator
        self.rma = rma
        self.ipj = ipj
        self.seria = seria
        self.echipament = echipament
        self.date = date
        self.nume_electric = nume_electric
        self.ok_electric = ok_electric
        self.obs_electric = obs_electric
        self.garantie = garantie

    def calculator(self, componente, cantitate):
        final_price = []
        product_price = [x for x in componente]
        qnt = [int(x) for x in cantitate]
        
        for x, y in zip(product_price, qnt):
            final_price.append(x * y)

        return final_price
        

    def deviz_layout(self, ok_nok, names, prices, quantity, stok_cmd, ore, descriere_defectiune, observatii):
        componente_manopera_ora = 60
        # counting indexes of nok products
        indexes_nok = []
        count = 0
        for x in ok_nok:
            if x == "NOK":
                indexes_nok.append(count)
            count += 1

        # getting only nok products
        nok_names = []
        nok_prices = []
        nok_quantity = []
        nok_stoc = []
        nok_ore = []
        nok_observatii = []
        for y in indexes_nok:
            nok_names.append(names[y])
            nok_prices.append(prices[y])
            nok_quantity.append(quantity[y])
            nok_stoc.append(stok_cmd[y])
            nok_ore.append(ore[y])
            nok_observatii.append(observatii[y])

        print(indexes_nok)

        # componente final cantitate x componente piesa
        final_price = self.calculator(nok_prices, nok_quantity)
    
        print(nok_prices)
        print(nok_quantity)
        print(final_price)

        # manopera ore
        total_ore = 0
        for y in nok_ore:
            total_ore += y
        
        total_componente_manopera = componente_manopera_ora * total_ore

        # componente piese comanda si stoc
        stoc = []
        comanda = []
        for each in zip(nok_names, nok_stoc, nok_prices):
            if each[1] == "Stoc":
                stoc.append(each[2])
            elif each[1] == "Comanda":
                comanda.append(each[2])
        
        total_stoc = 0
        total_comanda = 0

        for tp in zip(final_price, nok_stoc):
            if tp[1] == "Stoc":
                total_stoc += tp[0]
            elif tp[1] == "Comanda":
                total_comanda += tp[0]

        

        total_cost_proiect = total_componente_manopera + total_stoc + total_comanda


        # CREARE PDF
        self.image("images\header.png", 10, 3, 190)
        self.image("images\logo_bg.png", 10, 80, 190, 190)
        self.ln(20)
        self.set_font("times", "U", 16)
        self.cell(0, 10, "DEVIZ SERVICE",ln=1, align="C")
        self.ln(10)
        self.set_font("times", "", 12)
        self.cell(0, 10, "Descrierea defectiunii:", align="L")
        self.ln(7)
        self.multi_cell(0, 5, f"{descriere_defectiune}", align="L")
        self.ln(20)

        # Titluri
        self.set_font("times", "", 13)
        titlu_pos_y = 80
        self.line(9, titlu_pos_y + 2, 200, titlu_pos_y + 2)
        self.set_y(titlu_pos_y + 3)
        self.set_x(30)
        self.cell(0, 10, "Piese necesare")

        self.set_font("times", "", 11)
        self.set_y(titlu_pos_y)
        self.set_x(109)
        self.cell(0, 10, "Nr.")

        self.set_x(125)
        self.cell(0, 10, "Pret per")

        self.set_x(150)
        self.cell(0, 10, "Disponi-")

        self.set_x(180)
        self.cell(0, 10, "Pret total")

        self.set_y(titlu_pos_y + 5)
        self.set_x(108)
        self.cell(0, 10, "buc")

        self.set_x(129)
        self.cell(0, 10, "buc")

        self.set_x(150)
        self.cell(0, 10, "bilitate")

        self.set_x(180)
        self.cell(0, 10, "fara TVA")

        self.set_y(titlu_pos_y + 9)
        self.set_x(127)
        self.cell(0, 10, "(euro)")
        self.set_x(182)
        self.cell(0, 10, "(euro)")


        # afisare informatii !!
        initial_pos = 93
        self.set_auto_page_break(0)
        new_page = False


        for names, cantitate, componente, disp, total in zip(nok_names, nok_quantity, nok_prices, nok_stoc, final_price):
            if initial_pos > 235:
                new_page = True
                self.add_page()
                initial_pos = 35
                if new_page:
                    self.line(9, initial_pos + 5, 200, initial_pos + 5)
                    self.image("images\header.png", 10, 3, 190)
                    self.image("images\logo_bg.png", 10, 80, 190, 190)
                    initial_pos += 6
                    self.line(9, initial_pos + 5, 200, initial_pos + 5)
                new_page = False
            else:
                initial_pos += 6
                self.line(9, initial_pos + 5, 200, initial_pos + 5)
                
            #nume piese
            self.set_y(initial_pos)
            self.set_x(10)
            self.cell(0, 4, names, align="L")

            #cantitate
            self.set_y(initial_pos)
            self.set_x(110)
            self.cell(0, 4, cantitate)

            #componente
            self.set_y(initial_pos)
            self.set_x(130)
            self.cell(0, 4, f"{str(componente)}")

            #disponbilitate
            self.set_y(initial_pos)
            self.set_x(150)
            self.cell(0, 4, disp)

            #total componente
            self.set_y(initial_pos)
            self.set_x(185)
            self.cell(0, 4, f"{str(total)}")
            
        print(initial_pos)
             # draw last horizontal line

    
        self.ln(10)
        self.set_font("times", "B", 11)
        self.cell(0, 10, "MANOPERA/ora(fara TVA)")
        self.set_x(108)
        self.cell(0, 10, str(componente_manopera_ora) + " eur" + "    x")
        self.set_x(128)
        self.cell(0, 10, str(total_ore) + " ore" + "                  =")
        self.cell(0, 10, f"{int(total_componente_manopera)} eur", align="R")

        self.ln(5)
        self.cell(0, 10, "TOTAL COSTURI piese din STOC")
        self.cell(0, 10, f"{total_stoc} eur", align="R")

        self.ln(5)
        self.cell(0, 10, "TOTAL COSTURI piese la COMANDA")
        self.cell(0, 10, f"{total_comanda} eur", align="R")

        self.ln(5)
        self.cell(0, 10, "TOTAL COSTURI PROIECT (fara TVA)")
        self.cell(0, 10, f"{int(total_cost_proiect)} eur", align="R")
        

        # incadrare PDF pe pagina urmatoare (final de pdf


        # final de PDF
        if initial_pos > 208 and not new_page:
            self.add_page()
            self.image("images\header.png", 10, 3, 190)
            self.image("images\logo_bg.png", 10, 80, 190, 190)
            self.ln(10)

        self.ln(13)
        self.set_font("times", "", 11)
        self.cell(0, 5, "Costul final va fi calculat in lei la cursul BNR de la data plasarii comenzii ferme la care se va adauga TVA.")
        self.ln(5)
        self.cell(0, 5, "Termenul de plata este de 30 de zile.")
        self.ln(5)
        self.multi_cell(0, 5, "Acest document este o estimare. In urma discutiilor cu beneficiarul, unele repere pot fi omise iar altele adaugate. Varianta finala va fi agreata cu beneficiarul.")
        self.ln(5)
        self.multi_cell(0, 5, "Pentru a putea demara lucrarile de reparatie, clientul are obligatia de a aproba varianta finala prin semnatura. Aceasta aprobare tine loc de comanda ferma de reparatie.")
        self.ln(5)
        self.multi_cell(0, 5, "In cazul in care se constata si alte probleme, clientul va fi instiintat daca este nevoie de mai mult timp, manopera suplimentara, piesele de schimb si costurile de expediere care ar putea fi descoperite in timpul unei reparatii convenite sau pentru lucrari suplimentare la LTI Irlanda si/sau SCS Polonia.", ln=0)

        # save pdf
        json_data = {
            "Piese_NOK": nok_names,
            "Observatii_NOK": nok_observatii,
            "cost_manopera": int(total_componente_manopera),
            "total_ore": total_ore,
            "cost_componente": total_comanda + total_stoc
        }

        with open(f"Json\{self.seria}_{self.ipj}.json", "r") as ex:
            ex_data = json.load(ex)
        json_data.update(ex_data)

        with open(f"Json\{self.seria}_{self.ipj}.json", "w") as f:
            json.dump(json_data, f, indent=1)

        
    def footer(self):
        self.set_font("times", "", 15)
        self.set_y(-15)
        self.image("images\semnatura_sandu.png", 100, 280, 40, 15)
        self.cell(0, 15, "Semnatura:________________", align="C")
        self.set_font("times", "", 10)
        self.set_x(35)
        self.cell(0, 5, "Cu deosebita stima,", align="L")
        self.set_y(-10)
        self.set_x(40)
        self.cell(0, 5, "Sandu Buglea", align="L")