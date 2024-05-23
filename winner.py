import tkinter as tkk
import random

def winner(tk, mF, cHack, cBlack, players):
    # Funciones
    def on_enter(text):
        helpp.config(text=text)

    def on_leave(text):
        helpp.config(text=text)

    def determinate(label, win):
        if len(players) > 1:
            if players[0][1] == players[1][1]:
                label.configure(text="Los ganadores son:")
                win.configure(text=players[0][0]+" y "+players[1][0])
            else:
                label.configure(text="El ganador es:")
                win.configure(text=players[0][0])
        else:
            label.configure(text="El ganador es:")
            win.configure(text=players[0][0])
        
    def changeColor(mf, win):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Generar un color hexadecimal aleatorio
        win.config(fg=color)  # Cambiar el color del texto
        mf.after(500, lambda: changeColor(mf, win))  # Llamar a la función después de 1 segundo (1000 ms)


    # Instancias
    labelText = tk.Label(mF, font=('Consolas', 12), text="", bg=cBlack, fg=cHack)

    playerWin = tk.Label(mF, font=('Consolas', 18), text="", bg=cBlack, fg=cHack)

    helpp = tk.Label(mF, font=('Consolas', 12), text="Felicidades!!", bg=cBlack, fg=cHack, height=2)

    # Variables

    determinate(labelText, playerWin)
    changeColor(mF, playerWin)

    # Configuraciones
    helpp.grid(columnspan=3, row=4, column=0)

    labelText.grid(columnspan=3, column=0, row=1)

    playerWin.grid(columnspan=3, column=0, row=2)