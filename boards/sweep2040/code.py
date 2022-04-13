print("Starting")

import board
import kb


from kmk.keys import KC
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.encoder import EncoderHandler

#keyboard.col_pins = (board.GP0)    # try D5 on Feather, keeboar
#keyboard.row_pins = (board.GP1)    # try D6 on Feather, keeboar
#keyboard.diode_orientation = DiodeOrientation.COL2ROW

#LOWER = KC.MO(1)
#RAISE = KC.MO(2)

keyboard = kb.KMKKeyboard()
keyboard.debug_enabled=True
keyboard.keymap = [
    [  #QWERTY
        KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,\
        KC.LCTL,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,\
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RSFT,\
                                            KC.LGUI,   KC.SPACE,                  KC.ENT,   KC.BSPC,
    ],
]

print(f'cood_mapping={keyboard.coord_mapping}')
# TODO Comment one of these on each side
#split_side = SplitSide.LEFT
split_side = SplitSide.RIGHT
split = Split(split_type=SplitType.ONEWIRE,split_side=split_side,
split_target_left=False,split_offset=20,
debug_enabled=True,)

split.data_pin=board.GP17

encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler,split]
encoder_handler.pins = ((board.GP13,board.GP14,board.GP9),)
# Rotary Encoder (1 encoder / 1 definition per layer)
encoder_handler.map = ( ((KC.LEFT, KC.RIGHT, KC.Z),),) 
##keyboard.encoders = [GPIOEncoder(board.GP13, board.GP14, onRotateA) ]
if __name__ == '__main__':
    keyboard.go()
