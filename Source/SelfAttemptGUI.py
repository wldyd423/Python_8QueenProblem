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

##### NOW LETS TRY MAKING SOMETHING

#Lets make a chess board
"""from PIL import Image
import io
queen = Image.open("queen2.png")
queen.thumbnail((50, 50))
bio = io.BytesIO()
queen.save(bio, format("PNG"))
img = sg.Image(data=bio.getvalue())
layout = [[sg.Text("ChessBoard")],
          [sg.Canvas(size=(400, 400), background_color='white', key='canvas')],
          [sg.Button('Quit')],
          [sg.Graph(canvas_size=(400, 400), graph_top_right=(400,400), graph_bottom_left=(0,0), key='graph')]]

window = sg.Window('ChessBoard', layout, finalize=True)
canvas = window['canvas'].TKCanvas
graph = window['graph']
graph.DrawImage(data=bio.getvalue(), location=(0, 400))
graph.BackgroundColor = 'white'
for i in range(1, 8):
    canvas.create_line(0, 400/8*i, 400, 400/8*i, fill='black')
    canvas.create_line(400/8*i, 0, 400/8*i, 400, fill='black')
while 1:
    event, values = window.read(timeout=0)
    if event == sg.WINDOW_CLOSED or event =='Quit':
        break
window.close()"""

#lets try that again
"""import io
from PIL import Image
queen = Image.open("queen2.png")
queen.thumbnail((50, 50))
bio = io.BytesIO()
queen.save(bio, format("PNG"))
layout = [[sg.Text("Chess Board")],
          [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0,0), graph_top_right=(400,400), background_color='white', key='graph')],
          [sg.Button('Quit')]]
window = sg.Window("Chess", layout, finalize=True)
graph = window['graph']

coord = []

for i in range(0, 8):
    for j in range(1, 9):
        #print(f"({50 * i},{50 * j})")
        coord.append((50*i, 50*j))

for i in range(1, 8):
    graph.DrawLine((0, 400/8*i), (400, 400/8*i))
    graph.DrawLine((400/8*i, 0), (400/8*i, 400))
for element in coord:
    graph.DrawImage(data=bio.getvalue(), location=element)
while 1:
    event, values = window.read(timeout=0)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
        
window.close()"""

#Now that kinda worked but lets do it a little better

import io
from PIL import Image
boardSize = 200

class Chessboard:
    def __init__(self, graph, data):
        self.graph = graph
        self.data = data

    def placeQueen(self, loc):#loc => 0 0 ~ 8 8
        self.graph.DrawImage(data=self.data, location=(loc[0] * boardSize/8, loc[1] * boardSize/8 + boardSize/8))

layout = [[sg.Text("Chessboard")],
          [sg.Graph(canvas_size=(boardSize, boardSize), graph_bottom_left=(0, 0), graph_top_right=(boardSize, boardSize), background_color='white', key='graph'),
          sg.Graph(canvas_size=(boardSize, boardSize), graph_bottom_left=(0, 0), graph_top_right=(boardSize, boardSize), background_color='white', key='graph2')],
          [sg.Button('Quit')]]
window = sg.Window("Chess", layout, finalize=True)
graph = window['graph']
graph2 = window['graph2']
for i in range(1, 8):
    graph.DrawLine((0, boardSize/8*i), (boardSize, boardSize/8*i))
    graph.DrawLine((boardSize/8*i, 0), (boardSize/8*i, boardSize))
    graph2.DrawLine((0, boardSize / 8 * i), (boardSize, boardSize / 8 * i))
    graph2.DrawLine((boardSize / 8 * i, 0), (boardSize / 8 * i, boardSize))

for i in range(4):
    for j in range(8):
        graph.DrawRectangle(((boardSize/4*i+boardSize/8*j)%boardSize, boardSize/8+boardSize/8*j), (boardSize/8+(boardSize/4*i+boardSize/8*j)%boardSize, boardSize/8*j), fill_color='black')
        graph2.DrawRectangle(((boardSize/4 * i + boardSize/8 * j) % boardSize, boardSize/8 + boardSize/8 * j), (boardSize/8 + (boardSize/4 * i + boardSize/8 * j) % boardSize, boardSize/8 * j),
                            fill_color='black')

img = Image.open('queen2.png')
img.thumbnail((boardSize/8, boardSize/8))
bio = io.BytesIO()
img.save(bio, format("PNG"))
chess = Chessboard(graph, bio.getvalue())
chess.placeQueen((1, 1))
chess.placeQueen((7, 7))
while 1:
    event, value = window.read(timeout=0)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
window.close()