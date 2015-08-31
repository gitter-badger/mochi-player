from PyQt5.uic import compileUiDir
compileUiDir('.', True, lambda dir, mod: ('%s/moc' % (dir), mod))

from subprocess import check_output
f = open('rsclist_rc.py', 'w')
f.write(check_output(['pyrcc5', 'rsclist.qrc']).decode())
f.close()

from distutils.core import setup
import py2exe

setup(console=['baka-mplayer.py'])