from tkinter import *
# GLOBALS
wd = 900 # Ancho de app
hg = 500 # Alto de app

# Config raiz
raiz = Tk()
raiz.title("IngCalc")
raiz.resizable(False, False)
raiz.config(bg="#111")
raiz.iconbitmap("./assets/logo.ico")
raiz.geometry(str(wd) + "x" + str(hg))