from data import Data

class Input:
  def __init__(self):
    self.data = Data({
      'Ctrl++': {
        'cmd': 'mpv add sub-scale +0.1',
        'label': 'Increase sub size',
      },
      'Ctrl+-': {
        'cmd': 'mpv add sub-scale -0.1',
        'label': 'Decrease sub size',
      },
      'Ctrl+W': {
        'cmd': 'mpv cycle sub-visibility',
        'label': 'Toggle subtitle visibility',
      },
      'Ctrl+R': {
        'cmd': 'mpv set time-pos 0',
        'label': 'Restart playback',
      },
      'PgDown': {
        'cmd': 'mpv add chapter +1',
        'label': 'Go to next chapter',
      },
      'PgUp': {
        'cmd': 'mpv add chapter -1',
        'label': 'Go to previous chapter',
      },
      'Right': {
        'cmd': 'mpv seek +5',
        'label': 'Seek forwards by %d sec' % (5),
      },
      'Left': {
        'cmd': 'mpv seek -5',
        'label': 'Seek backwards by %d sec' % (5),
      },
      'Shift+Left': {
        'cmd': 'mpv frame_back_step',
        'label': 'Frame step backwards',
      },
      'Shift+Right': {
        'cmd': 'mpv frame_step',
        'label': 'Frame step',
      },
      'Ctrl+M': {
        'cmd': 'mute',
        'label': 'Toggle mute audio',
      },
      'Ctrl+T': {
        'cmd': 'screenshot subtitles',
        'label': 'Take screenshot with subtitles',
      },
      'Ctrl+Shift+T': {
        'cmd': 'screenshot',
        'label': 'Take screenshot without subtitles',
      },
      'Ctrl+Down': {
        'cmd': 'volume -5',
        'label': 'Decrease volume',
      },
      'Ctrl+Up': {
        'cmd': 'volume +5',
        'label': 'Increase volume',
      },
      'Ctrl+Shift+Up': {
        'cmd': 'speed +0.1',
        'label': 'Increase playback speed by %d' % (10),
      },
      'Ctrl+Shift+Down': {
        'cmd': 'speed -0.1',
        'label': 'Decrease playback speed by %d' % (10),
      },
      'Ctrl+Shift+R': {
        'cmd': 'speed 1.0',
        'label': 'Reset speed',
      },
      'Alt+Return': {
        'cmd': 'fullscreen',
        'label': 'Toggle fullscreen',
      },
      'Ctrl+D': {
        'cmd': 'dim',
        'label': 'Dim lights',
      },
      'Ctrl+E': {
        'cmd': 'show_in_folder',
        'label': 'Show the file in its folder',
      },
      'Tab': {
        'cmd': 'media_info',
        'label': 'View media information',
      },
      'Ctrl+J': {
        'cmd': 'jump',
        'label': 'Show jump to time dialog',
      },
      'Ctrl+N': {
        'cmd': 'new',
        'label': 'Open a new window',
      },
      'Ctrl+O': {
        'cmd': 'open',
        'label': 'Show open file dialog',
      },
      'Ctrl+Q': {
        'cmd': 'quit',
        'label': 'Quit',
      },
      'Ctrl+Right': {
        'cmd': 'playlist play +1',
        'label': 'Play next file',
      },
      'Ctrl+Left': {
        'cmd': 'playlist play -1',
        'label': 'Play previous file',
      },
      'Ctrl+S': {
        'cmd': 'stop',
        'label': 'Stop playback',
      },
      'Ctrl+U': {
        'cmd': 'open_location',
        'label': 'Show location dialog',
      },
      'Ctrl+V': {
        'cmd': 'open_clipboard',
        'label': 'Open clipboard location',
      },
      'Ctrl+F': {
        'cmd': 'playlist toggle',
        'label': 'Toggle playlist visibility',
      },
      'Ctrl+Z': {
        'cmd': 'open_recent 0',
        'label': 'Open the last played file',
      },
      'Ctrl+G': {
        'cmd': 'output',
        'label': 'Access command-line',
      },
      'F1': {
        'cmd': 'online_help',
        'label': 'Launch online help',
      },
      'Space': {
        'cmd': 'play_pause',
        'label': 'Play/Pause',
      },
      'Alt+1': {
        'cmd': 'fitwindow',
        'label': 'Fit the window to the video',
      },
      'Alt+2': {
        'cmd': 'fitwindow 50',
        'label': 'Fit window to %d%%' % (50),
      },
      'Alt+3': {
        'cmd': 'fitwindow 75',
        'label': 'Fit window to %d%%' % (75),
      },
      'Alt+4': {
        'cmd': 'fitwindow 100',
        'label': 'Fit window to %d%%' % (100),
      },
      'Alt+5': {
        'cmd': 'fitwindow 150',
        'label': 'Fit window to %d%%' % (150),
      },
      'Alt+6': {
        'cmd': 'fitwindow 200',
        'label': 'Fit window to %d%%' % (200),
      },
      'Esc': {
        'cmd': 'boss',
        'label': 'Boss key',
      },
      'Down': {
        'cmd': 'playlist select +1',
        'label': 'Select next file on playlist',
      },
      'Up': {
        'cmd': 'playlist select -1',
        'label': 'Select previous file on playlist',
      },
      'Return': {
        'cmd': 'playlist play',
        'label': 'Play selected file on playlist',
      },
      'Del': {
        'cmd': 'playlist remove',
        'label': 'Remove selected file from playlist',
      }
    })
