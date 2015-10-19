"""
Player provides an interface between the core video player engine
  and this program's engine.
"""

from mpv import MPV
from data import Data

class Player(MPV, Data):
  def __init__(self):
    MPV.__init__(self) # todo--deal with event loop

    # todo

    Data.__init__(self)

  def attach(self, win):
    """
    Attach the mpv engine to the window control.
    """
    self.window_id = win
