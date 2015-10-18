"""
Player provides an interface between the core video player engine
  and this program's engine.
"""

from mpv import MPV

class Player(MPV):
  def attach(self, win):
    """
    Attach the mpv engine to the window control.
    """
    self.window_id = win
