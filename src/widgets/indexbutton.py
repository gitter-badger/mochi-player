from PyQt5.QtWidgets import QPushButton, QToolTip
from PyQt5.Qt import QPainter, QColor, QFont

class IndexButton(QPushButton):
  index = 0

  def getIndex(self):
    return self.index

  def setIndex(self, ind):
    if ind != 0:
      index = ind
      self.setMouseTracking(abs(index) >= 1000)
      self.repaint(self.rect())

  def paintEvent(self, event):
    super(IndexButton, self).paintEvent(event)
    if self.isEnabled() and self.index != 0 and abs(index) < 1000:
      region = event.rect()
      painter = QPainter(self)
      painter.setPen(QColor(0,0,0))
      painter.setFont(QFont('Noto Sans', 6))
      if index > 0:
        painter.drawText(region.adjusted(-2, -1, -2, -1), Qt.AlignCenter, str(index))
      else:
        painter.drawText(region.adjusted(2, -1, 2, -1), Qt.AlignCenter, str(index))

  def mouseMoveEvent(self, event):
    if self.isEnabled() and self.index > 0:
      QToolTip.showText(event.globalPos(), str(abs(index)), self, self.rect())
    QPushButton.mouseMoveEvent(self, event)
