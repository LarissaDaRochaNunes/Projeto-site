from tkinter import *
from tkinter import ttk

cor1 = "#121211" #preta
cor2 = "#ed87de" #Rosa claro
cor3 = "#faf5f9" #Branco
cor4 = "#5d606e" #cinza
cor5 = "#f542da" #Rosa

janela =Tk()
janela.title("Radar eletrônico")
janela.geometry("400x300")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=400, height=300, bg=cor3)
frame_tela.grid(row=0, column=0)


janela.mainloop()