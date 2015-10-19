"""
Config has certain globals that are used throughout the program
  that may be changed with command-line arguments.
"""

class Config:
  Version = '2.1.0'
  SettingsFile = 'mochi-player.ini'
  LanguagePath = ':/translations/'

  audio_filetypes = ["*.mp3","*.ogg","*.wav","*.wma","*.m4a","*.aac","*.ac3","*.ape","*.flac","*.ra"]
  video_filetypes = ["*.avi","*.divx","*.mpg","*.mpeg","*.m1v","*.m2v","*.mpv","*.dv","*.3gp","*.mov","*.mp4","*.m4v","*.mqv","*.dat","*.vcd","*.ogm","*.ogv","*.asf","*.wmv","*.vob","*.mkv","*.ram","*.flv","*.rm","*.ts","*.rmvb","*.dvr-ms","*.m2t","*.m2ts","*.rec","*.f4v","*.hdmov","*.webm","*.vp8","*.letv","*.hlv"]
  media_filetypes = audio_filetypes + video_filetypes
  subtitle_fileypes = ["*.sub","*.srt","*.ass","*.ssa"]

  # todo: allow config changes through command-line
  def __init__(self, argv):
    # todo