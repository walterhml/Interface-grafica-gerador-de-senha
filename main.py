import PySimpleGUI as sg
import random

layout = [  [sg.Text('primary inteface grafica!') ],
            [sg.Text('veja um input: '), sg.InputText()],
            [sg.Button('ok'), sg.Button('Cancel')] ]

window = sg.Window('Gerenciador de Tarefas', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
