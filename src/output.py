'''
Output provides a qt wrapper for stdout/stderr to redirect to the gui.
'''
import sys
from PyQt5.QtCore import QObject, pyqtSignal

class Output(QObject):
  written = pyqtSignal(object, object)

  class Stream(QObject):
    written = pyqtSignal(object, object)

    def __init__(self, parent, stream):
      QObject.__init__(self, parent)
      self._stream = stream

    def write(self, text):
      # self._stream.write(text)
      self.written.emit(text, self._stream)

    def __getattr__(self, name):
      return getattr(self._stream, name)

  def __init__(self, parent=None):
    QObject.__init__(self, parent)
    self._stdout = Output.Stream(self, sys.stdout)
    sys.stdout = self._stdout
    self._stderr = Output.Stream(self, sys.stderr)
    sys.stderr = self._stderr
    self._stdout.written.connect(self.written)
    self._stderr.written.connect(self.written)

  def __del__(self):
    try:
      sys.stdout = self._stdout._stream
      sys.stderr = self._stderr._stream
    except AttributeError:
      pass
