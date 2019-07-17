from tkinter import *
from tkinter import ttk
import tkinter as tt
import time
import datetime
import potato
import persistence_file
  
class Application (Toplevel):
    def __init__(self, ownerName, petName):
        # self.ownerName = ownerName
        # self.petName = petName
        # Pega dados do PET
        # features = persistence_file.getPet(ownerName, petName)
        features = persistence_file.getPet('ana', 'jujuba')
        self.ownerName = 'ana'
        self.petName = 'jujuba'

        # Instancia PET
        self.pet = potato.Potato(features[0], datetime.datetime.strptime(features[1], '%a %b %d %H:%M:%S %Y'), float(features[2]), float(features[3]), float(features[4]), float(features[5]), float(features[6]))
        # self.pet = potato.Potato(features[0], time.strptime(features[1], '%a %b %d %H:%M:%S %Y'), int(features[2]), int(features[3]), int(features[4]), int(features[5]), int(features[6]))

        # Controla o tempo de vida do PET
        self.time = time.ctime()
        self.pet.timeLife(datetime.datetime.now()) # Atualiza valores de acordo com o tempo


        #self.pet.updateState()

        # Controla taxa de crescimento das barras
        self.growVal = 10

        # self.buildWindow(master)
        

    # Constroi Janela
    def buildWindow (self, master=None):
        self.master = master
        self.master.protocol('WM_DELETE_WINDOW', self.closeWindow)
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
        self.fontePadrao = ("Arial", "8")

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
        self.labelHappy = Label(self.statusContainer,text="Happy:", font=self.fontePadrao)
        self.labelHappy.pack(side=LEFT)
        self.happyBar = ttk.Progressbar(self.statusContainer, variable=self.varHappyBar, maximum=100, length=50)
        self.happyBar.pack(side=LEFT)

        self.labelHealth = Label(self.statusContainer,text="Health:", font=self.fontePadrao)
        self.labelHealth.pack(side=LEFT)
        self.healthBar = ttk.Progressbar(self.statusContainer, variable=self.varHealthBar, maximum=100, length=50)
        self.healthBar.pack(side=LEFT)

        self.labelHunger = Label(self.statusContainer,text="Hunger:", font=self.fontePadrao)
        self.labelHunger.pack(side=LEFT)
        self.hungerBar = ttk.Progressbar(self.statusContainer, variable=self.varHungerBar, maximum=100, length=50)
        self.hungerBar.pack(side=LEFT)

        self.labelClean = Label(self.statusContainer,text="Clean:", font=self.fontePadrao)
        self.labelClean.pack(side=LEFT)
        self.cleanBar = ttk.Progressbar(self.statusContainer, variable=self.varCleanBar, maximum=100, length=50)
        self.cleanBar.pack(side=LEFT)

        self.labelEnergy = Label(self.statusContainer,text="Energy:", font=self.fontePadrao)
        self.labelEnergy.pack(side=LEFT)
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
        self.life()

    def closeWindow (self):
        rates = self.pet.getRates()
        persistence_file.write_file(self.ownerName, self.petName, "" + self.petName + "," + str(time.ctime()) + "," + str(rates[0]) + "," + str(rates[1]) + "," + str(rates[2]) + "," + str(rates[3]) + "," + str(rates[4]))
        self.master.destroy()
  
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

    def life (self):
        now = datetime.datetime.now()
        # Se já passou mais de 3 segundos desde a ultima atualização
        # print(((now - self.pet.getTime()).seconds))
        if ((now - self.pet.getTime()).seconds) >= 1:
            self.pet.timeLife(now) # Atualiza valores de acordo com o tempo
            self.updateRates()
            # self.master.update()
        time.sleep(0.5)
        self.life()
        
