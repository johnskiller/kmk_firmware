import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.native_keypad_scanner import keys_scanner

_KEY_CFG = [
           [#board.GP10,
            board.GP4, board.GP3,  board.GP0, board.GP1,  board.GP2,
            #board.GP8,
            board.GP5, board.GP28, board.GP7, board.GP6,  board.GP27,
            #board.GP12,
            board.GP26,board.GP22, board.GP21,board.GP20, board.GP19,
                                                          board.GP15, board.GP18
            ]
        ]

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        self.matrix = keys_scanner(_KEY_CFG)
        '''
        index of key_map
         0  1  2  3  4  5    6  7  8  9 10
        11 12 13 14 15 16   17 18 19 20 21
        22 23 24 25 26 27   28 29 30 31 32
                    33 34   35 36
        '''
        '''
        self.matrix.coord_mapping = [
           #0  1  2  3  4  5  6 . 7 . 8 . 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 
            0, 1, 2, 3, 4, 5,                   6, 7, 8, 9,10,11,               12,13,14,15,16,17,               18,19
        ]
        '''
        self.matrix.coord_mapping = [
             0, 1, 2, 3, 4, 5,     24,23,22,21,20,
             6, 7, 8, 9,10,11,     29,28,27,26,25,
            12,13,14,15,16,17,     34,33,32,31,30,
                        18,19,     36,35,
        ] 
