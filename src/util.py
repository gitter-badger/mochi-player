'''
Util holds general useful functions re-used throughout the program.
'''

import sys, re

class Util:
  def canUpdateStreamingSupport():
    return (sys.platform == 'win32')

  def isValidFile(path):
    '''
    Check to see if this is a valid file.
    '''
    if sys.platform == 'linux2':
      return re.match(r'^^\\.{1,2}|/', path, re.IGNORECASE)
    elif sys.platform == 'win32':
      return re.match(r'^(\\.{1,2}|[a-z]:|\\\\\\\\)', re.IGNORECASE)
    return False

  def isValidLocation(path):
    '''
    Check to see if this is a valid location.
    '''
    if sys.platform == 'linux2':
      return re.match(r'^([a-z]{2,}://|\\.{1,2}|/)', path, re.IGNORECASE)
    elif sys.platform == 'win32':
      return re.match(r'^([a-z]{2,}://|\\.{1,2}|[a-z]:|\\\\\\\\)', re.IGNORECASE)
    return False
