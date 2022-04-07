print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.native_keypad_scanner import keys_scanner
from kmk.modules.encoder import EncoderHandler

#keyboard.col_pins = (board.GP0)    # try D5 on Feather, keeboar
#keyboard.row_pins = (board.GP1)    # try D6 on Feather, keeboar
#keyboard.diode_orientation = DiodeOrientation.COL2ROW



_KEY_CFG = [
        [board.GP0,board.GP1,board.GP2,board.GP3]
        ]

class Keyboard2040(KMKKeyboard):
    def __init__(self):
        self.matrix = keys_scanner(_KEY_CFG)

keyboard = Keyboard2040()
keyboard.keymap = [
    [KC.A,KC.B,KC.C,KC.D]
]
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]
encoder_handler.pins = ((board.GP13,board.GP14,board.GP15),)
# Rotary Encoder (1 encoder / 1 definition per layer)
encoder_handler.map = ( ((KC.LEFT, KC.RIGHT, KC.Z),),) 
##keyboard.encoders = [GPIOEncoder(board.GP13, board.GP14, onRotateA) ]
if __name__ == '__main__':
    keyboard.go()
