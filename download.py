from pytube import YouTube, exceptions
import PySimpleGUI as sg
import time


class Download(object):
    
    def __init__(self):
        self.__url = ''
    

    def start(self):

        layout = [
            [sg.Text('Link do Video: ', size=(40,0))],
            [sg.Input(), sg.Button('Baixar')],
            [sg.Text('Qualidade', size=(40,0))],
            [sg.InputCombo(('720p', '480p', '360p', '240p', '144p'), size=(20, 1))],
            [sg.Text('Diretorio para salvar o video', size=(40,0))],
            [sg.InputText('Videos'), sg.FolderBrowse()],
            [sg.Output(size=(50,10))],
            [sg.Exit()],
        ]

        self.janela = sg.Window('Baixar Videos', layout=layout)
            
        self._download()

    def _download(self):
        while True:
            self.evento, self.valores = self.janela.Read()

            if self.evento == 'Baixar':
                if self.valores.get(1) == '':
                    self.valores[1] = '360p' 
                try:
                    download = YouTube(self.valores.get(0))
                    download = download.streams.get_by_resolution(self.valores.get(1))
                    download.download(self.valores.get(2))
                    print(f'Download do video {download.title} completo')
                except exceptions.ExtractError:
                    print('URL invalido!')
                except  :
                    print(f'Um erro ocorreu no download do video')
            elif self.evento == sg.WIN_CLOSED or self.evento == 'Sair':
                break
            else:
                print('Saindo')
                self.janela.close()
            
            
            
        
video = Download()
video.start()