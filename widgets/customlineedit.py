from PyQt5.QtWidgets import QLineEdit
from PyQt5.Qt import Qt, pyqtSignal

class CustomLineEdit(QLineEdit):
  submitted = pyqtSignal('QString')

  def keyPressEvent(self, event):
    if event.key() == Qt.Key_Return:
      self.submitted.emit(self.text())
      event.accept()
    super(CustomLineEdit, self).keyPressEvent(event)