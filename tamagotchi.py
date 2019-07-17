from tkinter import *
from tkinter import ttk
import tkinter as tt
import time
import potato
import persistence_file
  
class Application (Toplevel):
    def __init__(self, ownerName, petName):
        # Pega dados do PET
        features = persistence_file.getPet(ownerName, petName)
        # features = persistence_file.getPet('ana', 'jujuba')

        # Instancia PET
        self.pet = potato.Potato(features[0], int(features[2]), int(features[3]), int(features[4]), int(features[5]), int(features[6]))
        self.pet.updateState()

        # Controla taxa de crescimento das barras
        self.growVal = 20

        # self.buildWindow(master)
        

    # Constroi Janela
    def buildWindow (self, master=None):
        self.valHappyBar = 0
        self.valHealthBar = 0
        self.valHungerBar = 0
        self.valCleanBar = 0
        self.valEnergyBar = 0
        self.varHappyBar = tt.DoubleVar()
        self.varHealthBar = tt.DoubleVar()
        self.varHungerBar = tt.DoubleVar()
        self.varCleanBar = tt.DoubleVar()
        self.varEnergyBar = tt.DoubleVar()
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

        self.cleanBar = ttk.Progressbar(self.statusContainer, variable=self.varCleanBar, maximum=100, length=50)
        self.cleanBar.pack(side=LEFT)

        self.energyBar = ttk.Progressbar(self.statusContainer, variable=self.varEnergyBar, maximum=100, length=50)
        self.energyBar.pack(side=LEFT)
        # print(self.minha_barra.config())

        # ********** Main frame **********
        self.mainImage = tt.PhotoImage(file=potato.StatePotato.getImage(self.pet.getState()))
        self.imgPet = Label(self.centerContainer, image=self.mainImage)
        self.imgPet.mainImage = self.mainImage
        self.imgPet.pack()
  
  
        # ********** Actions buttons **********
        # Eat
        self.btnEat = Button(self.optionsContainer)
        self.btnEat["text"] = "Comer"
        self.btnEat["font"] = ("Calibri", "8")
        self.btnEat["width"] = 6
        self.btnEat["command"] = self.toEat
        self.btnEat.pack(side=LEFT)

        # Shower
        self.btnShower = Button(self.optionsContainer)
        self.btnShower["text"] = "Limpar"
        self.btnShower["font"] = ("Calibri", "8")
        self.btnShower["width"] = 6
        self.btnShower["command"] = self.toClean
        self.btnShower.pack(side=LEFT)

        # Cure
        self.btnCure = Button(self.optionsContainer)
        self.btnCure["text"] = "Curar"
        self.btnCure["font"] = ("Calibri", "8")
        self.btnCure["width"] = 6
        self.btnCure["command"] = self.toCure
        self.btnCure.pack(side=LEFT)

        # Sleep
        self.btnSleep = Button(self.optionsContainer)
        self.btnSleep["text"] = "Dormir"
        self.btnSleep["font"] = ("Calibri", "8")
        self.btnSleep["width"] = 6
        self.btnSleep["command"] = self.toSleep
        self.btnSleep.pack(side=LEFT)

        # Play
        self.btnPlay = Button(self.optionsContainer)
        self.btnPlay["text"] = "Brincar"
        self.btnPlay["font"] = ("Calibri", "8")
        self.btnPlay["width"] = 6
        self.btnPlay["command"] = self.verificaSenha
        self.btnPlay.pack(side=LEFT)

        self.updateRates()
  
    # Método verificar senha
    def verificaSenha (self):
        if self.valHappyBar < 100 :
            self.valHappyBar = self.valHappyBar + 1
        if self.valHealthBar < 100 :
            self.valHealthBar = self.valHealthBar + 10
        if self.valHungerBar < 100 :
            self.valHungerBar = self.valHungerBar + 20
            self.valCleanBar = self.valCleanBar + 20

    def toEat (self):
        self.pet.toEat(self.growVal)
        self.updateRates()

    def toCure (self):
        self.pet.toCure(self.growVal)
        self.updateRates()

    def toSleep (self):
        self.pet.toSleep(self.growVal)
        print(self.pet.getState())
        self.updateImg()
        # self.updateRates()
        time.sleep(3)
        self.pet.toWakeUp()
        print(self.pet.getState())
        print('===============')
        self.updateImg()
        self.updateRates()

    def toClean (self):
        self.pet.toClean(self.growVal)
        self.updateRates()


    def updateRates (self):
        rates = self.pet.getRates() # [happy, health, hunger, clean, energy]
        self.valHappyBar = rates[0]
        self.valHealthBar = rates[1]
        self.valHungerBar = rates[2]
        self.valCleanBar = rates[3]
        self.valEnergyBar = rates[4]

        self.varHappyBar.set(self.valHappyBar)
        self.varHealthBar.set(self.valHealthBar)
        self.varHungerBar.set(self.valHungerBar)
        self.varCleanBar.set(self.valCleanBar)
        self.varEnergyBar.set(self.valEnergyBar)

        self.updateImg()

    def updateImg (self):
        self.mainImage2 = tt.PhotoImage(file=potato.StatePotato.getImage(self.pet.getState()))
        self.imgPet.configure(image=self.mainImage2)
        self.imgPet.image=self.mainImage2