import PySimpleGUI as sg
from Comandos import *

layout = [[sg.Text("Digite uma cidade ")], [sg.InputText(key="nome_cidade")], [sg.Button("Buscar"), sg.Button("fechar")], [sg.Text("", key="texto_cidade")]]
janela = sg.Window("Previsão do Tempo", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "fechar":
        break
    if evento == "Buscar":
        codigo_cidade = valores["nome_cidade"]
        res_cidade = previsao(codigo_cidade)
        janela["texto_cidade"].update(f'A Temperatura da Cidade de {codigo_cidade}{res_cidade}.')

janela.Close()