#import SimpleSolutionForKColumns
#import SimpleButABetterSolution
import PySimpleGUI as sg
import ChessboardGUI as cg
import SimpleSolutionForKColumns as ssfk
import io
from PIL import Image

BoardSize = 800
k = 10

better = ssfk.KColumnChessBoard(k)
better.find_first_solution(0)
print(better.valid_solution)

img = Image.open('queen2.png')
img.thumbnail((BoardSize / k, BoardSize / k))
bio = io.BytesIO()
img.save(bio, format("PNG"))

bb = cg.KChessboardGUI(BoardSize, bio.getvalue(), k)


for element in better.valid_solution:
    bb.place_queen(element, bb.graph)
while 1:
    event, value = bb.window.read(timeout=0)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
bb.window.close()