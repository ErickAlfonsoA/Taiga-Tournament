import math
import random
import major as m
import timerT as t

def duels(tk, mF, cHack, cBlack, name, players, logo, font):
    def mostrarDatos():
        print(name)
        print("")
        print(players)

    def returnMajor():
        for widget in mF.winfo_children():
            widget.destroy()
        m.major(tk, mF, cHack, cBlack, name, logo, font)

    def continueTorn():
        for widget in mF.winfo_children():
            widget.destroy()
        t.timer(tk, mF, cHack, cBlack, players, rond, 0)
    
    def on_enter(text):
        helpp.config(text=text)

    def on_leave(text):
        helpp.config(text=text)

    #Nuevo frame para la tabla
    table = tk.Frame(mF, background=cBlack, highlightbackground=cHack, highlightcolor= cHack, highlightthickness=2)
    table.grid(columnspan=3, rowspan=3, column=0, row=0)

    #Operaciones varias para el numero de rondas y primera ronda
    size = len(players)
    print(players)
    
    rond = round(math.log2(size))
    print("Numero de rondas:", rond)

    random.shuffle(players)
    print(players)

    #Mostrar en un label los duelos
    if size % 2 == 0:
        for p in range(0, size, 2):
            duel = tk.Label(table, font=('Consolas', 12), text=players[p][0]+" vs "+players[p+1][0], bg=cBlack, fg='#20C20E', height=2)
            duel.grid(columnspan=3, row=p, column=0, padx=20)
    else:
        for p in range(0, size-1, 2):
            duel = tk.Label(table, font=('Consolas', 12), text=players[p][0]+" vs "+players[p+1][0], bg=cBlack, fg='#20C20E', height=2)
            duel.grid(columnspan=3, row=p, column=0, padx=20)
        duel = tk.Label(table, font=('Consolas', 12), text=players[size-1][0]+" Tiene pase directo", bg=cBlack, fg='#20C20E', height=2)
        duel.grid(columnspan=3, row=p+1, column=0, padx=20)
        players[size-1][1] += 2
        print("despues del pase\n")
        print(players)

    #Instancias
    before = tk.Button(mF, text="Anterior", font=("Consolas", 12), activebackground='red', activeforeground='white')
    after = tk.Button(mF, text="Continuar", font=("Consolas", 12), activebackground='red', activeforeground='white')

    helpp = tk.Label(mF, font=('Consolas', 12), text="Numero de rondas: "+str(rond), bg=cBlack, fg=cHack, height=2)

    #Configuraciones
    helpp.grid(columnspan=3, row=4, column=0)

    before.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
    before.configure(command=returnMajor)
    before.bind('<Enter>', lambda event: on_enter("Regresar a la ventana anterior"))
    before.bind('<Leave>', lambda event: on_leave("Numero de rondas: "+str(rond)))
    before.grid(row=3, column=0)

    after.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
    after.configure(command=continueTorn)
    after.bind('<Enter>', lambda event: on_enter("Continuar con el torneo"))
    after.bind('<Leave>', lambda event: on_leave("Numero de rondas: "+str(rond)))
    after.grid(row=3, column=2)

    #mostrar = tk.Button(mF, text="Añadir", font=("Consolas", 12), activebackground='red', activeforeground='white')
    #mostrar.configure(command=mostrarDatos)
    #mostrar.grid(row=0, column=0)