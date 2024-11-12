# IMPORTS
from main2 import *
class Tab_Menu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # assets
        image1=tk.PhotoImage(file="assets/image1.png")


        # Tittle frame
        menu_title = tk.Frame(self, height="150")
        menu_title.config(bg="tan")
        menu_title.pack(fill='x')

        menu_title_h1 = tk.Label(menu_title, text="Ing Calc", font=('Stencil', 50), justify='left')
        menu_title_h1.pack(pady=10, padx=10, anchor='w')

        # Options frame
        menu_options = tk.Canvas(self, width=900, height=350)
        menu_options.pack(side="bottom", fill="both", expand=True)
        menu_options.create_image(0, 0, anchor='w', image=image1)

        # Opciones
        menu_options_op1 = tk.Label(menu_options, text="Conversor",
            padx=20, pady=10,
            bg='blue', borderwidth=2, relief='solid',
            font=('Arial', 20), justify='center',
            anchor='center', width=10, height=1
        )
        menu_options_op1.pack(pady=10)

        menu_options_op2 = tk.Label(menu_options, text="Óptica",
            padx=20, pady=10,
            bg='blue', borderwidth=2, relief='solid',
            font=('Arial', 20), justify='center',
            anchor='center', width=10, height=1
        )
        menu_options_op2.pack(pady=10)

        menu_options_op3 = tk.Label(menu_options, text="Vigas",
            padx=20, pady=10,
            bg='blue', borderwidth=2, relief='solid',
            font=('Arial', 20), justify='center',
            anchor='center', width=10, height=1
        )
        menu_options_op3.pack(pady=10)

        menu_options_op4 = tk.Label(menu_options, text="Triángulos",
            padx=20, pady=10,
            bg='blue', borderwidth=2, relief='solid',
            font=('Arial', 20), justify='center',
            anchor='center', width=10, height=1
        )
        menu_options_op4.pack(pady=10)