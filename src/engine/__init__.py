'''
Engine is the main controller of the player. It initalizes everything
  and facilitates communication between the models and views.
'''

from PyQt5.Qt import QApplication, QProcess
from ui.mainwindow import MainWindow
from .data import Data
from .config import Config
from .player import Player
from .input import Input
from .overlay import Overlay
from .playlist import Playlist
from .translator import Translator
from .remote import Remote
from .update import Update

class Engine(Data):
    data = ['window', 'player', 'input', 'overlay', 'playlist', 'remote', 'update', 'translator']

    def __init__(self, argv):
        ''' Creates all components
          argv: command-line arguments '''
        # initialize everything
        qt = QApplication(argv)

        self.window = MainWindow()
        self.player = Player(self.window.ui.mpvFrame.winId())
        self.input = Input(self.window.ui)
        self.overlay = Overlay()
        self.playlist = Playlist()
        self.remote = Remote()
        self.update = Update()
        self.translator = Translator()

        self.save_init()

        # volatile initialization
        self.config = Config(argv)
        self.qt = qt
        self.quit = qt.quit
        self.window.ui.consoleWidget.pushVariables(vars(self))

        # connect everything
        # window
        self.window.config = self.config
        self.window.input = self.input
        self.window.playlist = self.playlist
        self.window.eval = self.eval
        self.window.overlay = self.overlay
        self.window.player = self.player
        # player
        # input
        self.input.eval = self.eval
        self.input.config = self.config
        # overlay
        self.overlay.config = self.config
        self.overlay.mpvFrame = self.window.ui.mpvFrame
        self.overlay.player = self.player
        # playlist
        self.playlist.player = self.player
        # translator
        self.translator.register_translate_callback(
            self.window.ui.retranslateUi)

    def exec_(self):
        ''' Main program loop. '''
        self.load(self.config.settingsFile)
        res = self.qt.exec_()
        self.save(self.config.settingsFile)
        return res

    def eval(self, s):
        ''' Safely evaluate a python statement in the scope of the engine class. '''
        try:
            exec(s, self.exec_scope)
        except Exception as e:
            print('Error in engine.eval(%s): %s' % (s, e))

    def new(self):
        ''' Create new instance of application. '''
        if self.config.script:
            # find main script filename
            import __main__
            args = [__main__.__file__]
        else:
            args = []
        QProcess.startDetached(QApplication.applicationFilePath(), args)
