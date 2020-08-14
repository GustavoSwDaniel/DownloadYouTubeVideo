from pytube import YouTube
import PySimpleGUI as sg
import time


class Download(object):
    
    def __init__(self):
        self.__url = ''
    

    def start(self):

        layout = [
            [sg.Text('Link do Video: ', size=(40,0))],
            [sg.Input()],
            [sg.Text('Qualidade', size=(40,0))],
            [sg.InputCombo(('720p', '480p', '360p', '240p', '144p'), size=(20, 1))],
            [sg.Output(size=(50,10))],
            [sg.Button('Baixar'), sg.Button('Sair')],
        ]

        self.janela = sg.Window('Decida por Mim!', layout=layout)
        self.evento, self.valores = self.janela.Read()
        print(type(self.valores))
        self._download()

    def _download(self):
        if self.evento == 'Baixar':
            try:
                download = YouTube(self.valores.get(0))
                download = download.streams.get_by_resolution(self.valores.get(1))
                download.download('./videos')
                print(f'Download do video {self.valores.get(0)} completo')
                self.janela.close()
            except:
                print(f'Um erro ocorreu no download do video') 
        else:
            print('Saindo')
            

video = Download()
video.start()