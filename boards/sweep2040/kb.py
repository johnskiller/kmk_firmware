import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.native_keypad_scanner import keys_scanner

_KEY_CFG = [
        [board.GP0,board.GP1,board.GP2,board.GP3,]
        ]

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        self.matrix = keys_scanner(_KEY_CFG)
