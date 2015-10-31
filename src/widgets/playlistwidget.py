from PyQt5.QtWidgets import QListWidget
from PyQt5.Qt import Qt

class PlaylistWidget(QListWidget):
  def __init__(self, parent):
    QListWidget.__init__(self, parent)
    self.setAttribute(Qt.WA_NoMousePropagation)
