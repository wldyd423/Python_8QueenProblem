import PySimpleGUI as sg
###
###This is unrelated to main project. I am only testing PySimpleGUI out because I want to use it
###as the GUI to present solutions for my 8 Queen problem AI
###

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
"""layout = [[sg.Text("What's your name?")],
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

window.close()"""
#End of Tutorial Code 2


#Tutorial Code 3
"""window = sg.Window('Columns')
col = [[sg.Text('col Row1')],
       [sg.Text('col Row2'), sg.Input('col input 1')],
       [sg.Text('col Row3'), sg.Input('col input 2')],
       [sg.Text('col Row4'), sg.Input('col input 3')],
       [sg.Text('col Row5'), sg.Input('col input 4')],
       [sg.Text('col Row6'), sg.Input('col input 5')],
       [sg.Text('col Row7'), sg.Input('col input 6')]]

layout = [[sg.Slider(range=(1, 100), default_value=10, orientation='v', size=(8,20)), sg.Column(col)],
          [sg.In('Last input')],
          [sg.OK()]]
window = sg.Window('Compact 1-line window with column', layout)
event, values = window.read()
window.close()
sg.Popup(event, values, line_width=200)"""
#End of Tutorial Code 3


#Tutorial Code 4
###
###Bases structure is copied form this code: https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Pong.py

"""import math
import random

class Ball:
    def __init__(self, canvas, color, theta):
        self.canvas = canvas
        self.id = self.canvas.create_oval(10, 10, 35, 35, fill=color)
        self.canvas.move(self.id, 327, 220)
        self.x = 0
        self.y = 0
        self.dir = 4

        self.theta = theta

        self.col0 = False
        self.col1 = False
        self.col2 = False
        self.col3 = False




    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        self.x = self.dir*math.cos(self.theta)
        self.y = self.dir*math.sin(self.theta)
        #self.dir *= 1.01

        if pos[0] < 0 and pos[1] < 0:
            print("Corner pos0 pos1")
            self.theta = math.pi/4
            self.col0 = True
            self.col1 = True
            self.col2 = False
            self.col3 = False
        elif pos[0] < 0 and pos[3] >= self.canvas.winfo_height():
            print("Corner pos0 pos3")
            self.theta = 2*math.pi - math.pi/4
            self.col0 = True
            self.col1 = False
            self.col2 = False
            self.col3 = True
        elif pos[1] < 0 and pos[2] >= self.canvas.winfo_width():
            print("Corner pos1 pos2")
            self.theta = math.pi - math.pi/4
            self.col0 = False
            self.col1 = True
            self.col2 = True
            self.col3 = False
        elif pos[2] >= self.canvas.winfo_width() and pos[3] >= self.canvas.winfo_height():
            print("Corner pos2 pos3")
            self.theta = math.pi + math.pi/4
            self.col0 = False
            self.col1 = False
            self.col2 = True
            self.col3 = True

        elif self.col0 == False and pos[0] < 0:
            self.theta = math.pi - self.theta
            if self.theta < 0:
                self.theta += 2*math.pi
            self.theta = self.theta % (2 * math.pi)
            self.col0 = True
            self.col1 = False
            self.col2 = False
            self.col3 = False

        elif self.col1 == False and pos[1] < 0:
            self.theta = 2*math.pi - self.theta
            if self.theta < 0:
                self.theta += 2*math.pi
            self.theta = self.theta % (2*math.pi)
            self.col0 = False
            self.col1 = True
            self.col2 = False
            self.col3 = False

        elif self.col2 == False and pos[2] >= self.canvas.winfo_width():
            self.theta = math.pi - self.theta
            if self.theta < 0:
                self.theta += 2*math.pi
            self.theta = self.theta % (2 * math.pi)
            self.col0 = False
            self.col1 = False
            self.col2 = True
            self.col3 = False

        elif self.col3 == False and pos[3] >= self.canvas.winfo_height():
            self.theta = 2*math.pi - self.theta
            if self.theta < 0:
                self.theta += 2*math.pi
            self.theta = self.theta % (2*math.pi)
            self.col0 = False
            self.col1 = False
            self.col2 = False
            self.col3 = True





        #print(pos)



layout = [[sg.Canvas(size=(700, 400), background_color='black', key='canvas')],
          [sg.T('Some Text:')],
          [sg.Text('Is this different?')],
          [sg.Button('hi')],
          [sg.Button('bye')]]
window = sg.Window('Canvas test', layout, finalize=True)


canvas = window['canvas'].TKCanvas
canvas.create_line(350, 0, 350, 400, fill='white')

dot = Ball(canvas, 'white', random.random() * 2*math.pi)
dot2 = Ball(canvas, 'blue', random.random() * 2*math.pi)
dot3 = Ball(canvas, 'green', random.random() * 2*math.pi)
dot4 = Ball(canvas, 'red', random.random() * 2*math.pi)
dot5 = Ball(canvas, 'yellow', random.random() * 2*math.pi)
dot6 = Ball(canvas, 'purple', random.random() * 2*math.pi)
dot7 = Ball(canvas, 'orange', random.random() * 2*math.pi)

while 1:
    dot.draw()
    dot2.draw()
    dot3.draw()
    dot4.draw()
    dot5.draw()
    dot6.draw()
    dot7.draw()
    event, values = window.read(timeout=0)
    if event == sg.WINDOW_CLOSED or event == 'bye':
        break
    canvas.after(10)
window.close()
"""
#Made this simple program to test canvas. Maybe use it for more interesting projects
#Maybe add collision between balls? or even magnetic interaction?
#End of Tutorial Code 4