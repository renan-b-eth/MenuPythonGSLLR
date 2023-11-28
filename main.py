from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time
from random import randint
from random import *

fraqueza = 5

root = Tk()
#criacao menu
menu= Menu(root)
root.config(menu=menu)
root.title("Menu InovaAcess - GS HapVida")
root.geometry("600x600")
root.resizable(False, False)


def abrirSistema():
    
    #criacao de nova tela
    root2 = Tk()
    root2.title("Menu InovaAcess - GS HapVida")
    root2.geometry("500x500")
    btn2 = Button(root2, text = 'Conectar SmartWatch', bd = '5', 
                          command = lambda: criarFraqueza())
    btn2.place(relx=0.5, rely=0.5, anchor=CENTER)   
    btn2.configure(height=10, width=20, bg="gray") 
    root.destroy() # fecha a tela principal

def alertarFamiliares():
    return None

def criarFraqueza():
    while True:
      time.sleep(1) # só executa depois de 2 segundos
      if(fraqueza <= 0):
          if(fraqueza2 <= 8):
            print("fraqueza está baixa primeiro if")
            break
            print("nao executo mais")
            #ativar o metodo alertarHospital, alertarFamiliares, ligarEmergencia
      else:
        #gera um novo numero para fraqueza
        fraqueza2 = randint(0,100)
        print(fraqueza2)
        if(fraqueza2 <= 8):
            print("fraqueza está baixa ", fraqueza2)
            break
        time.sleep(1)


#criando o botao
btn = Button(root, text = 'Abrir Sistema', bd = '5', #essse lambda é o que faz o evento de clicar e não executar na hora
                          command = lambda: criarFraqueza())
#deixa botão centralizado  
btn.place(relx=0.5, rely=0.5, anchor=CENTER)   
btn.configure(height=10, width=20, bg="green") 




def pfuncionalidade():
    var = tk.StringVar()
    mylabel = tk.Label(root, textvariable=var)
    mylabel.pack()

    messagebox.showinfo('Marcação de Consultas Simplificadas', \
      'Portal de Agendamento Intuitivo: Navegação amigável nos portais Hapvida e Notredame. Eficiência na Marcação: Processo simplificado para agendar consultas médicas com rapidez.')
    
def sfuncionalidade():
    var = tk.StringVar()
    mylabel = tk.Label(root, textvariable=var)
    mylabel.pack()

    messagebox.showinfo('Telemedicina Acessível ', \
      'Consultas Virtuais a Qualquer Hora: Acesso 24/7 para consultas remotas. Conexão Prática e Direta: Plataforma facilitaora de interação entre médicos e pacientes.')

def tfuncionalidade():
    var = tk.StringVar()
    mylabel = tk.Label(root, textvariable=var)
    mylabel.pack()

    messagebox.showinfo(' Carteira de Vacinação Digital ', \
      'Acompanhamento Difital das Imunizações: Registro eletrônico para fácil monitoramento. Notificações Automáticas: Alertas para manter as vacinas em dia.')


def qfuncionalidade():
    var = tk.StringVar()
    mylabel = tk.Label(root, textvariable=var)
    mylabel.pack()

    messagebox.showinfo(' Lembretes Automáticos ', \
      'Sistema de alertas Personalizado: Lembretes automáticos para consultas, exames e vacinas. Organização Eficiente: Promoção da continuidade do cuidado com lembretes personalizaveis')


def quemSomos():
    messagebox.showinfo("Quem Somos?", "Larissa Kawaguti Feliciano - 553356\nLucas Alcântara Carvalho - 95111\nRenan Bezerra dos Santos - 553228")

opcao1 = Menu(menu, tearoff=0)
opcao1.add_command(label= "1 - Funcionalidade Marcação de Consultas Simplificadas", command=pfuncionalidade)
opcao1.add_command(label= "2 - Funcionalidade Telemedicina Acessível", command=sfuncionalidade)
opcao1.add_command(label= "3 - Funcionalidade Carteira de Vacinação Digital", command=tfuncionalidade)
opcao1.add_command(label= "4 - Funcionalidade  Lembretes Automáticos", command=qfuncionalidade)

sobrenos = Menu(menu, tearoff=0)
sobrenos.add_command(label= "Quem somos", command=quemSomos)

sair = Menu(menu, tearoff=0)
sair.add_command(label="Sair", command=exit)


menu.add_cascade(label = "Funcionalidades", menu= opcao1)
menu.add_cascade(label = "Sobre Nos", menu= sobrenos)
menu.add_cascade(label = "Sair", menu= sair)


root.mainloop()