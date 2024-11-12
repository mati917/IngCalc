import tkinter as tk

class Tab_Menu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = tk.Label(self, text="IngCalc", font=("Stencil", 50))
        label.pack(pady=20, padx=20)
        
        button = tk.Button(self, text="Conversor",
                           command=lambda: controller.show_frame("Page2"))
        button.pack()

        button2 = tk.Button(self, text="Vigas",
                            command=lambda: controller.show_frame("Page3"))
        button2.pack()

        button3 = tk.Button(self, text="Óptica",
                            command=lambda: controller.show_frame("Page3"))
        button3.pack()

        button4 = tk.Button(self, text="Triángulos",
                            command=lambda: controller.show_frame("Page3"))
        button4.pack()