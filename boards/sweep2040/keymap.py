
class Keyboard:
    pass

class KeyAttrDict:
    def __getattr__(self, key, depth=0):        
        if key in ['LT']:
            return self.lt
        return key
    
    def lt(self, layer, key):
        return f'[{layer},{key}]'

KC = KeyAttrDict()
keyboard = Keyboard()
FUN=7 # Function Keys
SYM=6 # Symbol Layer
MK =4 # Mouse key
NAV=3 # Navication
DIG=2 # Digits
QWERTY=1
DVORAK=0

TAB_LCTL = 'TAB_LCTL'
ENT_LALT = 'ENT_LALT'
SLSH_RSFT = 'SLSH_RSFT'
#ESC_GRV=KC.TD(KC.ESC,KC.TILD,KC.GRV)
NAV_SPC = 'NAV_SPC'
XXXXXXX = 'XXXXXXX'
_______ = '_______'
keyboard.keymap = [
    # DVORAK
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
    [  #Layer 0 QWERTY
       KC.GESC, KC.Q,   KC.W,   KC.E,   KC.R,  KC.T,                                    KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,\
       TAB_LCTL,KC.A,  KC.LT(SYM,KC.S),   KC.LT(DIG,KC.D),KC.LT(FUN,KC.F),  KC.G,       KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,\
        KC.LSFT,KC.Z,   KC.X,   KC.C,   KC.V,  KC.B,                                    KC.N,    KC.M, KC.COMM,  KC.DOT, SLSH_RSFT, KC.RSFT,\
                                     KC.LGUI,   ENT_LALT,                    NAV_SPC,   KC.BKDL,
    ],
    [   #Layer 1 Digit
        KC.GRV ,_______,_______,_______,_______,_______,                         KC.PLUS,  KC.N7,    KC.N8,    KC.N9,   KC.EQL,  KC.BSPC,\
        _______,_______,_______,XXXXXXX,KC.UNDS,_______,                         KC.MINUS, KC.N4,    KC.N5,    KC.N6,   KC.ASTR, KC.QUOT,\
        _______,_______,_______,_______,_______,_______,                         KC.N0,    KC.N1,    KC.N2,    KC.N3,   _______, KC.RSFT,\
                                        _______,_______,                        KC.DOT,   _______,
    ],
]

def filte_layer(layer):
    new_lay = layer
    d=layer[11::12]
    print(d)
    d.reverse()
    print(d)
    for x in d:
        new_lay.remove(x)
    return new_lay

def filte_all(keymap):
    new_map=[]
    for layer in keymap:
        new_map.append(filte_layer(layer))
    return new_map

def test():
    print_map(keyboard.keymap)

    print("===== after filter =====")
    nmap = filte_all(keyboard.keymap)
    print_map(nmap,kpl=11)

def print_map(keymap,kpl=12):
    for layer in keymap:
        idx = 0
        line = 0
        for key in layer:
            if idx == 6:
                print('        ', end='')
            if idx == kpl:
                line += 1
                idx = 0
                print('')
                if line == 3:
                    print('                                   ',end='')
                    idx = 4
            print(f'{key:<9}', end='')
            idx = idx + 1

        print('\n=============================================')

if __name__ == '__main__':
    test()