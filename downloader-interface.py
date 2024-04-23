from tkinter import *
from pytube import YouTube, Playlist
import os

janela = Tk()

janela.geometry("300x100")

user = os.getlogin()

def makedir():
    caminho = rf'C:\Users\{user}\Music\NameDownloader'
    if not os.path.exists(caminho):
        os.makedirs(caminho)

makedir()

pasta = rf'C:\Users\{user}\Music\NameDownloader'


def DownloadUnico():
    urlU = entradaU.get()
    try :
        yt = YouTube(str(urlU))
        audio = yt.streams.get_audio_only()
        audio.download(pasta)
    except:
        erroU = Label(janelaUnico, text="URL invalida")
        erroU.pack()

def DownloadPlaylist():
    urlP = entradaP.get()
    play = Playlist(str(urlP))
    try :
        for url in play.video_urls:
            yt = YouTube(str(url))
            audio = yt.streams.get_audio_only()
            audio.download(pasta)
    except:
        erro = Label(janelaP, text="URL invalida")
        erro.pack()
        
def unico():
    global entradaU, janelaUnico
    janelaUnico = Tk()
    janelaUnico.geometry("300x100")
    entradaU = Entry(janelaUnico, width=30)
    entradaU.pack(pady=10)
    botao = Button(janelaUnico, text="Download", command=DownloadUnico)
    botao.pack()


def playlist():
    global entradaP, janelaP
    janelaP = Tk()
    janelaP.geometry("300x100")
    entradaP = Entry(janelaP, width=30)
    entradaP.pack(pady=10)
    botao = Button(janelaP, text="Download", command=DownloadPlaylist)
    botao.pack()

botaoU = Button(janela, text="Video Unico", command=unico)
botaoU.pack(pady=10)


botaoP = Button(janela, text="PlayList", command=playlist)
botaoP.pack(pady=10)


janela.mainloop()