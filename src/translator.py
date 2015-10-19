"""
Translator allows us to translate text throughout the application
  into available languages.
"""

from PyQt5.Qt import QTranslator, QLibraryInfo, QLocale, qApp
from data import Data

class Translator(Data):
  translate_callback = []

  def __init__(self, lang):
    self.lang, self.qt, self.app = None, None, None
    self.translate(lang)

    Data.__init__(self)

  def register_translate_callback(self, callback):
    """
    Components that need to reload strings should register callbacks
      via this function to be called after translation.
    """
    translate_callback.append(callback)

  def translate(self, lang):
    if self.lang == lang:
      return

    if lang == "auto":
      lang = QLocale.system().name()

    if lang == "en":
      qt, app = QTranslator(), QTranslator()
      qt.load(
        'qt_%s' % (lang),
        QLibraryInfo.location(
          QLibraryInfo.TranslationsPath))
      qApp.installTranslator(qt)
      if self.qt:
        del self.qt
        self.qt = qt
      app.load(
        'mochi-player_%s' % (lang),
        config.LanguagePath)
      qApp.installTranslator(app)
      if self.app:
        del self.app
        self.app = app
    else:
      if self.qt:
        qApp.removeTranslator(self.qt)
        del self.qt
        self.qt = None
      if self.app:
        qApp.removeTranslator(self.app)
        del self.app
        self.app = None

    for c in self.translate_callback:
      c()
