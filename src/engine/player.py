'''
Player provides an interface between the core video player engine
  and this program's engine.
'''

import locale
from mpv import MPV
from .data import Data

# todo: deal with before mpv is initialized with values


class Player(MPV, Data):
    data = ['volume']
    def __init__(self, wid):
        locale.setlocale(locale.LC_NUMERIC, 'C')  # reset locale to C for mpv
        MPV.__init__(self, wid=int(wid))

    def play(self, f):
        if f:
            MPV.play(self, f)

    def stop(self):
        self.time_pos = self.time_start
        self.pause = True
