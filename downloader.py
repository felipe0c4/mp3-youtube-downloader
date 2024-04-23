from pytube import YouTube, Playlist
import os

user = os.getlogin()

def makedir():
    caminho = rf'C:\Users\{user}\Music\NameDownloader'
    if not os.path.exists(caminho):
        os.makedirs(caminho)

makedir()

unica = ["1", "um", "UNICO", "unico", "Unico"]
playlistvariaveis = ["2", "dois", "playlist", "PLAYLIST", "play list", "PLAY LIST", "play", "PLAY", "list", "LIST", "PlayList"]
fechar = ["quit", "QUIT", "FECHAR", "fechar", "SAIR", "sair", "3", "tres", "Quit", "Fechar"]

while True:
    a = str(input("\n Deseja baixar uma musica ou uma PlayList? \n [1]Unica Musica \n [2]PlayList \n [3]Sair \n  "))
    if a in unica:
        url = str(input("URL: "))
        pasta = rf'C:\Users\{user}\Music\NameDownloader'
        try:
            yt = YouTube(url)
            audio = yt.streams.get_audio_only()
            audio.download(pasta)
            print(f'{yt.title} foi baixado')
        except:
            print("\nURl invalida\n")

    elif a in playlistvariaveis:
        urlP = str(input("URL: "))

        pasta = rf'C:\Users\{user}\Music\NameDownloader'

        play = Playlist(urlP)

        try :
            for url in play.video_urls:
                yt = YouTube(url)
                audio = yt.streams.get_audio_only()
                audio.download(pasta)
                print(f'\n{yt.title} foi baixado')
        except:
            print("\nURl invalida\n")
    elif a in fechar:
        print("\n Até uma outra hora :D\n")
        break