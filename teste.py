from tkinter import *
from tkinter import ttk
import tkinter as tt
# import tkinter as tt
  
class Application:
    def __init__(self, master=None):
        self.valorbarra = 0
        self.fontePadrao = ("Arial", "10")
        self.var_barra = tt.DoubleVar()

        # Cria containers
        self.statusContainer = Frame(master)
        self.statusContainer["padx"] = 20
        self.statusContainer.pack()

        self.centerContainer = Frame(master)
        # self.centerContainer["pady"] = 200
        self.centerContainer.pack()
  
        self.optionsContainer = Frame(master)
        self.optionsContainer["padx"] = 20
        self.optionsContainer.pack()
  
        # Preenche containers
        imagem = tt.PhotoImage(file="happy.gif")
        self.titulo = Label(self.centerContainer, image=imagem)
        self.titulo.imagem = imagem
        self.titulo.pack()
  
        # Status Bar
        self.minha_barra = ttk.Progressbar(self.statusContainer, variable=self.var_barra, maximum=100)
        self.minha_barra.pack(side=LEFT)
  
        # Actions buttons
        # Eat
        self.btnEat = Button(self.optionsContainer)
        self.btnEat["text"] = "Comer"
        self.btnEat["font"] = ("Calibri", "8")
        self.btnEat["width"] = 6
        self.btnEat["command"] = self.verificaSenha
        self.btnEat.pack(side=LEFT)

        # Shower
        self.btnShower = Button(self.optionsContainer)
        self.btnShower["text"] = "Limpar"
        self.btnShower["font"] = ("Calibri", "8")
        self.btnShower["width"] = 6
        self.btnShower["command"] = self.verificaSenha
        self.btnShower.pack(side=LEFT)

        # Cure
        self.btnCure = Button(self.optionsContainer)
        self.btnCure["text"] = "Curar"
        self.btnCure["font"] = ("Calibri", "8")
        self.btnCure["width"] = 6
        self.btnCure["command"] = self.verificaSenha
        self.btnCure.pack(side=LEFT)

        # Play
        self.btnPlay = Button(self.optionsContainer)
        self.btnPlay["text"] = "Brincar"
        self.btnPlay["font"] = ("Calibri", "8")
        self.btnPlay["width"] = 6
        self.btnPlay["command"] = self.verificaSenha
        self.btnPlay.pack(side=LEFT)

  
    #Método verificar senha
    def verificaSenha(self):
        if self.valorbarra < 100 :
            self.valorbarra = self.valorbarra + 1

        self.var_barra.set(self.valorbarra)
        root.update()
  
  
root = tt.Tk()
Application(root)
root.mainloop()