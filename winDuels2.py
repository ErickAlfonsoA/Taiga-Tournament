import statistics as s
import winner as w

def winDuels2(tk, mF, cHack, cBlack, players, rond):
    # Funcciones
    def buttons(i, s, l1, r1, l2, r2, l3, r3):
        print(i)
        print(s)
        print(players)
        if s >= 6:
            l1.configure(text="Gano "+players[i][0], font=("Consolas", 12), activebackground='red', activeforeground='white')        
            r1.configure(text="Gano "+players[i+1][0], font=("Consolas", 12), activebackground='red', activeforeground='white')
    
            l1.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
            
            l1.configure(command=lambda: points(i,i+1,r1,row1,play))
            l1.bind('<Enter>', lambda event: on_enter("Click para darle 3 puntos a "+players[0][0]))
            l1.bind('<Leave>', lambda event: on_leave(""))
            
            l1.grid(column=0, row=0)
            r1.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
            
            r1.configure(command=lambda: points(i+1,i,l1,row1,play))
            r1.bind('<Enter>', lambda event: on_enter("Click para darle 3 puntos a "+players[1][0]))
            r1.bind('<Leave>', lambda event: on_leave(""))

            r1.grid(column=2, row=0)

            l2.configure(text="Gano "+players[i+2][0], font=("Consolas", 12), activebackground='red', activeforeground='white')        
            r2.configure(text="Gano "+players[i+3][0], font=("Consolas", 12), activebackground='red', activeforeground='white')
    
            l2.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
            
            l2.configure(command=lambda: points(i+2,i+3,r2,row2,play))
            l2.bind('<Enter>', lambda event: on_enter("Click para darle 3 puntos a "+players[2][0]))
            l2.bind('<Leave>', lambda event: on_leave(""))
            
            l2.grid(column=0, row=1)
            r2.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
            
            r2.configure(command=lambda: points(i+3,i+2,l2,row2,play))
            r2.bind('<Enter>', lambda event: on_enter("Click para darle 3 puntos a "+players[3][0]))
            r2.bind('<Leave>', lambda event: on_leave(""))
            
            r2.grid(column=2, row=1)

            l3.configure(text="Gano "+players[i+4][0], font=("Consolas", 12), activebackground='red', activeforeground='white')        
            r3.configure(text="Gano "+players[i+5][0], font=("Consolas", 12), activebackground='red', activeforeground='white')
        
            l3.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
            
            l3.configure(command=lambda: points(i+4,i+5,r3,row3,play))
            l3.bind('<Enter>', lambda event: on_enter("Click para darle 3 puntos a "+players[4][0]))
            l3.bind('<Leave>', lambda event: on_leave(""))

            l3.grid(column=0, row=2)
            r3.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
            
            r3.configure(command=lambda: points(i+5,i+4,l3,row3,play))
            r3.bind('<Enter>', lambda event: on_enter("Click para darle 3 puntos a "+players[5][0]))
            r3.bind('<Leave>', lambda event: on_leave(""))

            r3.grid(column=2, row=2)
        else:
            if s == 4:
                row3.set(True)

                l1.configure(text="Gano "+players[i][0], font=("Consolas", 12), activebackground='red', activeforeground='white')        
                r1.configure(text="Gano "+players[i+1][0], font=("Consolas", 12), activebackground='red', activeforeground='white')
        
                l1.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
                
                l1.configure(command=lambda: points(i,i+1,r1,row1,play))
                l1.bind('<Enter>', lambda event: on_enter("Click para darle 3 puntos a "+players[0][0]))
                l1.bind('<Leave>', lambda event: on_leave(""))

                l1.grid(column=0, row=0)
                r1.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
                
                r1.configure(command=lambda: points(i+1,i,l1,row1,play))
                r1.bind('<Enter>', lambda event: on_enter("Click para darle 3 puntos a "+players[1][0]))
                r1.bind('<Leave>', lambda event: on_leave(""))
                
                r1.grid(column=2, row=0)

                l2.configure(text="Gano "+players[i+2][0], font=("Consolas", 12), activebackground='red', activeforeground='white')        
                r2.configure(text="Gano "+players[i+3][0], font=("Consolas", 12), activebackground='red', activeforeground='white')
            
                l2.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
                
                l2.configure(command=lambda: points(i+2,i+3,r2,row2,play))
                l2.bind('<Enter>', lambda event: on_enter("Click para darle 3 puntos a "+players[2][0]))
                l2.bind('<Leave>', lambda event: on_leave(""))
                
                l2.grid(column=0, row=1)
                r2.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
                
                r2.configure(command=lambda: points(i+3,i+2,l2,row2,play))
                r2.bind('<Enter>', lambda event: on_enter("Click para darle 3 puntos a "+players[3][0]))
                r2.bind('<Leave>', lambda event: on_leave(""))
                
                r2.grid(column=2, row=1)

            else:
                row2.set(True)
                row3.set(True)

                l1.configure(text="Gano "+players[i][0], font=("Consolas", 12), activebackground='red', activeforeground='white')        
                r1.configure(text="Gano "+players[i+1][0], font=("Consolas", 12), activebackground='red', activeforeground='white')

                l1.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
                
                l1.configure(command=lambda: points(i,i+1,r1,row1,play))
                l1.bind('<Enter>', lambda event: on_enter("Click para darle 3 puntos a "+players[0][0]))
                l1.bind('<Leave>', lambda event: on_leave(""))
                
                l1.grid(column=0, row=0)
                r1.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
                
                r1.configure(command=lambda: points(i+1,i,l1,row1,play))
                r1.bind('<Enter>', lambda event: on_enter("Click para darle 3 puntos a "+players[1][0]))
                r1.bind('<Leave>', lambda event: on_leave(""))
                
                r1.grid(column=2, row=0)
    
    def points(p1, p2, bp2, row, p):
        row.set(not row.get())
        if row.get():
            players[p1][1] += 3
            players[p1][5].append(players[p2][0]) # REGISTRO DEL JUEGO
            players[p2][5].append(players[p1][0]) # REGISTRO DEL JUEGO
            players[p1][2].append(players[p2][0]) # REGISTRO DEL GANADOR
            players[p2][3].append(players[p1][0]) # REGISTRO PERDEDOR

            p += [players[p1]]
            print("Aqui boludo")
            print(p)

            bp2.configure(state="disabled")

            if row3.get() == True and row2.get() == True and row1.get() == True:
                sigButton.configure(state="normal")
                
            print("\n")
            print(players)
        else:
            players[p1][1] -= 3
            players[p1][5].pop() # QUITAR EL REGISTRO
            players[p2][5].pop() # QUITAR EL REGISTRO
            players[p1][2].pop() # QUITAR EL REGISTRO
            players[p2][3].pop() # QUITAR EL REGISTRO

            p.pop()

            bp2.configure(state="normal")

            sigButton.configure(state="disabled")

            print("\n")
            print(players)

    def moveOn(l1, r1, l2, r2, l3, r3, r, play):
        size.set(size.get()-6)
        cont.set(cont.get()+6)

        print(cont.get())
        print(size.get())

        if size.get() <= 0:
            for widget in mF.winfo_children():
                widget.destroy()

            r -= 1
            if r == 0:
                w.winner(tk, mF, cHack, cBlack, play)
            else:
                s.statistics(tk, mF, cHack, cBlack, play, r, 1)
        else:
            if size.get() >= 6:
                l1.configure(state="normal")
                r1.configure(state="normal")

                l2.configure(state="normal")
                r2.configure(state="normal")

                l3.configure(state="normal")
                r3.configure(state="normal")

                row1.set(False)
                row2.set(False)
                row3.set(False)

                sigButton.configure(state="disabled")

                buttons(cont.get(), size.get(), l1, r1, l2, r2, l3, r3)
            else:
                if size.get() == 4:
                    l1.configure(state="normal")
                    r1.configure(state="normal")

                    l2.configure(state="normal")
                    r2.configure(state="normal")

                    l3.destroy()
                    r3.destroy()

                    row1.set(False)
                    row2.set(False)
                    row3.set(True)

                    sigButton.configure(state="disabled")

                    buttons(cont.get(), size.get(), l1, r1, l2, r2, l3, r3)
                else:
                    l1.configure(state="normal")
                    r1.configure(state="normal")

                    l2.destroy()
                    r2.destroy()

                    l3.destroy()
                    r3.destroy()

                    row1.set(False)
                    row2.set(True)
                    row3.set(True)

                    sigButton.configure(state="disabled")

                    buttons(cont.get(), size.get(), l1, r1, l2, r2, l3, r3)

    def on_enter(text):
        helpp.config(text=text)

    def on_leave(text):
        helpp.config(text=text)

    # Variables
    size = tk.IntVar()
    size.set(0)
    cont = tk.IntVar()
    cont.set(0)

    if len(players) % 2 == 0:
        size.set(len(players))
    else:
        size.set(len(players)-1)

    row1 = tk.BooleanVar()
    row1.set(False)

    row2 = tk.BooleanVar()
    row2.set(False)

    row3 = tk.BooleanVar()
    row3.set(False)

    play = []

    # Instancias
    helpp = tk.Label(mF, font=('Consolas', 12), text="¿Quienes ganaron?", bg=cBlack, fg=cHack, height=2)
    sigButton = tk.Button(mF, text="Siguiente", font=("Consolas", 12), activebackground='red', activeforeground='white')

    playerL1 = tk.Button(mF)        
    playerR1 = tk.Button(mF)
    
    playerL2 = tk.Button(mF)        
    playerR2 = tk.Button(mF)

    playerL3 = tk.Button(mF)        
    playerR3 = tk.Button(mF)

    # Mostrar los primeros jugadores
    buttons(cont.get(), size.get(), playerL1, playerR1, playerL2, playerR2, playerL3, playerR3)

    # Configuraciones
    helpp.grid(columnspan=3, column=0, row=4)

    sigButton.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
    sigButton.configure(command=lambda: moveOn(playerL1, playerR1, playerL2, playerR2, playerL3, playerR3, rond, play))
    sigButton.configure(state="disabled")
    sigButton.bind('<Enter>', lambda event: on_enter("Avanzar a la siguiente ventana"))
    sigButton.bind('<Leave>', lambda event: on_leave("¿Quien gano?"))
    sigButton.grid(column=2, row=3)