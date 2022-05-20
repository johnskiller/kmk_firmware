import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.encoder import RotaryioEncoder

_KEY_CFG = [board.GP10, board.GP4, board.GP3,  board.GP0, board.GP1,  board.GP2,
            board.GP8,  board.GP5, board.GP28, board.GP7, board.GP6,  board.GP27,
            board.GP12, board.GP26,board.GP22, board.GP21,board.GP20, board.GP19,
                                                          board.GP15, board.GP18
            ]


def six_col_map():
    return [
             0, 1, 2, 3, 4, 5,     25,24,23,22,21,20,
             6, 7, 8, 9,10,11,     31,30,29,28,27,26,
            12,13,14,15,16,17,     37,36,35,34,33,32,
                        18,19,     39,38,
        ]
def five_col_map():
    return [
             0, 1, 2, 3, 4, 5,     27,26,25,24,23,
             6, 7, 8, 9,10,11,     32,31,30,29,28,
            12,13,14,15,16,17,     37,36,35,34,33,
                        18,19,     39,38,
                     20,21,22,     41,40, 
        ]
class KMKKeyboard(_KMKKeyboard):
    def __init__(self,col=5):
        if col == 5:
            for x in [board.GP10,board.GP8,board.GP12]:
                _KEY_CFG.remove(x)
        else:
            _KEY_CFG.append(board.GP9)  # add encoder button to matrix
        self.matrix = [KeysScanner(_KEY_CFG), RotaryioEncoder(board.GP13,board.GP14)]

        self.coord_mapping = five_col_map()