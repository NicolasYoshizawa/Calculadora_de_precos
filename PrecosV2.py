# Importa as bibliotecas
from tkinter import *
import tkinter.font as tkFont
import pandas as pd

# Lê e trata a base de dados em excel
data = pd.read_excel("preços das unidades.xlsx", engine='openpyxl')
data = data.drop(columns='prato')

# Cria e configura a interface gráfica
root = Tk()
root.title('Preços')
root.geometry('400x300')
root.resizable(False, False)

# Algumas variáveis e configurações de estilo da interface gráfica
background = '#696969'
background2 = '#D3D3D3'
root.configure(bg=background)
fontStyle = tkFont.Font(family="Comic Sans MS", size=13)

# Cria a função responsável por obter a variável do usuário, calcular o preço total e exibe na interface gráfica
def calcular(event):
    sashimi = data['preço'][0]
    tako = data['preço'][1]
    niguiri = data['preço'][2]
    niguiriebi = data['preço'][3]
    gyoza = data['preço'][4]
    x = int(entry.get())
    texto1['text'] = '{} fatias de sashimi fica R${:.2f}'.format(x, sashimi*x)
    texto2['text'] = '{} fatias de tako fica R${:.2f}'.format(x, tako * x)
    texto3['text'] = '{} un de niguiri z fica R${:.2f}'.format(x, niguiri * x)
    texto4['text'] = '{} un de niguiri de Tako/Ebi fica R${:.2f}'.format(x, niguiriebi * x)
    texto5['text'] = '{} un de gyozá fica R${:.2f}'.format(x, gyoza * x)
    entry.delete(0, END)

# Cria a entreda para receber a variável do usuário
entry = Entry(root, bd='5', bg=background2)
entry.pack(padx=10, pady=10)

# Cria o botão para executar a função
botao = Button(root, text='Calcular', bd='5', command=calcular, height=2, width=10, bg=background2)
botao.pack(padx=10, pady=10)

root.bind('<Return>', calcular)

# Configuração para que o preço apareça na interface gráfica
texto1 = Label(root, text='', font=fontStyle, bg=background, foreground='white')
texto1.pack()
texto2 = Label(root, text='', font=fontStyle, bg=background, foreground='white')
texto2.pack()
texto3 = Label(root, text='', font=fontStyle, bg=background, foreground='white')
texto3.pack()
texto4 = Label(root, text='', font=fontStyle, bg=background, foreground='white')
texto4.pack()
texto5 = Label(root, text='', font=fontStyle, bg=background, foreground='white')
texto5.pack()

# Cria um loop da interface gráfica, mantendo-a aberta
root.mainloop()
