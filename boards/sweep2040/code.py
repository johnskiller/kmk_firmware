print("Starting")

import board
import kb


from kmk.keys import KC
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.tapdance import TapDance
from kmk.modules.mouse_keys import MouseKeys
#from kmk.extensions.lcd import LCD

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

combos = Combos()
keyboard.modules.append(combos)

Di2=7 # second digit layer
FUN=6 # Function Keys
SYM=5 # Symbol Layer
MK =4 # Mouse key
NAV=3 # Navication
DIG=2 # Digits
QWERTY=1
DVORAK=0

TAB_LCTL = KC.MT(KC.TAB, KC.LCTL)
ENT_LALT = KC.MT(KC.ENT, KC.LALT)
SLSH_RSFT = KC.MT(KC.SLSH, KC.RSFT)
#ESC_GRV=KC.TD(KC.ESC,KC.TILD,KC.GRV)
NAV_SPC = KC.LT(NAV,KC.SPACE)

combos.combos = [
    Chord((KC.J, KC.K), KC.TG(MK))
]
def filte_layer(layer):
    new_lay = layer
    d=[35,23,11]
    for x in d:
        new_lay.pop(x)
    return new_lay

def filte_all(keymap):
    new_map=[]
    for layer in keymap:
        new_map.append(filte_layer(layer))
    return new_map
keymap = [
    # DVORAK 0
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Esc  |   '  |   ,  |   .  |   P  |   Y  |                    |   F  |   G  |   C  |   R  |   L  | BKSP |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | Tab  |   A  |   O  |   E  |   U  |   I  |                    |   D  |   H  |   T  |   N  |   S  |  ENT |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | Shft |   ;  |   Q  |   J  |   K  |   X  |-------.    ,-------|   B  |   M  |   W  |   V  |   Z  |   /  |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          | LALT | LGUI | /       /       \      \  |  Ctl |  Up  |
    #                          |      |      |/       /         \      \ |      |      |
    #                          `---------------------'           '------''-------------'
    #
    [
        # DVORAK
        KC.GESC,  KC.QUOT, KC.COMM, KC.DOT,  KC.P,    KC.Y,                           KC.F,    KC.G,    KC.C,    KC.R,    KC.L,    KC.BSPC, \
       TAB_LCTL,  KC.A,    KC.LT(SYM,KC.O),  KC.LT(DIG,KC.E),KC.LT(FUN,KC.U), KC.I,   KC.D,    KC.H,    KC.T,    KC.N,    KC.S,    KC.ENT, \
        KC.LSFT,  KC.SCLN, KC.Q,    KC.J,    KC.K,    KC.X,                           KC.B,    KC.M,    KC.W,    KC.V,    KC.Z,    KC.SLSH, \
                                        KC.LGUI, ENT_LALT,                          NAV_SPC, KC.BKDL,
    ],
    [  #Layer 1 QWERTY
       KC.GESC, KC.Q,   KC.W,   KC.E,   KC.R,  KC.T,                                    KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,\
       TAB_LCTL,KC.A,  KC.LT(SYM,KC.S),   KC.LT(DIG,KC.D),KC.LT(FUN,KC.F),  KC.G,       KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,\
        KC.LSFT,KC.Z,   KC.X,   KC.C,   KC.V,  KC.B,                                    KC.N,    KC.M, KC.COMM,  KC.DOT, SLSH_RSFT, KC.RSFT,\
                                     KC.LGUI,   ENT_LALT,                    NAV_SPC,   KC.BKDL,
    ],
    [   #Layer 2 Digit
        KC.GRV ,_______,_______,_______,_______,_______,                         KC.PLUS,  KC.N7,    KC.N8,    KC.N9,   KC.EQL,  KC.BSPC,\
        _______,_______,_______,XXXXXXX,KC.UNDS,_______,                         KC.MINUS, KC.N4,    KC.N5,    KC.N6,   KC.ASTR, KC.QUOT,\
        _______,_______,_______,_______,_______,_______,                         KC.N0,    KC.N1,    KC.N2,    KC.N3,   _______, KC.RSFT,\
                                        _______,_______,                        KC.DOT,   _______,
    ],
    [   #Layer 3 navication
        KC.GRV ,KC.EXLM,KC.AT,  KC.HASH,KC.DLR, KC.PERC,                         KC.HOME,KC.END ,KC.PGUP,KC.PGDN,_______,_______,\
        _______,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,                         KC.LEFT,KC.DOWN,KC.UP,  KC.RGHT,_______,_______,\
        _______,_______,_______,_______,_______,_______,                         KC.DF(1),_______,_______,_______,_______,_______,\
                                        _______,_______,                         KC.NO,   KC.DF(0),
    ],
    [   #Layer 4 Mouse key
        _______,_______,KC.MB_RMB,KC.MS_UP,KC.MB_LMB,KC.MW_UP,                   _______,KC.MB_LMB,KC.MB_MMB,KC.MB_RMB, _______,_______,\
        _______,_______,KC.MS_LT,KC.MS_DN,KC.MS_RT,KC.MW_DN,                     KC.MS_LT,KC.MS_DN,KC.MS_UP,KC.MS_RT,_______,_______,\
        _______,_______,_______,_______,_______,_______,                         _______,_______, _______, _______,_______,_______,\
                                            KC.MB_MMB,   KC.ENT,                  KC.SPACE,   KC.TG(MK),
    ],
    [   #Layer 5 Symbols
        _______,_______,_______,_______,_______,_______,                         KC.HASH,KC.LPRN, KC.RPRN, KC.LBRC,KC.RBRC,_______,\
        _______,_______,XXXXXXX,KC.EQL ,KC.EXLM,KC.TILD,                         KC.AT,  KC.LCBR, KC.RCBR, KC.BSLS,KC.QUOT,_______,\
        _______,_______,_______,_______,KC.CIRC,_______,                         KC.DLR, KC.PERC, KC.LABK, KC.RABK,KC.QUES,_______,\
                                            KC.LGUI,   KC.ENT,                  KC.SPACE,   KC.BSPC,
    ],
    [   #Layer 6 Function keys
        _______,_______,_______,_______,_______,_______,                         KC.F1  ,KC.F2  , KC.F3  , KC.F4  ,KC.F5  ,_______ ,\
        _______,_______,_______,_______,XXXXXXX,_______,                         KC.F6  ,KC.F7  , KC.F8  , KC.F9  ,KC.F10 ,_______ ,\
        _______,_______,_______,_______,_______,_______,                         KC.F11 ,KC.F12 , KC.F13 , KC.F14 ,KC.F15 ,_______ ,\
                                            KC.LGUI,   KC.LALT,                  KC.SPACE,   KC.BSPC,
    ],
    [   #Layer 7 Digit2
        _______,KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5,                           _______,_______, _______, _______,_______,_______,\
        _______,KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N0,                           _______,_______, _______, _______,_______,_______,\
        _______,_______,_______,_______,_______,_______,                         _______,_______, _______, _______,_______,_______,\
                                            KC.LGUI,   KC.ENT,                  KC.SPACE,   KC.BSPC,
    ],
    [   #Layer 8 Digit
        _______,_______,_______,_______,_______,_______,                         _______,_______, _______, _______,_______,_______,\
        _______,_______,_______,_______,_______,_______,                         _______,_______, _______, _______,_______,_______,\
        _______,_______,_______,_______,_______,_______,                         _______,_______, _______, _______,_______,_______,\
                                            KC.LGUI,   KC.ENT,                  KC.SPACE,   KC.BSPC,
    ],
]

keyboard.keymap = filte_all(keymap)

print(f'cood_mapping={keyboard.coord_mapping}')
# TODO Comment one of these on each side
#split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(split_target_left=False,split_offset=20,use_pio=True,
debug_enabled=True,)

split.data_pin=board.GP16
split.data_pin2=board.GP17

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP13,board.GP14,None),)
# Rotary Encoder (1 encoder / 1 definition per layer)
encoder_handler.map = ( ((KC.LEFT, KC.RIGHT),),) 
keyboard.modules.append(encoder_handler)
keyboard.modules.append(split)
##keyboard.encoders = [GPIOEncoder(board.GP13, board.GP14, onRotateA) ]
if __name__ == '__main__':
    keyboard.go()
