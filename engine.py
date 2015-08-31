from mpv import MPV
from PyQt5.Qt import QApplication, qApp
from ui.aboutdialog import AboutDialog

class Engine:
  commands = {}
  data = {}

  def command(self, args):
    if type(args) == str:
      args = args.split(' ')
    if args == []:
      return 'mochi requires arguments'
    func = self.commands.get(args.pop(0))
    if func:
      return func(args)
    else:
      return 'Command does not exist.'

  def register(self, func):
    self.commands[func.__name__] = func

mochi = Engine()

@mochi.register
def help(args):
  '''Get help on a specific command
Usage: help [command]
'''
  if args == []:
    for cmd, func in mochi.commands.items():
      print("%s\t%s" % (cmd, func.__doc__[:func.__doc__.find('\n')].strip()))
  else:
    func = mochi.commands.get(args.pop(0))
    if func:
      print(func.__doc__[func.__doc__.find('\n')+1:].strip())

@mochi.register
def mpv(args):
  '''Executes mpv command.
Usage: mpv <cmd>
'''
  if args == []:
    return 'mpv requires arguments'
  return MPV.command(args.pop(0), *args)

@mochi.register
def sh(args):
  '''Executes shell command.
Usage: sh <cmd>
'''
  from subprocess import check_output
  if args == []:
    return 'sh requires arguments'
  return check_output(args).decode()

@mochi.register
def get(args):
  '''Get the value of a property.
Usage: get [property]
'''
  if args == []:
    return 'get requires arguments'
  else:
    key = args.pop(0)
    val = engine.data.get(key)
    if not val:
      return '%s property not found' % (key)
    return '%s = %s' % (key, str(val))

@mochi.register
def set(args):
  '''Set the value of a property.
Usage: set <property> [+|-]<value>
'''
  if args == []:
    return 'set requires arguments'
  else:
    key = args.pop(0)
    val = engine.data.get(key)
    if not val:
      return '%s property not found' % (key)
    if args == []:
      return 'set requires 2 arguments'
    newVal = args.pop(0)
    if type(val) == str:
      val = newVal
    elif type(val) == int:
      if newVal.startsWith('+'):
        val += int(newVal[1:])
      elif newVal.startsWith('-'):
        val -= int(newVal[1:])
      else:
        val = int(newVal)
    elif type(val) == float:
      if newVal.startsWith('+'):
        val += float(newVal[1:])
      elif newVal.startsWith('-'):
        val -= float(newVal[1:])
      else:
        val = float(newVal)
    else:
      return 'error: unknown type'

@mochi.register
def about(args):
  '''Displays about information
Usage: about
'''
  if args == []:
    AboutDialog().exec_()
    return ''
  arg = args.pop()
  if args == []:
    if arg == 'qt':
      qApp.aboutQt()
      return ''
  else:
    return 'error: unknown arguments'

@mochi.register
def quit(args):
  '''Quits the application
Usage: quit
'''
  QApplication.quit()
  return ''
