# IMPORTS
from main import *

Tab_Menu = App("Vigas")  

def crearMenupag(title, command):
    tk.Button(menu_options, text=title,
    padx=20, pady=10,
    bg='blue', borderwidth=2, relief='solid',
    font=('Arial', 20), justify='center',
    anchor='center', width=10, height=1, command=print(f"Hola, {command}")
    ).pack(pady=10, side="bottom")


# Options frame
menu_options = tk.Canvas(Tab_Menu, width=900, height=350)
menu_options.pack(side="bottom", fill="both", expand=True)

# Opciones
paginas = ['Flexión', 'Compresión', 'Torsión', 'Cerca']
for pag in paginas:
    pag = crearMenupag(pag, pag )

Tab_Menu.mainloop()