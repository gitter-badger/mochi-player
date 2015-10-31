from PyQt5.QtWidgets import QSlider
from PyQt5.Qt import Qt, QStyle

class CustomSlider(QSlider):
  def setValueNoSignal(self, val):
    self.blockSignals(True)
    self.setValue(val)
    self.blockSignals(False)

  def mousePressEvent(self, event):
    if event.button() == Qt.LeftButton:
      self.setValue(QStyle.sliderValueFromPosition(
        self.minimum(),
        self.maximum(),
        event.x(),
        self.width()))
      event.accept()
    QSlider.mousePressEvent(self, event)
