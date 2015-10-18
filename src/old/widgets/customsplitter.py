from PyQt5.QtWidgets import QSplitter
from PyQt5.Qt import pyqtSignal
from math import fsum

class CustomSplitter(QSplitter):
  normalPos = 0

  positionChanged = pyqtSignal(int)

  def __init__(self, parent):
    super(CustomSplitter, self).__init__(parent)
    self.splitterMoved.connect(
      lambda pos, index: \
        index == 1 and \
        self.positionChanged.emit(self.max() - pos))

  def position(self):
    return self.sizes()[1]

  def normalPosition(self):
    return self.normalPos

  def max(self):
    return int(fsum(self.sizes()))

  def setPosition(self, pos):
    self.setSizes([self.max() - pos, pos])
    self.positionChanged.emit(pos)

  def setNormalPosition(self, pos):
    normalPos = pos