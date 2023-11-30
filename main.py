from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time
from random import randint
from random import *
from tkinter import ttk
import matplotlib.pyplot as plt
#from playsound import playsound tentei mas está dando bug
from datetime import datetime
import os
import webbrowser
from geopy.geocoders import Nominatim


fraqueza = 5
fraqueza2 = 5
tamanhoLista = 0
enderecoCompleto = None


os.system('cls')


root = Tk()
#criacao menu
menu= Menu(root)
root.config(menu=menu)
root.title("Menu InovaAcess - GS HapVida")
root.geometry("600x600")
root.resizable(False, False)


root2 = Tk()
root2.title("Menu InovaAcess - GS HapVida")
root2.geometry("500x500")
variavelMuda = tk.DoubleVar()
label = Label(root2, text = f"ESTAMOS MONITORANDO SUA FREQUENCIA CARDIACA", textvariable= variavelMuda).place(x = 40,y = 100)  
root2.withdraw() # deixa a tela ocultada


etLogin = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
etLogin.place(x=200, y=50)
lblLogin = Label(font=('Arial', '11', 'bold'), fg='black', text='Login:')
lblLogin.place(x=180, y=50)


etSenha = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
etSenha.place(x=200, y=100)
lblSenha = Label(font=('Arial', '11', 'bold'), fg='black', text='Senha:')
lblSenha.place(x=180, y=100)


btnLogin = Button(root, text = 'login', bd = '5',
                       command = lambda: validarLogin(etLogin.get(),etSenha.get()))                  
btnLogin.place(x=310, y=150, anchor=CENTER)
btnLogin.configure(height=2, width=5, bg="#CDAA64")


def criarMensagem(titulo, mensagem):
    return messagebox.showinfo(titulo, mensagem)


#metodo validar login
def validarLogin(login, senha):
    loginPadrao = "admin"
    senhaPadrao = "admin"
    if login == loginPadrao and senha == senhaPadrao:
        criarMensagem("LOGIN OK", "LOGIN FEITO COM SUCESSO")
        #criando o botao
        btn = Button(root, text = 'Abrir Sistema', bd = '5', #essse lambda é o que faz o evento de clicar e não executar na hora
                          command = lambda: abrirSistema())
        #deixa botão centralizado  
        btn.place(relx=0.5, rely=0.5, anchor=CENTER)  
        btn.configure(height=10, width=20, bg="green")
    else:
        criarMensagem("LOGIN ERRADO", "TENTE NOVAMENTE, SENHA OU LOGIN ERRADO")


#criacao da barra de progresso
progress_bar = ttk.Progressbar(root2, length=300, mode="determinate", orient="horizontal")
progress_bar.grid(row=5, column=0, sticky=E, padx=0.5, pady=0.5)


def abrirSite(url):
    return webbrowser.open(url)


def atualizar_barra(valor):
    progress_bar["value"] = valor
    root2.update()


def abrirSistema():
   
    #criacao de nova tela
   
    btn2 = Button(root2, text = 'Conectar SmartWatch', bd = '5',
                          command = lambda: criarFraqueza())                  
    btn2.place(relx=0.5, rely=0.5, anchor=CENTER)
    btn2.configure(height=10, width=20, bg="gray")
    root.destroy() # fecha a tela principal
    root2.deiconify() # aparece a tela


def trocarLabel(numero):
    numero2 = StringVar()
    numero2.set(numero)
    label = Label(root2, text = "", textvariable= numero2).place(x = 40,y = 100)  


def alertarFamiliares():
    return messagebox.showinfo(' AVISAR OS FAMILIARES!! ', \
            'Todos os seus familiares cadastrados no sistema foi avisado com sucesso!')


def ligarEmergencia(numero):
    return messagebox.showinfo(' LIGANDO PARA O NUMERO!! ', \
            'Estamos ligando para o numero: ' + numero +  ' para acionar a emergencia!!')


#Pega sua localização


def criarFraqueza():
    messagebox.showinfo(' SmarthWatch ', \
            'SmarthWatch conectado com sucesso!!')
    #criacao da lista
    listaValores = []
    while True:
      time.sleep(0.5) # só executa depois de 2 segundos
      if(fraqueza <= 0):
          if(fraqueza2 <= 5):
            print("fraqueza está baixa primeiro if")
            break
            #ativar o metodo alertarHospital, alertarFamiliares, ligarEmergencia
      else:
        #gera um novo numero para fraqueza
        fraqueza2 = randint(0,100)
        listaValores.append(fraqueza2) ## adiciona na lista os valores
        print(fraqueza2)
        #toca o bip1 do coração
        #playsound('bipc1.mp3')
        variavelMuda.set(fraqueza2)
        #nao consegui atualizar na label
        atualizar_barra(fraqueza2)
        #toca o bip2 do coração
        #playsound("bipc1.mp3")
        #messagebox.showinfo(' SUA FRAQUEZA É ', \
           # f'Sua fraqueza é: {fraqueza2} ')
        if(fraqueza2 <= 5):
             #toca o alerta do coração
           
            tamanhoLista = len(listaValores) # pega o tamanho da lista
            #print(f'tamanho da lista {len(listaValores)}')
            # pega a sua localização em tempo real
            geo = Nominatim(user_agent="geo")
            loc = geo.geocode("rua dos nordestinos 12")
            enderecoCompleto = loc.address , " Latitude: " , loc.latitude , " logintude" ,  loc.longitude
            #print(enderecoCompleto)
            ligarEmergencia("192") # vai chamar o metodo ligarEmergencia
            abrirSite("www.samues.com.br") #abre o site
            time.sleep(2)
            alertarFamiliares()
            #tentar colocar ligação para avisar familiares
            alertarHospital(enderecoCompleto)
            linkGoogle = "www.google.com.br/maps/@" + str(loc.latitude) + "," + str(loc.longitude) +",15z?entry=ttu"
            abrirSite(linkGoogle) # abre o mapa do google com sua localização
            time.sleep(5)
            abrirSite("https://www2.gndi.com.br/pt/hospitalrosario")
            #www.google.com.br/maps/@-23.5601864,-46.6423727,15z?entry=ttu
            messagebox.showinfo(' RELATÓRIO!! ', \
            f'Esse é o seu relatório de variações de fraqueza: {listaValores}')
            criarGrafico(listaValores, len(listaValores)) #cria o gráfico
            messagebox.showinfo(' RELATÓRIO!! ', \
            f'Relatório enviado com sucesso para o servidor do hospital, juntamente com a sua ficha de alergias e ficha médica, aguarde a ambulância!!!')
            break
        time.sleep(0.5)



def alertarHospital(endereco):
    dataAtual = datetime.now()
    return messagebox.showinfo(' HOSPITAL AVISADO!! ', \
            f'O hospital onde está cadastrado já foi avisado no horario: {dataAtual} e sua localização: {endereco} foi enviada com sucesso!')


#criar o gráfico


def criarGrafico(listaValor, tamanhoLista):
    eixoY = []
    eixoX = listaValor
    i=10
    for i in range(tamanhoLista):
        #adiciona na lista o tamanho de numeros de x
        eixoY.append(i)
        i = i + 10
    plt.plot(eixoX, eixoY)
    return plt.show()


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