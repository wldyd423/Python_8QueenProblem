import PySimpleGUI as sg

#Tutorial Code 1
"""layout = [[sg.Text("What's your name?")],
          [sg.Input()],
          [sg.Button('Ok')]]

window = sg.Window("Window Title", layout)

event, values = window.read()
print('Hello', values[0], "! Thanks for trying PySimpleGUI")
window.close()"""
#End of Tutorial Code 1


#Tutorial Code 2
layout = [[sg.Text("What's your name?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('OK'), sg.Button('QUIT')]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'QUIT':
        break
    window['-OUTPUT-'].update('Hello '+values['-INPUT-'] + "! Thanks for trying PySimpleGUI !",
                              text_color='yellow')

window.close()
#End of Tutorial Code 2