"""
Player provides an interface between the core video player engine
  and this program's engine.
"""

from mpv import MPV

class Player(MPV):
  def __init__(self, viewport):
    super().__init__(window_id=viewport)
