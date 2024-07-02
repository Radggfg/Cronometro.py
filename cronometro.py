from tkinter import *

# Cores
cor1 = "#0a0a0a"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

# Configurando a janela----------
janela = Tk()
janela.title("")
janela.geometry('300x180')
janela.configure(bg=cor1)
janela.resizable(width=False, height=False)

# Definindo variáveis globais
global tempo
global rodar
global contador
global limitador

limitador = 59
tempo = "00:00:00"
rodar = True
contador = -5

# Função iniciar
def iniciar():
    global tempo
    global contador
    global limitador

    if rodar:
        # Antes do cronômetro começar
        if contador < 0:
            inicio = 'Começando em ' + str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Times 20 bold'
        else:
            label_tempo['font'] = 'Times 50 bold'

            h, m, s = map(int, tempo.split(":"))
            s = contador

            if s >= limitador:
                contador = 0
                m += 1

            if m >= 60:
                m = 0
                h += 1

            s_str = str(s).zfill(2)
            m_str = str(m).zfill(2)
            h_str = str(h).zfill(2)

            # Atualizando os valores atuais
            temporario = f"{h_str}:{m_str}:{s_str}"
            label_tempo['text'] = temporario
            tempo = temporario

        label_tempo.after(1000, iniciar)
        contador += 1

# Função para dar início
def start():
    global rodar
    rodar = True
    iniciar()


# Função pausar
def pausar():
    global rodar
    rodar = False



# Função reiniciar
def reiniciar():
    global contador
    global tempo

    # reiniciando o contador
    contador = 0

    # reiniciando o tempo
    tempo = "00:00:00"
    label_tempo['text'] = tempo




# Criando Labels
label_app = Label(janela, text='Cronômetro', font=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)
label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor4)
label_tempo.place(x=20, y=30)

# Criando Botões
botao_inicial = Button(janela, command=start, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_inicial.place(x=20, y=130)

botao_pausar = Button(janela, command=pausar, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=105, y=130)

botao_reiniciar = Button(janela, command=reiniciar, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=190, y=130)

janela.mainloop()
