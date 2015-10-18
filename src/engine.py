"""
Engine is the main controller of the player. It initalizes everything
  and facilitates communication between the models and views.
"""

from PyQt5.Qt import QApplication
from data import Data
from config import Config
from ui.mainwindow import MainWindow
from player import Player
from input import Input
from overlay import Overlay
from translator import Translator

class Engine(QApplication, Data):
  def __init__(self, argv):
    """
    Creates all components
      argv: command-line arguments
    """
    QApplication.__init__(self, argv)
    config = Config(argv)

    self.window = MainWindow()
    self.player = Player()
    self.input = Input()
    self.overlay = Overlay()
    self.translator = Translator()
    self.remote = Remote()
    self.update = Update()

    Data.__init__(self, config)
