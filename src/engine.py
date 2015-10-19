"""
Engine is the main controller of the player. It initalizes everything
  and facilitates communication between the models and views.
"""

import json, copy

from PyQt5.Qt import QApplication
from data import Data
from config import Config
from ui.mainwindow import MainWindow
from player import Player
from input import Input
from overlay import Overlay
from translator import Translator
from remote import Remote
from update import Update

class Engine(QApplication, Data):
  def __init__(self, argv):
    """
    Creates all components
      argv: command-line arguments
    """
    QApplication.__init__(self, argv)
    config = Config(argv)

    # initialize everything
    self.window = MainWindow()
    self.player = Player()
    self.input = Input()
    self.overlay = Overlay()
    self.translator = Translator()
    self.remote = Remote()
    self.update = Update()

    Data.__init__(self)

    # connect everything
    self.player.attach(self.window.ui.MpvFrame.winId())
    self.translator.register_translate_callback(window.retranslate)
    # todo

  # todo: make sure these work
  def load(self, file):
    try:
      f = open(file, 'r')
      super(Data, self).update(json.load(f))
      f.close()
    except:
      return False
    return True

  def save(self, file):
    try:
      f = open(file, 'w')
      d = copy.deepcopy(dict(self))
      for k, v in self.__default__.items():
        if d[k] == v:
          d.pop(k)
      json.dump(d, f, indent=4, sort_keys=True)
      f.close()
    except:
      return False
    return True
