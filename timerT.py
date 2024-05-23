import winDuels as w
import winDuels2 as w2

def timer(tk, mF, cHack, cBlack, players, rond, det):
    
    # Función para actualizar el temporizador
    def enter(event):
        try:
            if isinstance(int(time.get()), int):
                minutes.set(time.get())
                seconds.set(0)
        except ValueError:
            helpp.configure(text="Tiene que ser un numero pedazo de imbecil")

    def continueTorn():
        for widget in mF.winfo_children():
            widget.destroy()
        if det == 0:
            w.winDuels(tk, mF, cHack, cBlack, players, rond)
        else:
            w2.winDuels2(tk, mF, cHack, cBlack, players, rond)

    def actTemp():
        if temp.get():
            if minutes.get() >= 0:
                if seconds.get() > 0:
                    seconds.set(seconds.get() - 1)
                    clock.after(1000, actTemp)
                else:
                    if minutes.get() == 0:
                        pass
                    else:
                        minutes.set(minutes.get() - 1)
                        seconds.set(59)
                        clock.after(1000, actTemp)
            else:
                seconds.set(seconds.get() - 1)
        else:
            playButton.configure(text="Iniciar")
            rebootButton.configure(state="normal")
            contButton.configure(state='normal')
            time.configure(state="normal")

    # Función para detener el temporizador
    #def stopTemp():
     #   temp.set(False)
      #  stopButton.configure(state='disabled')
       # playButton.configure(state='normal')

    # Función para iniciar el temporizador
    def playTemp():
        temp.set(not temp.get())
        #stopButton.configure(state='normal')
        #playButton.configure(state='disabled')
        rebootButton.configure(state='disabled')
        contButton.configure(state='disabled')
        time.configure(state='disabled')
        playButton.configure(text="Detener")
        actTemp()

    def rebootTemp():
        minutes.set(time.get())
        seconds.set(0)

    def on_enter(text):
        helpp.config(text=text)

    def on_leave(text):
        helpp.config(text=text)

    # Variable para el tiempo en segundos y minutos
    seconds = tk.IntVar()
    seconds.set(0)  # Inicializar los segundos en 0 segundos
    minutes = tk.IntVar()
    minutes.set(40)

    # Variable para controlar el estado del temporizador
    temp = tk.BooleanVar()
    temp.set(False)  # Inicializar el temporizador como Falso para que un mismo boton lo active y pare

    # Frame para el reloj
    clock = tk.Frame(mF, background=cHack, highlightbackground=cHack, highlightcolor= cHack, highlightthickness=2)
    clock.grid(columnspan=3, rowspan=2, column=0, row=0)

    clock.columnconfigure([0,1,2], weight=1)
    clock.rowconfigure(0, weight=1)

    # Instancias
        # Label para el temporizador
    minuteLabel = tk.Label(clock, textvariable=minutes, font=("Consolas", 36), background=cHack, foreground=cBlack)

    points = tk.Label(clock, text=':', font=("Consolas", 36), background=cHack, foreground=cBlack)

    secondLabel = tk.Label(clock, textvariable=seconds, font=("Consolas", 36), background=cHack, foreground=cBlack, width=2)

    helpp = tk.Label(mF, font=('Consolas', 12), text="", bg=cBlack, fg=cHack, height=2)

    min = tk.Label(mF, font=('Consolas', 12), text="Minutos:", bg=cBlack, fg=cHack, height=2)
    time = tk.Entry(mF, width=15, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)

        # Botones
    playButton = tk.Button(mF, text="Iniciar", font=("Consolas", 12), activebackground='red', activeforeground='white')
    #stopButton = tk.Button(mF, text="Parar", font=("Consolas", 12), activebackground='red', activeforeground='white')
    rebootButton = tk.Button(mF, text="Reiniciar", font=("Consolas", 12), activebackground='red', activeforeground='white')
    contButton = tk.Button(mF, text="Siguiente", font=("Consolas", 12), activebackground='red', activeforeground='white')

    # Configuraciones
    minuteLabel.grid(column=0, row=0, padx=[40,0], pady=20)

    points.grid(column=1, row=0, pady=20)

    secondLabel.grid(column=2, row=0, padx=[0,40], pady=20)

    helpp.grid(columnspan=3, column=0, row=4)

    min.grid(column=0, row=2)

    time.grid(column=1, row=2)

    time.configure(font=("Consola", 12), bg=cBlack, fg=cHack)
    time.insert(0, 40)

    time.bind("<Return>", enter)

    playButton.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
    playButton.configure(command=playTemp)
    playButton.bind('<Enter>', lambda event: on_enter("Iniciar el temporizador"))
    playButton.bind('<Leave>', lambda event: on_leave(""))
    playButton.grid(column=0, row=3)

    rebootButton.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
    rebootButton.configure(command=rebootTemp)
    rebootButton.bind('<Enter>', lambda event: on_enter("Reinicia el temporizador"))
    rebootButton.bind('<Leave>', lambda event: on_leave(""))
    rebootButton.grid(column=1, row=3)

    contButton.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
    contButton.configure(command=continueTorn)
    contButton.bind('<Enter>', lambda event: on_enter("Avanzar a la siguiente ventana"))
    contButton.bind('<Leave>', lambda event: on_leave(""))
    contButton.grid(column=2, row=3)
    #stopButton.configure(background=cHack, foreground=cBlack, highlightbackground=cHack, highlightcolor= "red", highlightthickness=2)
    #stopButton.configure(command=stopTemp)
    #stopButton.bind('<Enter>', lambda event: on_enter("Detener el temporizador"))
    #stopButton.bind('<Leave>', lambda event: on_leave(""))
    #stopButton.grid(column=2, row=2)