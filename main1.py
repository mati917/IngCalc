from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        #GLOBALS
        wd = 900 # Ancho de app
        hg = 500 # Alto de app
        
        self.title("IngCalc")
        self.geometry(str(wd) + "x" + str(hg))

        # Menu
        menu_bar = Menu(self)
        menu_1 = Menu(menu_bar, tearoff=0)
        menu_2 = Menu(menu_bar, tearoff=0)
        
        # Crear un contenedor para las páginas
        self.frames = {}
        
        # Crear las diferentes páginas
        for F in (  Tab_Menu,
                    Tab_Conversor,
                    Tab_Optica
                ):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            
            # Colocar el frame en el contenedor
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("Tab_Menu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class Tab_Menu(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = Label(self, text="IngCalc", font=("Stencil", 50))
        label.pack(pady=20, padx=20)
        
        button = Button(self, text="Conversor",
                            command=lambda: controller.show_frame("Tab_Conversor"),
                            padx=20, pady=10,
                            bg='blue', borderwidth=2, relief='solid',
                            font=('Arial', 20), justify='center',
                            anchor='center', width=10, height=1)
        button.pack(pady=10)

        button2 = Button(self, text="Vigas",
                            command=lambda: controller.show_frame("Tab_Vigas"),
                            padx=20, pady=10,
                            bg='blue', borderwidth=2, relief='solid',
                            font=('Arial', 20), justify='center',
                            anchor='center', width=10, height=1)
        button2.pack(pady=10)

        button3 = Button(self, text="Óptica",
                            command=lambda: controller.show_frame("Tab_Optica"),
                            padx=20, pady=10,
                            bg='blue', borderwidth=2, relief='solid',
                            font=('Arial', 20), justify='center',
                            anchor='center', width=10, height=1)
        button3.pack(pady=10)

        button4 = Button(self, text="Triángulos",
                            command=lambda: controller.show_frame("Tab_Triangulo"),
                            padx=20, pady=10,
                            bg='blue', borderwidth=2, relief='solid',
                            font=('Arial', 20), justify='center',
                            anchor='center', width=10, height=1)
        button4.pack(pady=10)

       

class Tab_Conversor(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = Label(self, text="Conversor", font=("Helvetica", 16))
        label.pack(pady=10)
        
        button = Button(self, text="Ir a Página 1",
                           command=lambda: controller.show_frame("Tab_Menu"))
        button.pack()

        button2 = Button(self, text="Ir a Página 3",
                            command=lambda: controller.show_frame("Tab_Optica"))
        button2.pack()

class Tab_Optica(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = Label(self, text="Óptica", font=("Helvetica", 16))
        label.pack(pady=10)
        
        button = Button(self, text="Ir a Página 1",
                           command=lambda: controller.show_frame("Tab_Menu"))
        button.pack()

        button2 = Button(self, text="Ir a Página 2",
                            command=lambda: controller.show_frame("Tab_Optica"))
        button2.pack()

class Tab_Vigas(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = Label(self, text="Vigas", font=("Helvetica", 16))
        label.pack(pady=10)
        
        button = Button(self, text="Ir a Página 1",
                           command=lambda: controller.show_frame("Tab_Menu"))
        button.pack()

        button2 = Button(self, text="Ir a Página 2",
                            command=lambda: controller.show_frame("Tab_Optica"))
        button2.pack()

class Tab_Triangulo(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = Label(self, text="Triángulos", font=("Helvetica", 16))
        label.pack(pady=10)
        
        button = Button(self, text="Ir a Página 1",
                           command=lambda: controller.show_frame("Tab_Menu"))
        button.pack()

        button2 = Button(self, text="Ir a Página 2",
                            command=lambda: controller.show_frame("Tab_Optica"))
        button2.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()