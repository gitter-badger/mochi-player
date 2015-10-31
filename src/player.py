'''
Player provides an interface between the core video player engine
  and this program's engine.
'''

import locale
from mpv import MPV

class Player(MPV):
  def __init__(self, wid):
    locale.setlocale(locale.LC_NUMERIC, 'C') # reset locale to C for mpv
    MPV.__init__(self, wid=int(wid)) # todo--deal with event loop

  def play(self, f):
    if f:
      MPV.play(self, f)

  def stop(self):
    '''
    Stop playback.
    '''
    self.time_pos = self.time_start
    self.pause = True
