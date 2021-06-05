import PySimpleGUI as sg
import io
from PIL import Image

BoardSize = 800


class ChessboardGUI:
    def __init__(self, boardSize, imgdata):
        self.boardSize = boardSize
        self.imgdata = imgdata

        self.layout = [[sg.Text("Chessboard")],
                       [sg.Graph(canvas_size=(boardSize, boardSize),
                                 graph_bottom_left=(0, 0),
                                 graph_top_right=(boardSize, boardSize),
                                 background_color='white', key='graph')
                        ],
                       [sg.Button('Quit')]]
        self.window = sg.Window("Chess", self.layout, finalize=True)
        self.graph = self.window['graph']
        self.make_board(self.graph)

    def make_board(self, graph):
        for i in range(1, 8):
            graph.DrawLine((0, self.boardSize / 8 * i),
                           (self.boardSize, self.boardSize / 8 * i))
            graph.DrawLine((self.boardSize / 8 * i, 0),
                           (self.boardSize / 8 * i, self.boardSize))

        for i in range(4):
            for j in range(8):
                graph.DrawRectangle(
                    ((self.boardSize / 4 * i + self.boardSize / 8 * j) % self.boardSize,
                     self.boardSize / 8 + self.boardSize / 8 * j),
                    (self.boardSize / 8 + (self.boardSize / 4 * i + self.boardSize / 8 * j) % self.boardSize,
                     self.boardSize / 8 * j),
                    fill_color='black')

    def place_queen(self, coord, graph):
        if type(coord) != tuple:
            print("Tuple type required (0,0) to (7,7)")
            return False
        if len(coord) != 2:
            print("2 valued coordinate from (0,0) to (7,7)")
            return False
        for item in coord:
            if not isinstance(item, int):
                print("Integer values (0,0) to (7,7) only")
                return False
        if coord[0] < 0 or coord[0] > self.k - 1 and coord[1] < 0 or coord[1] > self.k -1:
            print("Coordinate from (0,0) to (7,7) accepted!")
            return False

        graph.DrawImage(data=self.imgdata,
                             location=(coord[0] * self.boardSize / 8,
                                       coord[1] * self.boardSize / 8 + self.boardSize / 8))
        return True

    def clear_board(self, graph):
        self.make_board(graph)


class KChessboardGUI:
    def __init__(self, boardSize, imgdata, k):
        self.boardSize = boardSize
        self.imgdata = imgdata
        self.k = k
        self.layout = [[sg.Text("Chessboard")],
                       [sg.Graph(canvas_size=(boardSize, boardSize),
                                 graph_bottom_left=(0, 0),
                                 graph_top_right=(boardSize, boardSize),
                                 background_color='white', key='graph')
                        ],
                       [sg.Button('Quit')]]
        self.window = sg.Window("Chess", self.layout, finalize=True)
        self.graph = self.window['graph']
        self.make_board(self.graph)

    def make_board(self, graph):
        if self.k % 2 == 0:
            for i in range(self.k // 2):
                for j in range(self.k):
                    graph.DrawRectangle(
                        ((self.boardSize / self.k * 2 * i + self.boardSize / self.k * j) % self.boardSize,
                         self.boardSize / self.k + self.boardSize / self.k * j),
                        (self.boardSize / self.k + (
                                    self.boardSize / self.k * 2 * i + self.boardSize / self.k * j) % self.boardSize,
                         self.boardSize / self.k * j),
                        fill_color='black')
        else:
            for i in range(self.k // 2 + 1):
                for j in range(self.k):
                    graph.DrawRectangle(
                        ((self.boardSize / self.k * 2 * i + self.boardSize / self.k * j) % self.boardSize,
                         self.boardSize / self.k + self.boardSize / self.k * j),
                        (self.boardSize / self.k + (
                                    self.boardSize / self.k * 2 * i + self.boardSize / self.k * j) % self.boardSize,
                         self.boardSize / self.k * j),
                        fill_color='black')


    def place_queen(self, coord, graph):
        if type(coord) != tuple:
            print(f"Tuple type required (0,0) to ({self.k - 1},{self.k - 1})")
            return False
        if len(coord) != 2:
            print(f"2 valued coordinate from (0,0) to ({self.k - 1},{self.k - 1})")
            return False
        for item in coord:
            if not isinstance(item, int):
                print(f"Integer values (0,0) to ({self.k - 1},{self.k - 1}) only")
                return False
        if coord[0] < 0 or coord[0] > self.k - 1 and coord[1] < 0 or coord[1] > self.k - 1:
            print(f"Coordinate from (0,0) to ({self.k - 1},{self.k - 1}) accepted!")
            return False

        graph.DrawImage(data=self.imgdata,
                             location=(coord[0] * self.boardSize / self.k,
                                       coord[1] * self.boardSize / self.k + self.boardSize / self.k))
        return True

    def clear_board(self, graph):
        self.make_board(graph)




###
###TEST CODE PART
###

"""k = 20
img = Image.open('queen2.png')
img.thumbnail((BoardSize / k, BoardSize / k))
bio = io.BytesIO()
img.save(bio, format("PNG"))

bb = KChessboardGUI(BoardSize, bio.getvalue(), k)

bb.place_queen((0, 0), bb.graph)
while 1:
    event, value = bb.window.read(timeout=0)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
bb.window.close()"""

# TODO be able to add new chessboards and be able to organize them add queens to chessboard you want
