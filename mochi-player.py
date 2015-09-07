import sys

from PyQt5.Qt import QApplication
from ui.mainwindow import MainWindow

if __name__ == '__main__':
  app = QApplication(sys.argv)

  window = MainWindow()
  window.show()

  if len(app.arguments()) > 1:
    window.Load(app.arguments().end())
  else:
    window.Load()
  res = app.exec_()
  window.Save()
  sys.exit(res)
