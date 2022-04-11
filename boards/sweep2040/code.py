print("Starting")

import board
import kb


from kmk.keys import KC
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.encoder import EncoderHandler

#keyboard.col_pins = (board.GP0)    # try D5 on Feather, keeboar
#keyboard.row_pins = (board.GP1)    # try D6 on Feather, keeboar
#keyboard.diode_orientation = DiodeOrientation.COL2ROW



keyboard = kb.KMKKeyboard()
keyboard.debug_enabled=True
keyboard.keymap = [
    [KC.A,KC.S,KC.D,KC.F, KC.J,KC.K,KC.L,KC.SCOLON]
]

print(f'cood_mapping={keyboard.coord_mapping}')
# TODO Comment one of these on each side
#split_side = SplitSide.LEFT
split_side = SplitSide.RIGHT
split = Split(split_type=SplitType.ONEWIRE,split_side=split_side,
split_target_left=False,split_offset=5,
debug_enabled=True,)

split.data_pin=board.GP17

encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler,split]
encoder_handler.pins = ((board.GP13,board.GP14,board.GP15),)
# Rotary Encoder (1 encoder / 1 definition per layer)
encoder_handler.map = ( ((KC.LEFT, KC.RIGHT, KC.Z),),) 
##keyboard.encoders = [GPIOEncoder(board.GP13, board.GP14, onRotateA) ]
if __name__ == '__main__':
    keyboard.go()
