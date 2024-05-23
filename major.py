import duels as d

def major(tk, mF, cHack, cBlack, name, logo, font):
    # Funciones de los botones Principal
    def enter(event):
        addPlayer()

    def addPlayer():
        ply = player.get()
        if ply != "":
            if ply in name:
                helpp.config(text=ply+" ya se encuentra entre\nlos jugadores")
            else:
                name.append(ply)
                player.delete(0, tk.END)
                players.config(state="normal")
                players.delete("1.0", tk.END)
                for i in name:
                    players.insert("1.0", "\n")
                    players.insert("1.0", i)
                players.config(state="disabled")
        else:
            helpp.config(text="No puedes ingresar un nombre\nvacio")

    def supPlayer():
        ply = player.get()
        if ply != "":
            player.delete(0, tk.END)
            if ply in name:
                ind = name.index(ply)
                name.pop(ind)
            players.config(state="normal")
            players.delete("1.0", tk.END)
            for i in name:
                players.insert("1.0", "\n")
                players.insert("1.0", i)
            players.config(state="disabled")
        else:
            helpp.config(text="Tienes que ingresar un nombre")

    def continueTorn():
        if len(name) != 0 and len(name) != 1:
            players2 = []
            for widget in mF.winfo_children():
                widget.destroy()
            for i in name:
                players2 += [[i, 0, [], [], [], []]]

            d.duels(tk, mF, cHack, cBlack, name, players2, logo, font)
        else:
            helpp.config(text="Tiene que haber minimo 2 jugadores")

    def on_enter(text):
        helpp.config(text=text)

    def on_leave(text):
        helpp.config(text=text)

    #Objetos Principal

        #Label logo, titulo, helpp
    logoL = tk.Label(mF, image=logo, bg=cBlack).grid(columnspan=3, row=0)
    title = tk.Label(mF, font=('Consolas', 16), text="TaigaTournament", bg=cBlack, fg='#20C20E')
    helpp = tk.Label(mF, font=('Consolas', 12), text="", bg=cBlack, fg=cHack, height=2)

        #Entry jugadores
    player = tk.Entry(mF, width=15, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)

        #Cuadro de texto
    players = tk.Text(mF, width=20, height=10, state="disabled", highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)

        #Scroll del cuadro de texto
    scrollTable = tk.Scrollbar(mF, command=players.yview)
    
        #Boton añadir
    add = tk.Button(mF, text="Añadir", font=("Consolas", 12), activebackground='red', activeforeground='white')

        #Boton eliminar
    sup = tk.Button(mF, text="Eliminar", font=("Consolas", 12), activebackground='red', activeforeground='white')

        #Boton continuar
    sig = tk.Button(mF, text="Siguiente", font=("Consolas", 12), activebackground='red', activeforeground='white')

    # Si regresa para vizualizar los jugadores que ya tenia

    print(name)
    players.config(state="normal")
    players.delete("1.0", tk.END)
    for i in name:
        players.insert("1.0", "\n")
        players.insert("1.0", i)
    players.config(state="disabled")    

    #Configuraciones de los objetos Principal
    title.grid(columnspan=3, row=1, padx=4, pady=4)

    under = font.Font(title, title.cget("font"))
    under.configure(underline=True)
    title.configure(font=under)

    helpp.grid(columnspan=3, row=4, column=0)

    player.configure(background=cBlack, foreground=cHack, font=('Consolas', 12))
    player.insert(0, "Jugador")
    player.grid(columnspan=2, row=2, column=0)

    players.configure(background=cBlack, foreground=cHack, font=('Consolas', 12))
    players.grid(row=2, column=2)

    player.bind("<Return>", enter)

    add.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
    add.configure(command=addPlayer)
    add.bind('<Enter>', lambda event: on_enter("Pon un nombre y dale \nal boton para añadirlo"))
    add.bind('<Leave>', lambda event: on_leave(""))
    add.grid(row=3, column=0)

    sup.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
    sup.configure(command=supPlayer)
    sup.bind('<Enter>', lambda event: on_enter("Escribe el nombre a eliminar\ny dale al boton"))
    sup.bind('<Leave>', lambda event: on_leave(""))
    sup.grid(row=3, column=1)

    sig.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
    sig.configure(command=continueTorn)
    sig.bind('<Enter>', lambda event: on_enter("Presiona para continuar"))
    sig.bind('<Leave>', lambda event: on_leave(""))
    sig.grid(row=3, column=2)