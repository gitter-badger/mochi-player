#!/bin/python

"""
mochi-player - a mpv based media player
"""

if __name__ == '__setup__':
  # compile qt ui
  from PyQt5.uic import compileUiDir
  compileUiDir('.', True, lambda dir, mod: ('%s/moc' % (dir), mod))
  # compile qt rcs
  from subprocess import check_output
  f = open('rsclist_rc.py', 'w')
  f.write(check_output(['pyrcc5', 'rsclist.qrc']).decode())
  f.close()
  # py -> executable
  print(check_output(['pyinstaller', '-F', '-i', 'img/logo.ico', 'mochi-player.py']).decode())

if __name__ == '__main__':
  import sys
  from PyQt5.Qt import QApplication
  from engine import Engine
  
  app = QApplication(sys.argv)
  engine = Engine(sys.argv)
  sys.exit(app.exec_())
