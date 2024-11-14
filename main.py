import tkinter as tk

class App(tk.Tk):
    def __init__(self, titulo):
        super().__init__()  # Llama al constructor de la clase base

        #GLOBALS
        wd = 1080  # Ancho de app
        hg = 600 # Alto de app
        self.titulo = titulo
        self.title(titulo) # Establece el título de la ventana
        self.createH1(titulo)  # Crea el encabezado H1
        self.resizable(False, False)
        self.config(bg="#111")
        self.iconbitmap("./assets/logo.ico")
        self.geometry(f"{wd}x{hg}")

        # Menu bar
        menubar = tk.Menu(self)
        menu_1 = tk.Menu(menubar, tearoff=0)
        menu_2 = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Home", menu=menu_1)
        menubar.add_cascade(label="Más", menu=menu_2)
        menu_1.add_command(label="Conversor")
        menu_1.add_command(label="Óptica")
        menu_1.add_command(label="Vigas")
        menu_1.add_command(label="Triángulos")
        menu_2.add_command(label="Soporte técnico")
        menu_2.add_command(label="Autor")
        self.config(menu=menubar)

    def createH1(self, title):
        tk.Label(self, text=title, font=("Stencil", 50)).pack(pady=20, padx=20)

    def createH2(self, title):
        tk.Label(self, text=title, font=("Stencil", 35)).pack(pady=20, padx=20)

    def createH3(self, title):
        tk.Label(self, text=title, font=("Stencil", 25)).pack(pady=20, padx=20)

    def crearMenupag(title, command, label):
        tk.Button(label, text=title,
            padx=20, pady=10,
            bg='blue', borderwidth=2, relief='solid',
            font=('Arial', 20), justify='center',
            anchor='center', width=10, height=1, command=print(f"Hola, {command}")
            ).pack(pady=10, side="bottom")
