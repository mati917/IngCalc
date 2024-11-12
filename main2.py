import tkinter as tk
from Tab_Menu import *
from Tab_Conversor import *
from Tab_Optica import *
from Tab_Vigas import *
from Tab_Triangulos import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #GLOBALS
        wd = 900 # Ancho de app
        hg = 500 # Alto de app
        
        self.title("IngCalc")
        self.resizable(False, False)
        self.config(bg="#111")
        self.iconbitmap("./assets/logo.ico")
        self.geometry(str(wd) + "x" + str(hg))
        self.createH1("Hola")


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

        # Crear las diferentes páginas
        self.pages={}
        for P in (  Tab_Menu,
                    Tab_Conversor,
                    Tab_Optica
                ):
            page_name = P.__name__
            page = P(parent=self, controller=self)
            self.pages[page_name] = page
            
            # Colocar el frame en el contenedor
            page.grid(row=0, column=0, sticky="nsew")

    def createH1(self, title):
        i=0
        locals()[f"{self}_h1-{++i}"] = tk.Label(self,
            text=title,
            font=("Stencil", 50)).pack(pady=20, padx=20)
    def createH2(self, title):
        i=0
        locals()[f"{self}_h2-{++i}"] = tk.Label(self,
            text=title,
            font=("Stencil", 35)).pack(pady=20, padx=20)
    def createH3(self):
        i=0
        locals()[f"{self}_h3-{++i}"] = tk.Label(self,
            text=title,
            font=("Stencil", 25)).pack(pady=20, padx=20)
    
    def show_frame(self, page_name):
        page=self.pages[page_name]
        page.tkraise()



if __name__ == "__main__":
    app = App()
    app.mainloop()
