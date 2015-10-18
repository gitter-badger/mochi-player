import enum

from PyQt5.Qt import QCoreApplication
import mpv
from data import Data
from type import PlayState, VideoParams, AudioParams

class Mpv:
  def __init__(self):
    self.data = Data({
      'state': -1, # PlayState.Idle
      'file': str(),
      'path': str(),
      'vo': str(),
      'ao': str(),
      'metadata': {},
      'video_params': {},
      'audio_params': {},
      'tracks': [],
      'chapters': [],
    })
    self.data.bind({
      'state': self.ChangeState,
      'file': lambda f: self.Command('loadfile %s' % (f)),
      'vo': lambda s: self.SetOption('vo', s),
      'ao': lambda s: self.SetOption('ao', s),
    })

    mpv_data = Data({
      'media_title': str(),
      'speed': 1.0,
      'playback-time': 0,
      'length': 0,
      'volume': 100,
      'mute': False,
      'sub-visibility': True,
      'vid': int(),
      'aid': int(),
      'sid': int(),
      'screenshot_template': str(),
    })
    mpv_bind = {}
    for k, v in mpv_data.items():
      mpv_bind[k] = lambda _v: mpv.MPV._set_property(k, v)
    self.data.update(mpv_data)
    self.data.bind(mpv_bind)

    mpv_formats = {
      mpv.MpvFormat.DOUBLE: float,
      mpv.MpvFormat.STRING: str,
      mpv.MpvFormat.INT64: int,
      mpv.MpvFormat.FLAG: bool,
    }

    self.events = {
      mpv.MpvEventID.PROPERTY_CHANGE: lambda data: self.data.__setitem__(data.name, mpv_formats[data.format](data.data)),
      mpv.MpvEventID.IDLE: lambda data: self.data.__setitem__('state', PlayState.Idle),
      mpv.MpvEventID.START_FILE: lambda data: self.data.__setitem__('state', PlayState.Loaded),
      mpv.MpvEventID.FILE_LOADED: lambda data: self.data.__setitem__('state', PlayState.Started),
      mpv.MpvEventID.UNPAUSE: lambda data: self.data.__setitem__('state', PlayState.Playing),
      mpv.MpvEventID.PAUSE: lambda data: self.data.__setitem__('state', PlayState.Paused),
      mpv.MpvEventID.END_FILE: lambda data: self.data.__setitem__('state', PlayState.Stopped),
      mpv.MpvEventID.SHUTDOWN: lambda data: QCoreApplication.quit(),
      # MPV_EVENT_LOG_MESSAGE data: lambda: ,
    }

  def handle_event(self, event):
    # todo: get mpv's actual events to be sent to this
    handler = self.events.get(event.event_id)
    if handler:
      handler(event.data)

  def ChangeState(self, state):
    if state == PlayState.Play:
      self.Set('pause', 1)
    if state == PlayState.Pause:
      self.Set('pause', 0)
    elif state == PlayState.Stop:
      self.Set('pause', 1)
      self.Set('time', 0)

  def Command(self, cmd):
    # todo: send command to mpv
    print('[mpv]: %s' % (cmd))
