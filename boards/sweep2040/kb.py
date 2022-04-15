import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner

_KEY_CFG = [board.GP10, board.GP4, board.GP3,  board.GP0, board.GP1,  board.GP2,
            board.GP8,  board.GP5, board.GP28, board.GP7, board.GP6,  board.GP27,
            board.GP12, board.GP26,board.GP22, board.GP21,board.GP20, board.GP19,
                                                          board.GP15, board.GP18
            ]

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        self.matrix = KeysScanner(_KEY_CFG)

        self.matrix.coord_mapping = [
             0, 1, 2, 3, 4, 5,     25,24,23,22,21,20,
             6, 7, 8, 9,10,11,     31,30,29,28,27,26,
            12,13,14,15,16,17,     37,36,35,34,33,32,
                        18,19,     39,38,
        ] 
