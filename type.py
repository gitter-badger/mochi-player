from enum import Enum

audio_filetypes = ["*.mp3","*.ogg","*.wav","*.wma","*.m4a","*.aac","*.ac3","*.ape","*.flac","*.ra"]
video_filetypes = ["*.avi","*.divx","*.mpg","*.mpeg","*.m1v","*.m2v","*.mpv","*.dv","*.3gp","*.mov","*.mp4","*.m4v","*.mqv","*.dat","*.vcd","*.ogm","*.ogv","*.asf","*.wmv","*.vob","*.mkv","*.ram","*.flv","*.rm","*.ts","*.rmvb","*.dvr-ms","*.m2t","*.m2ts","*.rec","*.f4v","*.hdmov","*.webm","*.vp8","*.letv","*.hlv"]
media_filetypes = audio_filetypes + video_filetypes
subtitle_fileypes = ["*.sub","*.srt","*.ass","*.ssa"]

class PlayState(Enum):
  Stopped = -2
  Idle = -1
  Started = 1
  Loaded = 2
  Play = 3
  Playing = 4
  Pause = 5
  Paused = 6

class Chapter:
  title = str()
  time = int()

class Track:
  id = int()
  type = str()
  src_id = int()
  title = str()
  lang = str()
  albumart = bool()
  default = bool()
  external = bool()
  external_filename = str()
  codec = str()

  def __eq__(self, t):
    return self.id == t.id

class VideoParams:
  codec = str()
  width = 0
  height = 0
  dwidth = 0
  dheight = 0
  aspect = 0

class AudioParams:
  codec = str()
  samplerate = str()
  channels = str()

class FileInfo:
  media_title = str()
  length = int()
  metadata = {}
  video_params = VideoParams()
  audio_params = AudioParams()
  tracks = []
  chapters = []
