NAME = "NeCalculator "

# TypeName
COMMON = ": COMMON"
SCIENTIFIC = ": SCIENTIFIC"
PROGRAMMER = ": PROGRAMMER"
PLOTTING = ": PLOTTING"
NAMES = [
    COMMON,
    SCIENTIFIC,
    PROGRAMMER,
    PLOTTING
]
# Signs
PI = '\u03C0'
DOT = '.'
PLUS = '+'
MINUS = '-'
SUB = '/'
MUL = "*"
POW = '**'
EQ = '='

CHARS = [
    PLUS,
    MINUS,
    SUB,
    MUL,
    POW,
    EQ
]

GEOMETRY = '400x500'

ICON_PATH = '../Resources/calculator.ico'
BACKGROUND_COLOR = "#171717"
BORDER_WIDTH = 10

SCIENTIFIC_BTN_PARAMS = {'bd': 5, 'fg': '#BBB', 'bg': '#3C3636', 'font': ('sans-serif', 20, 'bold')}
NUMBER_BTN_PARAMS = {'bd': 5, 'fg': '#000', 'bg': '#BBB', 'font': ('sans-serif', 20, 'bold')}
DELETE_BTN_PARAMS = {'bd': 5, 'fg': '#000', 'bg': '#db701f', 'font': ('sans-serif', 20, 'bold')}
MEMORY_BTN_PARAMS = {'bd': 5, 'fg': '#000', 'bg': '#db701f', 'font': ('sans-serif', 20, 'bold')}
CELLS_BTN_PARAMS = {'bd': 5, 'fg': '#000', 'bg': '#db701f', 'font': ('sans-serif', 15, 'bold')}
PLOTTING_BTN_PARAMS = {'bd': 5, 'fg': '#000', 'bg': '#48e520', 'font': ('sans-serif', 15, 'bold')}
CLEAR_BTN_PARAMS = {'bd': 5, 'fg': '#000', 'bg': '#db701f', 'font': ('sans-serif', 15, 'bold')}

MAX_MEMORY_CELLS = 4

DIR_DATA_PATH = '../Resources/Saved/'
SCIENTIFIC_DATA_PATH = DIR_DATA_PATH + 'Data.txt'
PLOT_DATA_PATH = DIR_DATA_PATH + '/Plot.txt'

NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ACCUARY = 50