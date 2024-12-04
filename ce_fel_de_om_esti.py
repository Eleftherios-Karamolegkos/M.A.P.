from tkinter import *
from tkinter import messagebox

afisaj = Tk()
afisaj.geometry("350x350")
afisaj.title ("Salut")
Label(afisaj,text="Nume").grid(row=0)
Label(afisaj,text="Prenume").grid(row=1)
nume = Entry(afisaj)
prenume = Entry(afisaj)
nume.grid(row=0, column=1)
prenume.grid(row=1, column=1)

def afisaza_numele():
    nume_afisat = nume.get()
    prenume_afisat = prenume.get()
    messagebox.showerror("Numele", f"Salut, {nume_afisat} {prenume_afisat}!")

Button(afisaj,text="Salut", command=afisaza_numele).grid(row=2)

mainloop()