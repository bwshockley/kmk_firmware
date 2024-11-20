import board

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.modules.macros import Macros
from kmk.modules.tapdance import TapDance

from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

layers = Layers()
keyboard.modules.append(layers)

macros = Macros()
keyboard.modules.append(macros)

tapdance = TapDance()
tapdance.tap_time = 500
keyboard.modules.append(tapdance)

CAPS_TD = KC.TD(
  KC.RSFT,
  KC.LCAP
)

PASS = KC.MACRO("Send Me Macro!")

split = Split(
    split_flip=True,              # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,    # Defaults to UART
    uart_interval=20,             # Sets the uarts delay. Lower numbers draw more power
    use_pio=False,                # Using Helios board, UART does not require PIO.
)

keyboard.modules.append(split)

rgb = RGB(
  pixel_pin=board.GP0,
  num_pixels=63,
  val_limit=100,

)
keyboard.extensions.append(rgb)

# Cleaner key names
XXXXXXX = KC.NO
LOWER = KC.MO(1)
RAISE = KC.MO(2)

# fmt:off
keyboard.keymap = [
    [  # QWERTY
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.BSPC,
        KC.GRV,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,                                             KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.MINS,
        KC.TAB,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,                                             KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,                                             KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  CAPS_TD,
                            KC.LGUI,  KC.LBRC,  KC.RBRC,  LOWER,    KC.ENT,   KC.PSCR,  KC.MUTE,  KC.SPC,   RAISE,    KC.RCTL,  KC.RALT,  KC.DEL,
    ],
    [  #LOWER
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        KC.ESC,   KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,                                            KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,
        XXXXXXX,  KC.F11,   KC.F12,   XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.PPLS,  KC.EQL,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  KC.UP,    XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          KC.LEFT,  KC.DOWN,  KC.RIGHT, XXXXXXX,  XXXXXXX,  PASS,
                            XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
    ],
    [  #RAISE
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  KC.N7,    KC.N8,    KC.N9,    XXXXXXX,  XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  KC.N4,    KC.N5,    KC.N6,    KC.PPLS,  KC.EQL,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  KC.N1,    KC.N2,    KC.N3,    XXXXXXX,  XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  KC.N0,    KC.PDOT,  XXXXXXX,  PASS,
                            XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
    ]
]
# fmt:on

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP29, board.GP28, None, False),)
encoder_handler.map = (
    ((KC.VOLD, KC.VOLU),),  # base layer
    ((KC.VOLD, KC.VOLU),),  # Raise
    ((KC.VOLD, KC.VOLU),),  # Lower
)

keyboard.modules.append(encoder_handler)

if __name__ == '__main__':
    keyboard.go()
