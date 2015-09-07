from PyQt5.uic import compileUiDir
compileUiDir('.', True, lambda dir, mod: ('%s/moc' % (dir), mod))

from subprocess import check_output
f = open('rsclist_rc.py', 'w')
f.write(check_output(['pyrcc5', 'rsclist.qrc']).decode())
f.close()

print(check_output(['pyinstaller', '-F', '-i', 'img/logo.ico', 'mochi-player.py']).decode())