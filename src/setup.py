#!/bin/python
'''
Setup - compiles the player's UI and Resource files.
'''

# compile qt ui
from PyQt5.uic import compileUiDir
compileUiDir('.', True, lambda dir, mod: ('%s/moc' % (dir), mod))
# compile qt rcs
from subprocess import check_output
f = open('rsclist_rc.py', 'w')
f.write(check_output(['pyrcc5', 'rsclist.qrc']).decode())
f.close()
# py -> executable
# print(check_output(['pyinstaller', '-F', '-i',
#                     'img/logo.ico', 'mochi-player.py']).decode())
