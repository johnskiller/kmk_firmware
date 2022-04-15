print("Starting")

import board
import kb


from kmk.keys import KC
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.tapdance import TapDance
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.lcd import LCD
#keyboard.col_pins = (board.GP0)    # try D5 on Feather, keeboar
#keyboard.row_pins = (board.GP1)    # try D6 on Feather, keeboar
#keyboard.diode_orientation = DiodeOrientation.COL2ROW

#LOWER = KC.MO(1)
#RAISE = KC.MO(2)
# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard = kb.KMKKeyboard()

# enable lcd module
# TODO add params for lcd pins
#keyboard.extensions.append(LCD())

keyboard.debug_enabled=True
keyboard.modules = [Layers(),ModTap(),TapDance(),MouseKeys()]

ESC_LCTL = KC.MT(KC.ESC, KC.LCTL)
ENT_LALT = KC.MT(KC.ENT, KC.LALT)
FUN=5 # Function Keys
SYM=4 # Symbol Layer
MK =3 # Mouse key
NAV=2 # Navication
DIG=1 # Digits

keyboard.keymap = [
    [  #Layer 0 QWERTY
        KC.TAB, KC.Q,   KC.W,   KC.E,   KC.R,  KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,\
       ESC_LCTL,KC.A,  KC.LT(SYM,KC.S),   KC.LT(1,KC.D),KC.LT(FUN,KC.F),  KC.G,        KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,\
        KC.LSFT,KC.Z,   KC.X,   KC.C,   KC.V,  KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RSFT,\
                                     KC.TD(KC.LGUI,KC.TG(MK)),   ENT_LALT,                  KC.LT(NAV,KC.SPACE),   KC.BSPC,
    ],
    [   #Layer 1 Digit
        KC.GRV ,_______,_______,_______,_______,_______,                         KC.PLUS,  KC.N7,    KC.N8,    KC.N9,   KC.EQL,  KC.BSPC,\
        _______,_______,_______,XXXXXXX,_______,_______,                         KC.MINUS, KC.N4,    KC.N5,    KC.N6,   KC.ASTR, KC.QUOT,\
        _______,_______,_______,_______,_______,_______,                         KC.N0,    KC.N1,    KC.N2,    KC.N3,   _______, KC.RSFT,\
                                            KC.LGUI,   KC.ENT,                  KC.SPACE,   KC.BSPC,
    ],
    [   #Layer 2 navication
        KC.GRV ,KC.EXLM,KC.AT,  KC.HASH,KC.DLR, KC.PERC,                         KC.HOME,KC.END ,KC.PGUP,KC.PGDN,_______,_______,\
        _______,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,                         KC.LEFT,KC.DOWN,KC.UP,  KC.RGHT,_______,_______,\
        _______,_______,_______,_______,_______,_______,                         _______,_______,_______,_______,_______,_______,\
                                            KC.LGUI,   KC.ENT,                  KC.NO,   KC.BSPC,
    ],
    [   #Layer 3 Mouse key
        _______,_______,KC.MB_RMB,KC.MS_UP,KC.MB_LMB,KC.MW_UP,                   _______,KC.MB_LMB,KC.MB_MMB,KC.MB_RMB, _______,_______,\
        _______,_______,KC.MS_LT,KC.MS_DN,KC.MS_RT,KC.MW_DN,                     _______,_______, _______, _______,_______,_______,\
        _______,_______,_______,_______,_______,_______,                         _______,_______, _______, _______,_______,_______,\
                                            KC.MB_MMB,   KC.ENT,                  KC.SPACE,   KC.TO(0),
    ],
    [   #Layer 4 Symbols
        _______,_______,_______,_______,_______,_______,                         KC.HASH,KC.LPRN, KC.RPRN, KC.LBRC,KC.RBRC,_______,\
        _______,_______,XXXXXXX,KC.EQL ,KC.EXLM,KC.TILD,                         KC.AT,  KC.LCBR, KC.RCBR, KC.BSLS,KC.QUOT,_______,\
        _______,_______,_______,_______,KC.CIRC,_______,                         KC.DLR, KC.PERC, KC.LABK, KC.RABK,KC.QUES,_______,\
                                            KC.LGUI,   KC.ENT,                  KC.SPACE,   KC.BSPC,
    ],
    [   #Layer 5 Function keys
        _______,_______,_______,_______,_______,_______,                         KC.F1  ,KC.F2  , KC.F3  , KC.F4  ,KC.F5  ,_______ ,\
        _______,_______,_______,_______,XXXXXXX,_______,                         KC.F6  ,KC.F7  , KC.F8  , KC.F9  ,KC.F10 ,_______ ,\
        _______,_______,_______,_______,_______,_______,                         KC.F11 ,KC.F12 , KC.F13 , KC.F14 ,KC.F15 ,_______ ,\
                                            KC.LGUI,   KC.ENT,                  KC.SPACE,   KC.BSPC,
    ],
    [   #Layer 1 Digit
        _______,_______,_______,_______,_______,_______,                         _______,_______, _______, _______,_______,_______,\
        _______,_______,_______,_______,_______,_______,                         _______,_______, _______, _______,_______,_______,\
        _______,_______,_______,_______,_______,_______,                         _______,_______, _______, _______,_______,_______,\
                                            KC.LGUI,   KC.ENT,                  KC.SPACE,   KC.BSPC,
    ],
]

print(f'cood_mapping={keyboard.coord_mapping}')
# TODO Comment one of these on each side
#split_side = SplitSide.LEFT
split_side = SplitSide.RIGHT
split = Split(split_side=split_side, split_target_left=False,split_offset=20,use_pio=True,
debug_enabled=True,)

split.data_pin=board.GP16

encoder_handler = EncoderHandler()
keyboard.modules.append(split)
encoder_handler.pins = ((board.GP13,board.GP14),)
# Rotary Encoder (1 encoder / 1 definition per layer)
encoder_handler.map = ( ((KC.LEFT, KC.RIGHT),),) 
##keyboard.encoders = [GPIOEncoder(board.GP13, board.GP14, onRotateA) ]
if __name__ == '__main__':
    keyboard.go()
