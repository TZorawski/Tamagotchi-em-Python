from tkinter import *
import tkinter as tt
import tamagotchi
  
class HomeScreen:
    def __init__(self, parent, master=None):
        self.parent = parent

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
  
        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.login
        self.autenticar.pack()
  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def fecha_jan(self):
        self.jan.destroy()
        
    def new_jan(self):
        self.jan=Toplevel()
        self.l=Label(self.jan, text='Feche esta para poder voltar a raiz!')
        self.l.grid()
        b=Button(self.jan, text='Fechar', command=self.fecha_jan)
        b.grid()
        self.jan.geometry('300x200')
        self.jan.transient(root)#
        self.jan.focus_force()#
        self.jan.grab_set()#

    # Entra na conta do usuario
    def login(self):
        usuario = self.nome.get()
        # self.new_jan()
        if True:
            self.petWindow = tt.Toplevel(self.parent)
            self.app = tamagotchi.Application(self.petWindow)
            # self.petWindow.protocol("WM_DELETE_WINDOW", self.app.on_closing)
        else:
            self.petWindow.deiconify()
        # tamagotchi.beginPet()
  

def main():
    global app, stopRead, root
    root = Tk()
    root.geometry("300x300")
    app = HomeScreen(root)
    root.mainloop()


if __name__ == '__main__':
    main()