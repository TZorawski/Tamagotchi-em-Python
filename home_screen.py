from tkinter import *
import tkinter as tt
import tamagotchi
  
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
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        # ======================== Preenche containers ========================
        self.titulo = Label(self.primeiroContainer, text="Login")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.botao = Button(self.quartoContainer)
        self.botao["text"] = "Entrar"
        self.botao["font"] = ("Calibri", "8")
        self.botao["width"] = 12
        self.botao["command"] = self.login
        self.botao.pack()


    # Entra na conta do usuario
    def login(self):
        usuario = self.nome.get()
        self.petWindow = tt.Toplevel(self.parent)
        self.app = tamagotchi.Application(self.petWindow)
        # self.petWindow.protocol("WM_DELETE_WINDOW", self.app.on_closing)
  

def main():
    global app, root
    root = Tk()
    app = HomeScreen(root)
    root.mainloop()


if __name__ == '__main__':
    main()