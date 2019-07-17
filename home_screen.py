from tkinter import *
import tkinter as tt
import tamagotchi
import time
import potato
import persistence_file
  
class HomeScreen:
    def __init__(self, parent, master=None):
        self.parent = parent

        # Cria containers
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        # ======================== Preenche containers ========================
        self.titulo = Label(self.primeiroContainer, text="Login")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        # Campos do usuário
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        # Campos do PET
        self.petLabel = Label(self.terceiroContainer,text="Pet", font=self.fontePadrao)
        self.petLabel.pack(side=LEFT)
  
        self.pet = Entry(self.terceiroContainer)
        self.pet["width"] = 30
        self.pet["font"] = self.fontePadrao
        self.pet.pack(side=LEFT)
  
        # Submit
        self.btnEntrar = Button(self.quartoContainer)
        self.btnEntrar["text"] = "Entrar"
        self.btnEntrar["font"] = ("Calibri", "8")
        self.btnEntrar["width"] = 12
        self.btnEntrar["command"] = self.login
        self.btnEntrar.pack()

        self.btnNovo = Button(self.quartoContainer)
        self.btnNovo["text"] = "Novo Pet"
        self.btnNovo["font"] = ("Calibri", "8")
        self.btnNovo["width"] = 12
        self.btnNovo["command"] = self.novoPet
        self.btnNovo.pack()


    # Entra na conta do usuario
    def login(self):
        owner = self.nome.get()
        pet = self.pet.get()

        self.petWindow = tt.Toplevel(self.parent)
        appPet = tamagotchi.Application(owner, pet)
        self.app = appPet.buildWindow(self.petWindow)
        # self.petWindow.protocol("WM_DELETE_WINDOW", self.app.on_closing)

    # Cadastra novo PET
    def novoPet (self):
        owner = self.nome.get()
        pet = self.pet.get()

        newPet = potato.Potato(pet)
        rates = newPet.getRates()
        persistence_file.write_file_new_pet(owner, "" + pet + "," + str(time.ctime()) + "," + str(rates[0]) + "," + str(rates[1]) + "," + str(rates[2]) + "," + str(rates[3]) + "," + str(rates[4]))

        self.login()
  

def main():
    global app, root
    root = Tk()
    app = HomeScreen(root)
    root.mainloop()


if __name__ == '__main__':
    main()