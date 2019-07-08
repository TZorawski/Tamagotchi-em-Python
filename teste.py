from tkinter import *
from tkinter import ttk
import tkinter as tt
# import tkinter as tt
  
class Application:
    def __init__(self, master=None):
        self.valHappyBar = 0
        self.valHealthBar = 0
        self.valHungerBar = 0
        self.varHappyBar = tt.DoubleVar()
        self.varHealthBar = tt.DoubleVar()
        self.varHungerBar = tt.DoubleVar()
        self.fontePadrao = ("Arial", "10")

        # Cria containers
        self.statusContainer = Frame(master)
        self.statusContainer.pack()

        self.centerContainer = Frame(master)
        self.centerContainer.pack()
  
        self.optionsContainer = Frame(master)
        self.optionsContainer["padx"] = 20
        self.optionsContainer.pack()
  
        # ======================== Preenche containers ========================
        # ********** Status Bar **********
        self.happyBar = ttk.Progressbar(self.statusContainer, variable=self.varHappyBar, maximum=100, length=50)
        self.happyBar.pack(side=LEFT)

        self.healthBar = ttk.Progressbar(self.statusContainer, variable=self.varHealthBar, maximum=100, length=50)
        self.healthBar.pack(side=LEFT)

        self.hungerBar = ttk.Progressbar(self.statusContainer, variable=self.varHungerBar, maximum=100, length=50)
        self.hungerBar.pack(side=LEFT)
        # print(self.minha_barra.config())

        # ********** Main frame **********
        imagem = tt.PhotoImage(file="happy.gif")
        self.titulo = Label(self.centerContainer, image=imagem)
        self.titulo.imagem = imagem
        self.titulo.pack()
  
  
        # ********** Actions buttons **********
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
        if self.valHappyBar < 100 :
            self.valHappyBar = self.valHappyBar + 1
        if self.valHealthBar < 100 :
            self.valHealthBar = self.valHealthBar + 10
        if self.valHungerBar < 100 :
            self.valHungerBar = self.valHungerBar + 20

        self.varHappyBar.set(self.valHappyBar)
        self.varHealthBar.set(self.valHealthBar)
        self.varHungerBar.set(self.valHungerBar)
        root.update()
  
  
root = tt.Tk()
Application(root)
root.mainloop()