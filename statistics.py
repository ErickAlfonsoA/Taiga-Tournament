from tkinter import ttk
import duels2 as d2
import duels3 as d3
import options as o

def statistics(tk, mF, cHack, cBlack, players, rond, lim):
    # Funciones
    def on_enter(text):
        helpp.config(text=text)

    def on_leave(text):
        helpp.config(text=text)

    def continueTorn():
        for widget in mF.winfo_children():
            widget.destroy()
        
        if rond == 0:
            o.options(tk, mF, cHack, cBlack, players)
        else:
            if lim == 0:
                d2.duels2(tk, mF, cHack, cBlack, players, rond)
            else:
                d3.duels3(tk, mF, cHack, cBlack, players, rond)

        

    # Instancias
    tree = ttk.Treeview(mF)
    scrollTable = tk.Scrollbar(mF, command=tree.yview)

    tree.tag_configure("back", font=("Consolas", 12))

    sigButton = tk.Button(mF, text="Siguiente", font=("Consolas", 12), activebackground='red', activeforeground='white')

    helpp = tk.Label(mF, font=('Consolas', 12), text="Resultados", bg=cBlack, fg=cHack, height=2)

    # Configuraciones
    tree["columns"] = ("col1", "col2", "col3", "col4")

    scrollTable.grid(sticky="NSW") #lo estira verticalmente y lo coloca en el medio de la fila
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

    tree.grid(columnspan=3, rowspan=3, column=0, row=0)

    helpp.grid(columnspan=3, column=0, row=4)

    sigButton.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
    sigButton.configure(command=continueTorn)
    sigButton.bind('<Enter>', lambda event: on_enter("Avanzar a la siguiente ventana"))
    sigButton.bind('<Leave>', lambda event: on_leave("Resultados"))
    sigButton.grid(columnspan=3, column=0, row=3)

    # Llenado de la tabla
    players = sorted(players, key=lambda z: z[1], reverse=True)
    print(players)
    print()
    for i in range(0, len(players)):
        tree.insert("", "end", tags="back", text=players[i][0], values=(players[i][1], len(players[i][2]), len(players[i][3]), len(players[i][4])))