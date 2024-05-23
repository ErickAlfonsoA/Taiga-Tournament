import tkinter as tk
import major as m
from tkinter import font
#from PIL import ImageTk, Image

#root
root = tk.Tk()

#colores y variables
cHack = '#20C20E'
cBlack = '#000000'

name = []

#Configuraciones iniciales del root #'../img/taigaR.png'
logo = tk.PhotoImage(file = '../img/taigaR.png') #'env/img/taigaR.png' esta ruta es para poder correrlo desde aqui, la que esta es para el instalador
root.iconphoto(False, logo, logo)

root.geometry('500x600+350+20')
root.minsize(480,500)
root.config(bg = cBlack)
root.title("TaigaTournament")

mF = tk.Frame(root, background=cBlack, highlightbackground=cHack, highlightcolor= cHack, highlightthickness=2)
mF.grid(column=0, row=0, sticky='nswe', padx=50, pady=50)

#configurando espacios para el responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mF.columnconfigure([0,1,2], weight=1)
mF.rowconfigure([0,1,2,3,4], weight=1)

m.major(tk, mF, cHack, cBlack, name, logo, font)

root.mainloop()