'''
Util holds general useful functions re-used throughout the program.
'''

import sys, re, os
from PyQt5.Qt import QDesktopServices, QUrl

class Util:
  def canUpdateStreamingSupport():
    return (sys.platform == 'win32')

  def isValidFile(path):
    '''
    Check to see if this is a valid file.
    '''
    if sys.platform == 'linux':
      return re.match(r'^^\\.{1,2}|/', path, re.IGNORECASE)
    elif sys.platform == 'win32':
      return re.match(r'^(\\.{1,2}|[a-z]:|\\\\\\\\)', re.IGNORECASE)
    return False

  def isValidLocation(path):
    '''
    Check to see if this is a valid location.
    '''
    if sys.platform == 'linux':
      return re.match(r'^([a-z]{2,}://|\\.{1,2}|/)', path, re.IGNORECASE)
    elif sys.platform == 'win32':
      return re.match(r'^([a-z]{2,}://|\\.{1,2}|[a-z]:|\\\\\\\\)', re.IGNORECASE)
    return False

  def showInFolder(path):
    '''
    Show the file in file manager.
    '''
    if sys.platform == 'linux':
      QDesktopServices.openUrl(QUrl('file:///%s' % (os.path.dirname(path))))
    elif sys.platform == 'win32':
      QProcess.startDetached('explorer.exe', ['/select,', path])
