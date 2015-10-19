"""
Overlay provides a way of overlaying data onto the video canvas for
  status messages or other purposes.
"""

from PyQt5.Qt import QThread, QTimer, \
  QImage, QPoint, QColor, \
  QPainter, QPainterPath, \
  QPen, QBrush, \
  QFontMetrics, QFont, \
  QFileInfo, QLabel

from data import Data
from config import Config

class Overlay:
  _min_overlay, _max_overlay = 1, 60
  _info_overlay, _status_overlay = 62, 63
  _refresh_rate = 1000
  _fm_correction = 1.3

  def __init__(self):
    self._overlay = self._min_overlay
    self._overlays = {}
    self._timer = None

  def showStatusText(self, text, duration = 4000):
    """
    Shows simple overlay status text for a specified duration.
    """
    if text != str() and duration != 0:
      self.showText(
        text,
        QFont(Config.MonospaceFont, 14, QFont.Bold),
        QColor(0xffffff),
        QPoint(20, 20),
        duration,
        self._status_overlay)
    else:
      self._remove(self._status_overlay)

  def showInfoText(self, show = True):
    """
    Shows the media-info overlay.
    """
    if show:
      if self._timer:
        self._timer = QTimer()
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self.showInfoText)
      self._timer.start(self._refresh_rate)
      self.showText(
        self.mediaInfo,
        QFont(Config.MonospaceFont, 14, QFont.Bold),
        QColor(0xffff00),
        QPoint(20, 20),
        0,
        self._info_overlay)
    else:
      del self._timer
      self._timer = None
      self._remove(self._info_overlay)

  def showText(self, text, font, color, pos, duration, id = -1):
    """
    Handles putting specific overlays on the different mpv
      provided overlay areas or uses a Qt label.
    """
    if id == -1:
      id = (self._overlay % self._max_overlay) + self._min_overlay

    fm = QFontMetrics(font)
    lines = text.split('\n')
    h = fm.height() * lines.length()
    w = max(map(lambda l: fm.width(l), lines))
    xF = (self.mpvFrameWidth - 2 * pos.x()) / (self._fm_correction * w)
    yF = (self.mpvFrameHeight - 2 * pos.y()) / h
    font.setPointSizeF(min(font.pointSizeF() * min(xF, yF), font.pointSizeF()))

    fm = QFontMetrics(font)
    h, w = fm.height(), 0
    path = QPainterPath(QPoint(0, 0))
    p = QPoint(0, h)
    for line in lines:
      path.addText(p, font, line)
      w = max(int(self._fm_correction * path.currentPosition().x()), w)
      p += QPoint(0, h)

    canvas = QImage(w, p.y(), QImage.Format_ARGB32)
    canvas.fill(QColor(0, 0, 0, 0))

    painter = QPainter(canvas)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setCompositionMode(QPainter.ComposititionMode_Overlay)
    painter.setFont(font)
    painter.setPen(QColor(0, 0, 0))
    painter.setBrush(color)
    painter.drawPath(path)

    self.mpv.add_overlay(
      self._overlay if id == -1 else id,
      pos.x(), pos.y(),
      '&%d' % (quintptr(canvas.bits())),
      0, canvas.width(), canvas.height())

    label = QLabel(self.mpvFrame)
    label.setStyleSheet('background-color:rgb(0,0,0,0);background-image:url();')
    label.setGeometry(pos.x(), pos.y(), canvas.width(), canvas.height())
    label.setPixmap(QPixmap.fromImage(canvas))
    label.show()

    if duration == 0:
      timer = None
    else:
      timer = QTimer()
      timer.start(duration)
      timer.timeout.connect(lambda: self._remove(id))

    overlay = self._overlays.get(id)
    if overlay:
      del overlay
    self._overlays[id] = (label, canvas, timer)

  def _remove(self, id):
    """
    Removes an overlay from both mpv and the list of overlays
    """
    self.mpv.remove_overlay(id)
    overlay = self._overlays.get(id)
    if overlay:
      del overlay
