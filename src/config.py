'''
Config has certain globals that are used throughout the program
  that may be changed with command-line arguments.
'''

class Config:
  version = '2.1.0'
  settingsFile = 'mochi-player.ini'
  languagePath = ':/translations/'
  remoteListen = '0.0.0.0:8474'
  onlineHelpUrl = 'http://mochi-player.github.io/help.html'
  monospaceFont = 'Courier New'
  audioFiletypes = ['*.mp3','*.ogg','*.wav','*.wma','*.m4a','*.aac','*.ac3','*.ape','*.flac','*.ra','*.mka']
  videoFiletypes = ['*.avi','*.divx','*.mpg','*.mpeg','*.m1v','*.m2v','*.mpv','*.dv','*.3gp','*.mov','*.mp4','*.m4v','*.mqv','*.dat','*.vcd','*.ogm','*.ogv','*.asf','*.wmv','*.vob','*.mkv','*.ram','*.flv','*.rm','*.ts','*.rmvb','*.dvr-ms','*.m2t','*.m2ts','*.rec','*.f4v','*.hdmov','*.webm','*.vp8','*.letv','*.hlv']
  mediaFiletypes = audioFiletypes + videoFiletypes
  subtitleFileypes = ['*.sub','*.srt','*.ass','*.ssa']
  help = False
  verbose = False
  script = True # are we a python script, or a wrapped executable?

  def __init__(self, argv):
    '''
    Allows config overriding with any arg in argv like so:
    mochi-player --SettingsFile=/tmp/mochi-player.ini
    '''
    self.__dict__.update({k[2:]:v for k,v in map(lambda s: s.split('='), filter(lambda s: s.startswith('--'), argv))})
