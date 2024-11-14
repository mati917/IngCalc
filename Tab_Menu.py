# IMPORTS
from main import *

Tab_Menu = App("Menú")  

# Options frame
menu_options = tk.Canvas(Tab_Menu, width=900, height=350)
menu_options.pack(side="bottom", fill="both", expand=True)

# Opciones
paginas = ['Conversor', 'Optica', 'Vigas', 'Triangulos']
for pag in paginas:
    pag = Tab_Menu.crearMenupag(pag, pag, menu_options)

Tab_Menu.mainloop()