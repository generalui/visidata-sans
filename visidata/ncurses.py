# Mock curses functionality for development and testing

# Constants for attributes
A_NORMAL = 0
A_BOLD = 1 << 1
A_REVERSE = 1 << 2
A_UNDERLINE = 1 << 3
A_BLINK = 1 << 4
A_DIM = 1 << 5

# Constants for colors
COLOR_BLACK = 0
COLOR_RED = 1
COLOR_GREEN = 2
COLOR_YELLOW = 3
COLOR_BLUE = 4
COLOR_MAGENTA = 5
COLOR_CYAN = 6
COLOR_WHITE = 7

# Error class
class error(Exception):
    pass

class Window:
    def __init__(self, height=24, width=80):
        self.height = height
        self.width = width
        self.cursor_y = 0
        self.cursor_x = 0
        print("Window.__init__")
        # Initialize screen buffer as 2D array of (char, attr) tuples
        self.buffer = [[(' ', A_NORMAL) for x in range(width)] for y in range(height)]
        self._keypad = False
        self._nodelay = False

    def getmaxyx(self):
        print("Window.getmaxyx")
        return self.height, self.width

    def getyx(self):
        print("Window.getyx")
        return self.cursor_y, self.cursor_x

    def move(self, y, x):
        print("Window.move")
        if 0 <= y < self.height and 0 <= x < self.width:
            self.cursor_y = y
            self.cursor_x = x
        else:
            raise error("move position out of bounds")

    def addstr(self, y, x, string, attr=A_NORMAL):
        print("Window.addstr")
        if y < 0 or x < 0:
            raise error("negative coordinates")
        
        try:
            for i, ch in enumerate(string):
                if x + i >= self.width:
                    break
                if y < self.height:
                    self.buffer[y][x + i] = (ch, attr)
        except IndexError:
            raise error("write outside window")

    def addch(self, y, x, ch, attr=A_NORMAL):
        print("Window.addch")
        if y < 0 or x < 0:
            raise error("negative coordinates")
            
        try:
            if y < self.height and x < self.width:
                self.buffer[y][x] = (ch, attr)
        except IndexError:
            raise error("write outside window")

    def clear(self):
        print("Window.clear")
        self.buffer = [[((' ', A_NORMAL)) for x in range(self.width)] for y in range(self.height)]

    def refresh(self):
        # In a real implementation, this would update the screen
        print("Window.refresh")

    def clrtoeol(self):
        print("Window.clrtoeol")
        if 0 <= self.cursor_y < self.height:
            for x in range(self.cursor_x, self.width):
                self.buffer[self.cursor_y][x] = (' ', A_NORMAL)

    def keypad(self, flag):
        """Enable/disable keypad mode"""
        self._keypad = flag
        return None

    def nodelay(self, flag):
        """Enable/disable no-delay mode"""
        self._nodelay = flag
        return None

    def getch(self):
        """Mock getting a character from input"""
        # In a real implementation, this would get actual input
        # For now, just return a dummy value
        return -1

# Color pair management
_color_pairs = {}
_next_pair = 1

def init_pair(n, fg, bg):
    print("init_pair")
    global _color_pairs
    if n < 1:
        raise error("Color pair numbers must be positive")
    _color_pairs[n] = (fg, bg)

def color_pair(n):
    print("color_pair")
    if n not in _color_pairs:
        raise error("Color pair not initialized")
    return n << 8

def initscr():
    return Window()

def endwin():
    print("endwin")

def start_color():
    print("start_color")

def use_default_colors():
    print("use_default_colors")

def curs_set(visibility):
    # 0: invisible, 1: normal, 2: very visible
    print("curs_set")

def can_change_color():
    print("can_change_color")
    return True

def init_color(color_number, r, g, b):
    print("init_color")

# Keyboard constants
KEY_RESIZE = 410
KEY_UP = 259
KEY_DOWN = 258
KEY_LEFT = 260
KEY_RIGHT = 261
KEY_HOME = 262
KEY_END = 360
KEY_NPAGE = 338  # Page down
KEY_PPAGE = 339  # Page up
KEY_ENTER = 343
KEY_BACKSPACE = 263

# Add these functions to the existing ncurses.py file

def use_env(flag):
    """Mock curses.use_env() which tells curses to use/ignore environment variables"""
    print("use_env")

def noecho():
    """Mock curses.noecho() which turns off automatic echoing of input"""
    print("noecho")

def cbreak():
    """Mock curses.cbreak() which enters cbreak mode (no line buffering)"""
    print("cbreak")

def raw():
    """Mock curses.raw() which enters raw mode (no input processing)"""
    print("raw")

def meta(flag):
    """Mock curses.meta() which enables/disables high-bit input"""
    print("meta")

def keypad(flag):
    """Mock curses.keypad() which enables/disables keypad mode"""
    print("keypad")

def halfdelay(tenths):
    """Mock curses.halfdelay() which sets half-delay mode"""
    print("halfdelay")

def nocbreak():
    """Mock curses.nocbreak() which leaves cbreak mode"""
    print("nocbreak")

def echo():
    """Mock curses.echo() which turns on echo mode"""
    print("echo")

def nl():
    """Mock curses.nl() which enables newline translation"""
    print("nl")

def nonl():
    """Mock curses.nonl() which disables newline translation"""
    pass

def def_prog_mode():
    """Save the current terminal mode as the 'program' mode"""
    print("def_prog_mode")

def reset_prog_mode():
    """Reset the terminal mode to the 'program' mode"""
    print("reset_prog_mode")

def def_shell_mode():
    """Save the current terminal mode as the 'shell' mode"""
    print("def_shell_mode")

def reset_shell_mode():
    """Reset the terminal mode to the 'shell' mode"""
    print("reset_shell_mode")