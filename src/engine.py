"""
Engine is the main controller of the player. It initalizes everything
  and facilitates communication between the models and views.
"""

import json, copy, locale

from PyQt5.Qt import QApplication
from config import Config
from ui.mainwindow import MainWindow
from player import Player
from input import Input
from overlay import Overlay
from playlist import Playlist
from translator import Translator
from remote import Remote
from update import Update

class Engine:
  def __init__(self, argv):
    """
    Creates all components
      argv: command-line arguments
    """
    # initialize everything
    qt = QApplication(argv)
    locale.setlocale(locale.LC_NUMERIC, 'C') # reset locale to C for mpv

    self.window = MainWindow()
    self.player = Player()
    self.input = Input()
    self.overlay = Overlay()
    self.playlist = Playlist()
    self.remote = Remote()
    self.update = Update()
    self.translator = Translator()

    # create a data tree of all modules' members for easy load/save
    self.data = {k: v.__dict__ for k, v in self.__dict__.items() }

    # volatile initialization
    self.config = Config(argv)
    self.qt = qt
    self.engine = self
    self.exec_scope = {k: v for k, v in self.__dict__.items() }

    # connect everything
    # window
    self.window.config = self.config
    self.window.input = self.input
    self.window.playlist = self.playlist
    self.window.exec_scope = self.exec_scope
    # player
    self.player.attach(self.window.ui.mpvFrame.winId())
    # input
    # overlay
    self.overlay.config = self.config
    # playlist
    self.playlist.player = self.player
    # translator
    self.translator.register_translate_callback(self.window.retranslate)

    self.load(self.config.settingsFile)

  def __del__(self):
    self.save(self.config.settingsFile)

  def exec_(self):
    return self.qt.exec_()

  def load(self, file):
    try:
      f = open(file, 'r')
      self.data.update(json.load(f))
      f.close()
    except:
      return False
    return True

  def save(self, file):
    try:
      f = open(file, 'w')
      d = copy.deepcopy(dict(self.data))
      for k, v in self.data.items():
        if d[k] == v:
          d.pop(k)
      json.dump(d, f, indent=2, sort_keys=True)
      f.close()
    except:
      return False
    return True

  def new(self):
    """
    Create new instance of application.
    """
    pass
