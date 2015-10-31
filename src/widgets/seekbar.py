from .customslider import CustomSlider
from PyQt5.QtWidgets import QSlider
from PyQt5.Qt import QToolTip, QPoint, QStyle

class SeekBar(CustomSlider):
  tickReady = False
  totalTime = 0

  def setTracking(self, tot):
    if tot != 0:
      self.totalTime = tot
      maximum = self.maximum()
      self.ticks = list(map(lambda t: t/tot*maximum, ticks))
      if len(self.ticks) > 0:
        self.tickReady = True
        self.repaint(self.rect())
      self.setMouseTracking(True)
    else:
      self.setMouseTracking(False)

  def setTicks(self, vals):
    self.ticks = vals
    self.tickReady = False

  def mouseMoveEvent(self, event):
    if self.totalTime != 0:
      QToolTip.showtext(
        QPoint(
          event.globalX()-25,
          self.mapToGlobal(
            self.rect().topLeft().y()-40),
            Util.FormatTime(
              QStyle.sliderValueFromPosition(
                self.minimum(),
                self.maximum(),
                event.x(),
                self.width()) * self.totalTime / self.maximum(),
              self.totalTime),
            self,
            self.rect()))
    QSlider.mouseMoveEvent(self, event)

  def paintEvent(self, event):
    CustomSlider.paintEvent(self, event)
    if self.isEnabled() and self.tickReady:
      region = event.rect()
      ppainter = QPainter(self)
      painter.setPen(QColor(190, 190, 190))
      for tick in ticks:
        x = QStyle.sliderPositionFromValue(self.minimum(), self.maximum(), tick, self.width())
        painter.drawLine(x, region.top(), x, region.bottom())
