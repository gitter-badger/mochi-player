from PyQt5.QtWidgets import QLabel
from PyQt5.Qt import Qt, pyqtSignal

class CustomLabel(QLabel):
  clicked = pyqtSignal()

  def mousePressEvent(self, event):
    if self.isEnabled() and event.button() == Qt.LeftButton:
      self.clicked.emit()
      event.accept()
    super(CustomLabel, self).mousePressEvent(event)
