# IMPORTS
from main2 import *


# assets
image1=PhotoImage(file="assets/image1.png")


# Menu bar
menu_bar = Menu(raiz)
menu_1 = Menu(menu_bar, tearoff=0)
menu_2 = Menu(menu_bar, tearoff=0)


menu_2.add_command(label="Soporte técnico")
menu_2.add_command(label="Autor")

menu_bar.add_cascade(label="Home", menu=menu_1)
menu_bar.add_cascade(label="Más", menu=menu_2)

raiz.config(menu=menu_bar)

# Tittle frame
menu_title = Frame(raiz, height="150")
menu_title.config(bg="tan")
menu_title.pack(fill='x')

menu_title_h1 = Label(menu_title, text="Ing Calc", font=('Stencil', 50), justify='left')
menu_title_h1.pack(pady=10, padx=10, anchor='w')

# Options frame
menu_options = Canvas(raiz, width=900, height=350)
menu_options.pack(side="bottom", fill="both", expand=True)
menu_options.create_image(0, 0, anchor='w', image=image1)

# Opciones
menu_options_op1 = Label(menu_options, text="Conversor",
    padx=20, pady=10,
    bg='blue', borderwidth=2, relief='solid',
    font=('Arial', 20), justify='center',
    anchor='center', width=10, height=1
)
menu_options_op1.pack(pady=10)

menu_options_op2 = Label(menu_options, text="Óptica",
    padx=20, pady=10,
    bg='blue', borderwidth=2, relief='solid',
    font=('Arial', 20), justify='center',
    anchor='center', width=10, height=1
)
menu_options_op2.pack(pady=10)

menu_options_op3 = Label(menu_options, text="Vigas",
    padx=20, pady=10,
    bg='blue', borderwidth=2, relief='solid',
    font=('Arial', 20), justify='center',
    anchor='center', width=10, height=1
)
menu_options_op3.pack(pady=10)

menu_options_op4 = Label(menu_options, text="Triángulos",
    padx=20, pady=10,
    bg='blue', borderwidth=2, relief='solid',
    font=('Arial', 20), justify='center',
    anchor='center', width=10, height=1
)
menu_options_op4.pack(pady=10)

raiz.mainloop()