#Miguel Hellmann Preuss
#insta: miguelhpreuss
#Descrição: Bot para whatsapp com tela 1920 x 1080 com navegador em meia tela

from pyautogui import *

if size().width != 1920 or size().height != 1080:
    print("Resolução não suportada") 
    quit()

class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def conferePosicao(x, y):
    posicaoatual = position()
    if x != posicaoatual.x or y != posicaoatual.y:
        alert("Programa abortado!")
        quit()

def clique(x, y, t = 1):
    moveTo(x, y, t)
    conferePosicao(x, y)
    #c = confirm("Clicar?")
    #if c == 'Cancel':
    #    quit()
    click(x, y)


WPP_aba = Vetor(71, 32)
WPP_busca = Vetor(184, 163)
WPP_selecionar = Vetor(142, 272)
WPP_campotexto = Vetor(602, 1010)
WPP_enviar = Vetor(925, 1010)

def mandar_msg(dest, msg, t):

    clique(WPP_aba.x, WPP_aba.y, t)

    clique(WPP_busca.x, WPP_busca.y, t)

    hotkey('ctrl', 'a')
    hotkey('backspace')
    typewrite(dest, t)

    clique(WPP_selecionar.x, WPP_selecionar.y, t)

    clique(WPP_campotexto.x, WPP_campotexto.y, t)
    typewrite(msg)
    clique(WPP_enviar.x, WPP_enviar.y, t)


mandar_msg("Nome do contato", "mensagem", 0)

#print("Vetor({}, {})".format(position().x, position().y))

print("Fim do programa!")
