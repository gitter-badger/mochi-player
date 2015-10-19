"""
Engine is the main controller of the player. It initalizes everything
  and facilitates communication between the models and views.
"""

import json, copy

from config import Config
from ui.mainwindow import MainWindow
from player import Player
from input import Input
from overlay import Overlay
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
    self.window = MainWindow()
    self.player = Player()
    self.input = Input()
    self.overlay = Overlay()
    self.translator = Translator()
    self.remote = Remote()
    self.update = Update()

    # create a data tree of all modules' members for easy load/save
    self.data = {k: v.__dict__ for k, v in self.__dict__.items() }

    # connect everything
    self.player.attach(self.window.ui.MpvFrame.winId())
    self.translator.register_translate_callback(window.retranslate)
    # todo

    self.load(Config.SettingsFile)

  def __del__(self):
    self.save(Config.SettingsFile)

  # todo: make sure these work
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
