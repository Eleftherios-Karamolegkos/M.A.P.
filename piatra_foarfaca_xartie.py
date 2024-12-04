from tkinter import *
from tkinter import messagebox
import random

afisaj = Tk()
afisaj.title("Piatra Hartie Foarfeca")
reguli = ("Regulile jocurile sunt: \n"
          "Piatra vs Hartia --> Hartie\n"
          "Piatra vs Foarfeca --> Piatra\n"
          "Hartie vs Foarfeca --> Foarfeca")

label_reguli = Label(afisaj, text=reguli, justify="center", fg="#5c1a15")
label_reguli.pack(side="top")
label_status_joc = Label(afisaj, text="Status joc: ", fg="#5c1a15")
label_status_joc.pack(side="bottom")
label_scor_pc = Label(afisaj, fg="red", text="Score pc: 0")
label_scor_pc.pack(side="top")
label_scor_om = Label(afisaj, fg="red", text="Score om: 0")
label_scor_om.pack(side="top")

#logiaca joc
counter_utilizator = 0
counter_calculator = 0
def joaca(alegere_utilizator):
    global label_status_joc,counter_calculator,counter_utilizator,label_scor_pc,label_scor_om
    optioni = ["Piatra", "Hartie", "Foarfeca"]
    alegere_calculator = random.choice(optioni)
    #Construim mesajul pentru afisare
    mesaj = f"Calculator a ales: {alegere_calculator}\n"

    if alegere_calculator == alegere_utilizator:
        mesaj += "Egalitate"
    elif (alegere_utilizator == "Piatra" and alegere_calculator=="Foarfeca") or \
         (alegere_utilizator == "Hartie" and alegere_calculator=="Piatra") or \
         (alegere_utilizator == "Foarfeca" and alegere_calculator=="Hartie"):
            mesaj += "Ai castigat!"
            counter_utilizator += 1
            label_scor_om.config(text=f"Scor utilizator: {counter_utilizator}")
    else:
         mesaj += "Ai pierdut"
         counter_calculator += 1
         label_scor_pc.config(text=f"Scor calculator: {counter_calculator}")

    label_status_joc.config(text=mesaj)
    if counter_utilizator == 3:
         messagebox.showinfo("Castigator", "Ai castigat jocul!")
         counter_calculator = 0
         counter_utilizator = 0
         label_scor_om.config(text=f"Scor utilizator: {counter_utilizator}")
         label_scor_pc.config(text=f"Scor calculator: {counter_calculator}")
    elif counter_calculator == 3:
         messagebox.showinfo("Castigator", "Calculatorul a castigat jocul!")
         counter_calculator = 0
         counter_utilizator = 0
         label_scor_om.config(text=f"Scor utilizator: {counter_utilizator}")
         label_scor_pc.config(text=f"Scor calculator: {counter_calculator}")
         
Button_foarfeca = Button(afisaj, text="Foarfeca", width=10, command=lambda:joaca("Piatra")).pack(side="left")
Button_hartie = Button(afisaj, text="Hartie", width=10, command=lambda:joaca("Hartie")).pack(side="left")
Button_bolovan = Button(afisaj, text="Piatra", width=10, command=lambda:joaca("Foarfeca")).pack(side="left")

mainloop()