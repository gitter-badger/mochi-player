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
from remote import Remote
from update import Update

class Engine(QApplication):
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

    # connect everything
    self.player.attach(self.window.ui.MpvFrame.winId())
    self.translator.register_translate_callback(window.retranslate)
    # todo

    # load settings
    self.data = Data(self.__dict__)
