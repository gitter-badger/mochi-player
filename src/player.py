"""
Player provides an interface between the core video player engine
  and this program's engine.
"""

import locale
from mpv import MPV

class Player(MPV):
  def __init__(self):
    locale.setlocale(locale.LC_NUMERIC, 'C') # reset locale to C for mpv
    MPV.__init__(self) # todo--deal with event loop
    locale.setlocale(locale.LC_NUMERIC, '')
    # todo

  def attach(self, win):
    """
    Attach the mpv engine to the window control.
    """
    self.window_id = win

  def stop(self):
    """
    Stop playback.
    """
    self.time_pos = self.time_start
    self.pause = True
