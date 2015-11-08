'''
Input deals with mapping bindings (key/mouse/gesture) to actual
  functions in the engine.
'''

from PyQt5.Qt import Qt, QApplication, QCursor, QKeySequence, QElapsedTimer

class Input:
  class Key:
    def __init__(self):
      self.input = {}

    def press(self, event):
      # get the actual input binding
      key = self.input.get(QKeySequence(event.modifiers() | event.key()).toString())
      if key:
        # execute the attached function
        self.eval(key[0])
        event.accept()

  class Mouse:
    _timer_threshold = 10
    _gesture_threshold = 15

    class GestureHandler:
      def __init__(self, startPos):
        self.startPos = startPos
        self.action = None
        self.timer = QElapsedTimer()
        self.timer.start()
        QApplication.setOverrideCursor(QCursor(Qt.PointingHandCursor))

    def __init__(self):
      self.input = {}
      self.buttonString = {
        Qt.LeftButton: 'Left',
        Qt.RightButton: 'Right',
        Qt.MiddleButton: 'Middle',
      }
      self.gestureHandler = {
        Qt.LeftButton: None,
        Qt.RightButton: None,
        Qt.MiddleButton: None,
      }

    def press(self, event):
      self.gestureHandler[event.button()] = Input.Mouse.GestureHandler(event.globalPos())
      event.accept()

    def move(self, event):
      for button, handler in filter(lambda h: h[1], self.gestureHandler.items()):
        if handler.timer.elapsed() > self._timer_threshold:
          delta = event.globalPos() - handler.startPos
          if handler.action == None:
            if abs(delta.x()) >= abs(delta.y()) + self._gesture_threshold:
              handler.action = self.input.get('%sHDrag' % (button))
            elif abs(delta.y()) >= abs(delta.x()) + self._gesture_threshold:
              handler.action = self.input.get('%sVDrag' % (button))
            # todo: DDrag
          else:
            self.eval(action[0])(delta)

    def release(self, event):
      button = event.button()
      handler = self.gestureHandler.get(button)
      click = True
      if handler:
        click = handler.timer.elapsed() < self._timer_threshold
        handler = None
        QApplication.restoreOverrideCursor()
      if click:
        action = self.input.get('%sClick' % (self.buttonString.get(button)))
        if act:
          self.eval(action[0])
          event.accept()

    def doubleClick(self, event):
      action = self.input.get('%sDoubleClick' % (self.buttonString.get(self.button)))
      if action:
        self.eval(action[0])
        event.accept()

    def wheel(self, event):
      angle = event.angleDelta()
      action = self.input.get('Wheel%s' % ('Up' if angle.y() > 0 else 'Down'))
      self.eval(action[0])
      event.accept()

  def __init__(self, ui):
    '''
    Initialize input bindings.
    '''
    self.key, self.mouse = Input.Key(), Input.Mouse()

    # todo: cleanup/organize differently

    # (Key Binding, Mouse Binding, Attached Function, Label, Attached Action)
    defaults = [
      ('Alt+1', None, 'window.fit()', 'Fit the window to the video', ui.action_To_Current_Size),
      ('Alt+2', None, 'window.fit(50)', 'Fit window to 50%', ui.action50),
      ('Alt+3', None, 'window.fit(75)', 'Fit window to 75%', ui.action75),
      ('Alt+4', None, 'window.fit(100)', 'Fit window to 100%', ui.action100),
      ('Alt+5', None, 'window.fit(150)', 'Fit window to 150%', ui.action150),
      ('Alt+6', None, 'window.fit(200)', 'Fit window to 200%', ui.action200),
      ('Alt+Return', 'DoubleClick', 'window.fullscreen = not window.fullscreen', 'Toggle fullscreen', ui.action_Full_Screen),
      ('Ctrl++', None, 'player.sub_scale += 0.1', 'Increase sub size', ui.action_Size),
      ('Ctrl+-', None, 'player.sub_scale -= 0.1', 'Decrease sub size', ui.actionS_ize),
      ('Ctrl+D', None, 'window.dim()', 'Dim lights', ui.action_Dim_Lights),
      ('Ctrl+Down', 'WheelDown', 'player.volume -= 5', 'Decrease volume', ui.action_Decrease_Volume),
      ('Ctrl+E', None, 'window.showInFolder()', 'Show the file in its folder', ui.actionShow_in_Folder),
      ('Ctrl+F', None, 'playlist.show = not playlist.show', 'Toggle playlist visibility', ui.action_Show_Playlist),
      ('Ctrl+G', None, 'window.output = not window.output', 'Access command-line', ui.actionShow_D_ebug_Output),
      ('Ctrl+J', None, 'window.jump()', 'Show jump to time dialog', ui.action_Jump_to_Time),
      ('Ctrl+Left', None, 'playlist.prev()', 'Play previous file', ui.actionPlay_Previous_File),
      ('Ctrl+M', None, 'player.mute = not player.mute', 'Toggle mute audio', ui.action_Mute),
      ('Ctrl+N', None, 'engine.new()', 'Open a new window', ui.action_New_Player),
      ('Ctrl+O', None, 'window.open()', 'Show open file dialog', ui.action_Open_File),
      ('Ctrl+Q', None, 'qt.quit()', 'Quit', ui.actionE_xit),
      ('Ctrl+R', None, 'player.time_pos = 0', 'Restart playback', ui.action_Restart),
      ('Ctrl+Right', None, 'playlist.next()', 'Play next file', ui.actionPlay_Next_File),
      ('Ctrl+S', None, 'player.stop()', 'Stop playback', ui.action_Stop),
      ('Ctrl+Shift+Down', None, 'player.speed -= 0.1', 'Decrease playback speed by 10', ui.action_Decrease),
      ('Ctrl+Shift+R', None, 'player.speed = 1', 'Reset speed', None),
      ('Ctrl+Shift+T', None, 'player.screenshot(includes="window")', 'Take screenshot without subtitles', ui.actionWithout_Subtitles),
      ('Ctrl+Shift+Up', None, 'player.speed += 0.1', 'Increase playback speed by 10', ui.action_Increase),
      ('Ctrl+T', None, 'player.screenshot(includes="subtitles")', 'Take screenshot with subtitles', ui.actionWith_Subtitles),
      ('Ctrl+U', None, 'window.openUrl()', 'Show location dialog', ui.actionOpen_URL),
      ('Ctrl+Up', 'WheelUp', 'player.volume += 5', 'Increase volume', ui.action_Increase_Volume),
      ('Ctrl+V', None, 'player.play(qt.clipboard().text())', 'Open clipboard location', ui.actionOpen_Path_from_Clipboard),
      ('Ctrl+W', None, 'player.sub_visibility = not player.sub_visibility', 'Toggle subtitle visibility', ui.actionShow_Subtitles),
      ('Del', None, 'playlist.remove(playlist.selected)', 'Remove selected file from playlist', None),
      ('Down', None, 'playlist.selection += 1', 'Select next file on playlist', None),
      ('Esc', None, 'window.fullscreen(False) if window.isFullScreen() else window.boss()', 'Boss key', None),
      ('F1', None, 'window.onlineHelp()', 'Launch online help', ui.actionOnline_Help),
      ('Left', None, 'player.time_pos -= 5', 'Seek backwards by 5 sec', None),
      ('PgDown', None, 'player.chapter += 1', 'Go to next chapter', ui.action_Next_Chapter),
      ('PgUp', None, 'player.chapter -= 1', 'Go to previous chapter', ui.action_Previous_Chapter),
      ('Return', None, 'player.play(playlist.selected)', 'Play selected file on playlist', None),
      ('Right', None, 'player.time_pos += 5', 'Seek forwards by 5 sec', None),
      ('Shift+Left', None, 'player.frame_back_step()', 'Frame step backwards', ui.actionFrame_Back_Step),
      ('Shift+Right', None, 'player.frame_step()', 'Frame step', ui.action_Frame_Step),
      ('Space', 'RightClick', 'player.pause = not player.pause', 'Play/Pause', ui.action_Play),
      ('Tab', None, 'overlay.media_info = not overlay.media_info', 'View media information', ui.actionMedia_Info),
      ('Up', None, 'playlist.selection -= 1', 'Select previous file on playlist', None),
      (None, None, 'player.speed = 1.0', None, ui.action_Reset),
      (None, None, 'player.sub_scale = 1', None, ui.action_Reset_Size),
      (None, None, 'player.video_aspect = "16:9"', None, ui.actionForce_16_9),
      (None, None, 'player.video_aspect = "2.35:1"', None, ui.actionForce_2_35_1),
      (None, None, 'player.video_aspect = "4:3"', None, ui.actionForce_4_3),
      (None, None, 'player.video_aspect = -1', None, ui.action_Auto_Detect),
      (None, None, 'playlist.full = not playlist.full', None, ui.action_Hide_Album_Art),
      (None, None, 'playlist.repeat = Repeat.Off', None, ui.action_Off),
      (None, None, 'playlist.repeat = Repeat.Playlist', None, ui.action_Playlist),
      (None, None, 'playlist.repeat = Repeat.This', None, ui.action_This_File),
      (None, None, 'playlist.shuffle()', None, ui.actionSh_uffle),
      (None, None, 'qt.aboutQt()', None, ui.actionAbout_Qt),
      (None, None, 'update.check()', None, ui.action_Check_for_Updates),
      (None, None, 'update.youtube_dl()', None, ui.actionUpdate_Streaming_Support),
      (None, None, 'window.about()', None, ui.actionAbout_Mochi_MPlayer),
      (None, None, 'window.add_subtitle()', None, ui.action_Add_Subtitle_File),
      (None, None, 'window.preferences()', None, ui.action_Preferences),
    ]

    # todo: use a list that can be loaded from settings

    for k, m, f, l, a in defaults:
      # compile the function into python byte-code
      if f:
        f = compile(f, '<string>', 'single')
      if k:
        # register function in key input hash
        self.key.input[k] = (f, l)
      if m:
        # register function in mouse input hash
        self.mouse.input[m] = (f, l)
      if a:
        # attach the function-call to the action
        a.triggered.connect(lambda v, f = f: self.eval(f))
        if k:
          # label action with shortcut
          a.setShortcut(QKeySequence.fromString(k))
