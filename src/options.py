from tkinter import ttk
import winner as w
import duels3 as d

def options(tk, mF, cHack, cBlack, players):
    # Funciones
    def on_enter(text):
        helpp.config(text=text)

    def on_leave(text):
        helpp.config(text=text)

    def winnerTorn():
        for widget in mF.winfo_children():
            widget.destroy()
        w.winner(tk, mF, cHack, cBlack, players)
    
    def bestTorn():
        for widget in mF.winfo_children():
            widget.destroy()
        d.duels3(tk, mF, cHack, cBlack, players, 2)
        

    def condi(b4):
        if len(players) > 4:
            b4.configure(state='normal')
        else:
            b4.configure(state='disabled')


    # Instancias
    win = tk.Button(mF, text="Ganador por puntos", font=("Consolas", 12), activebackground='red', activeforeground='white')

    best4 = tk.Button(mF, text="Final mejores 4", font=("Consolas", 12), activebackground='red', activeforeground='white')

    helpp = tk.Label(mF, font=('Consolas', 12), text="", bg=cBlack, fg=cHack, height=2)

    tree = ttk.Treeview(mF)
    scrollTable = tk.Scrollbar(mF, command=tree.yview)

    tree.tag_configure("back", font=("Consolas", 12))

    # Configuraciones
    tree["columns"] = ("col1", "col2", "col3", "col4")

    #scrollTable.grid(sticky="NSW") #lo estira verticalmente y lo coloca en el medio de la fila
    scrollTable.place(in_=tree, relx=1, relheight=1, bordermode="outside")

    tree["style"] = "Custom.Treeview"

    tree.heading("#0", text="Nombre")
    tree.heading("col1", text="Puntos")
    tree.heading("col2", text="Ganados")
    tree.heading("col3", text="Perdidos")
    tree.heading("col4", text="Empatados")

    tree.column("#0", width=70, minwidth=70)
    tree.column("col1", width=70, minwidth=70)
    tree.column("col2", width=70, minwidth=70)
    tree.column("col3", width=70, minwidth=70)
    tree.column("col4", width=70, minwidth=70)

    tree.grid(columnspan=3, rowspan=2, column=0, row=2)


    helpp.grid(columnspan=3, column=0, row=4)

    win.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
    win.configure(command=winnerTorn)
    win.bind('<Enter>', lambda event: on_enter("Define al ganador que haya\nobtenido mas puntos"))
    win.bind('<Leave>', lambda event: on_leave(""))
    win.grid(columnspan=3, column=0, row=0)

    best4.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
    best4.configure(command=bestTorn)
    best4.bind('<Enter>', lambda event: on_enter("Final entre los mejores 4\njugadores del torneo"))
    best4.bind('<Leave>', lambda event: on_leave(""))
    best4.grid(columnspan=3, column=0, row=1)

    #Llenado de la tabla
    condi(best4)

    for p in range(0, len(players)):
        for z in range(0, len(players[p][2])):
            priW = players[p][2][z]
            #print(priW)
            #indice = players.index(priW)

            for x in range(0, len(players)):
                if priW == players[x][0]:
                    priW = players[x]
                    #print(priW)
                    break

            #print(indice)
            for y in range(0, len(priW[2])):
                players[p][1] += .02
            for y in range(0, len(priW[4])):
                players[p][1] += .01
            
    players = sorted(players, key=lambda z: z[1], reverse=True)
    print(players)
    print()
    for i in range(0, len(players)):
        tree.insert("", "end", tags="back", text=players[i][0], values=(players[i][1], len(players[i][2]), len(players[i][3]), len(players[i][4])))