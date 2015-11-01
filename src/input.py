'''
Input deals with mapping bindings (key/mouse/gesture) to actual
  functions in the engine.
'''

from PyQt5.Qt import QKeySequence

# todo: get this to work properly

class Input:
  class KeyInput:
    def __init__(self, parent):
      self.input = parent

    def press(self, event):
      # get the actual input binding
      key = self.input.get(QKeySequence(event.modifiers() | event.key()).toString())
      if key:
        # execute the attached function
        exec(key[0], self.input.exec_scope)
        event.accept()

  class MouseInput:
    def __init__(self, parent):
      self.input = parent

    def press(self, event):
      pass
    def release(self, event):
      pass
    def move(self, event):
      pass
    def wheel(self, event):
      pass

  def __init__(self):
    self.input = {k: (compile(cmd, '<string>', 'single'), label) for k, cmd, label in [
      ('Ctrl++', 'player.sub_scale += 0.1', 'Increase sub size'),
      ('Ctrl+-', 'player.sub_scale -= 0.1', 'Decrease sub size'),
      ('Ctrl+W', 'player.sub_visibility = not player.sub_visibility', 'Toggle subtitle visibility'),
      ('Ctrl+R', 'player.time_pos = 0', 'Restart playback'),
      ('PgDown', 'player.chapter += 1', 'Go to next chapter'),
      ('PgUp', 'player.chapter -= 1', 'Go to previous chapter'),
      ('Right', 'player.time_pos += 5', 'Seek forwards by %d sec' % (5)),
      ('Left', 'player.time_pos -= 5', 'Seek backwards by %d sec' % (5)),
      ('Shift+Right', 'player.frame_step()', 'Frame step'),
      ('Shift+Left', 'player.frame_back_step()', 'Frame step backwards'),
      ('Ctrl+M', 'player.mute = not player.mute', 'Toggle mute audio'),
      ('Ctrl+T', 'player.screenshot(includes="subtitles")', 'Take screenshot with subtitles'),
      ('Ctrl+Shift+T', 'player.screenshot(includes="window")', 'Take screenshot without subtitles'),
      ('Ctrl+Down', 'player.volume -= 5', 'Decrease volume'),
      ('Ctrl+Up', 'player.volume += 5', 'Increase volume'),
      ('Ctrl+Shift+Up', 'player.speed += 0.1', 'Increase playback speed by %d' % (10)),
      ('Ctrl+Shift+Down', 'player.speed -= 0.1', 'Decrease playback speed by %d' % (10)),
      ('Ctrl+Shift+R', 'player.speed = 1', 'Reset speed'),
      ('Alt+Return', 'window.fullscreen = not window.fullscreen', 'Toggle fullscreen'),
      ('Ctrl+D', 'window.dim()', 'Dim lights'),
      ('Ctrl+E', 'window.showInFolder()', 'Show the file in its folder'),
      ('Tab', 'overlay.media_info = not overlay.media_info', 'View media information'),
      ('Ctrl+J', 'window.jump()', 'Show jump to time dialog'),
      ('Ctrl+N', 'engine.new()', 'Open a new window'),
      ('Ctrl+O', 'window.open()', 'Show open file dialog'),
      ('Ctrl+Q', 'qt.quit()', 'Quit'),
      ('Ctrl+Right', 'playlist.next()', 'Play next file'),
      ('Ctrl+Left', 'playlist.prev()', 'Play previous file'),
      ('Ctrl+S', 'player.stop()', 'Stop playback'),
      ('Ctrl+U', 'window.openUrl()', 'Show location dialog'),
      ('Ctrl+V', 'player.play(qt.clipboard().text())', 'Open clipboard location'),
      ('Ctrl+F', 'playlist.show = not playlist.show', 'Toggle playlist visibility'),
      # ('Ctrl+Z', '', 'Open the last played file'),
      ('Ctrl+G', 'window.output = not window.output', 'Access command-line'),
      ('F1', 'window.onlineHelp()', 'Launch online help'),
      ('Space', 'player.pause = not player.pause', 'Play/Pause'),
      ('Alt+1', 'window.fit()', 'Fit the window to the video'),
      ('Alt+2', 'window.fit(50)', 'Fit window to %d%%' % (50)),
      ('Alt+3', 'window.fit(75)', 'Fit window to %d%%' % (75)),
      ('Alt+4', 'window.fit(100)', 'Fit window to %d%%' % (100)),
      ('Alt+5', 'window.fit(150)', 'Fit window to %d%%' % (150)),
      ('Alt+6', 'window.fit(200)', 'Fit window to %d%%' % (200)),
      ('Esc', 'window.fullscreen(False) if window.isFullScreen() else window.boss()', 'Boss key'),
      ('Down', 'playlist.selection += 1', 'Select next file on playlist'),
      ('Up', 'playlist.selection -= 1', 'Select previous file on playlist'),
      ('Return', 'player.play(playlist.selected)', 'Play selected file on playlist'),
      ('Del', 'playlist.remove(playlist.selected)', 'Remove selected file from playlist'),
    ]}

    self.key, self.mouse = Input.KeyInput(self.input), Input.MouseInput(self.input)
