from PyQt5.QtWidgets import QPushButton
from PyQt5.Qt import Qt, pyqtSignal

class OpenButton(QPushButton):
  LeftClick = pyqtSignal()
  MiddleClick = pyqtSignal()
  RightClick = pyqtSignal()

  def mousePressEvent(self, event):
    if event.button() == Qt.LeftButton:
      self.LeftClick.emit()
    elif event.button() == Qt.MiddleButton:
      self.MiddleClick.emit()
    elif event.button == Qt.RightButton:
      self.RightClick.emit()
    event.accept()
    # QPushButton.mousePressEvent(self, event)
