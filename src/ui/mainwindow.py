from enum import Enum

from PyQt5.Qt import QTextCursor, QKeySequence
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from .moc.mainwindow import Ui_MainWindow

from util import Util
from .aboutdialog import AboutDialog
from .locationdialog import LocationDialog

class OnTop(Enum):
  Never=0
  Always=1
  Playing=2

class MainWindow(QMainWindow):
  ui = Ui_MainWindow()
  overlay = None

  def __init__(self):
    QMainWindow.__init__(self)
    self.ui.setupUi(self)
    self.ui.actionUpdate_Streaming_Support.setEnabled(Util.canUpdateStreamingSupport())
    self.addActions(self.ui.menubar.actions())
    self.ui.mpvFrame.installEventFilter(self)
    self.ui.mpvFrame.setMouseTracking(True)
    # todo autohide

    # define data we're interested in (gets populated by engine)
    self.autoFit = 100
    self.fullscreen = False
    self.dim = False
    self.onTop = OnTop.Never
    self.remaining = True
    self.hidePopup = False
    self.screenshotDialog = True
    self.showAll = True
    self.splitter = 254
    self.trayIcon = False

    self._mapCommandActions()

    # connect signals and slots
    self.ui.inputLineEdit.submitted.connect(
      lambda s: self.eval(compile(s, '<string>', 'single')))

    self.show()

  def eval(self, s):
    try:
      exec(s, self.exec_scope)
    except Exception as e:
      print(e)

  def output(self, s):
    self.ui.outputTextEdit.moveCursor(QTextCursor.End)
    self.ui.outputTextEdit.insertPlainText(s)

  def _mapCommandActions(self):
    '''
    Map the interface actions to engine commands
    '''
    for cmd, act in [
      ('player.chapter += 1', self.ui.action_Next_Chapter),
      ('player.chapter -= 1', self.ui.action_Previous_Chapter),
      ('player.sub_scale = 1', self.ui.action_Reset_Size),
      ('player.sub_scale += 0.1', self.ui.action_Size),
      ('player.sub_scale -= 0.1', self.ui.actionS_ize),
      ('player.video_aspect = -1', self.ui.action_Auto_Detect),
      ('player.video_aspect = "16:9"', self.ui.actionForce_16_9),
      ('player.video_aspect = "2.35:1"', self.ui.actionForce_2_35_1),
      ('player.video_aspect = "4:3"', self.ui.actionForce_4_3),
      ('player.sub_visibility = not player.sub_visibility', self.ui.actionShow_Subtitles),
      ('player.time_pos = 0', self.ui.action_Restart),
      ('player.frame_step()', self.ui.action_Frame_Step),
      ('player.frame_back_step()', self.ui.actionFrame_Back_Step),
      # ('deinterlace', self.ui.action_Deinterlace),
      # ('interpolate', self.ui.action_Motion_Interpolation),
      ('player.mute = not player.mute', self.ui.action_Mute),
      ('player.screenshot(includes="subtitles")', self.ui.actionWith_Subtitles),
      ('player.screenshot(includes="window")', self.ui.actionWithout_Subtitles),
      ('player.pause = not player.pause', self.ui.action_Play),
      ('player.stop()', self.ui.action_Stop),
      ('player.volume += 5', self.ui.action_Increase_Volume),
      ('player.volume -= 5', self.ui.action_Decrease_Volume),
      ('player.speed += 0.1', self.ui.action_Increase),
      ('player.speed -= 0.1', self.ui.action_Decrease),
      ('player.speed = 1.0', self.ui.action_Reset),
      ('player.play(qt.clipboard().text())', self.ui.actionOpen_Path_from_Clipboard),
      ('window.add_subtitle()', self.ui.action_Add_Subtitle_File),
      ('window.fit()', self.ui.action_To_Current_Size),
      ('window.fit(50)', self.ui.action50),
      ('window.fit(75)', self.ui.action75),
      ('window.fit(100)', self.ui.action100),
      ('window.fit(150)', self.ui.action150),
      ('window.fit(200)', self.ui.action200),
      ('window.fullscreen = not window.fullscreen', self.ui.action_Full_Screen),
      ('window.jump()', self.ui.action_Jump_to_Time),
      ('window.open()', self.ui.action_Open_File),
      ('window.openUrl()', self.ui.actionOpen_URL),
      ('window.dim()', self.ui.action_Dim_Lights),
      ('window.showInFolder()', self.ui.actionShow_in_Folder),
      ('window.output = not window.output', self.ui.actionShow_D_ebug_Output),
      ('window.preferences()', self.ui.action_Preferences),
      ('window.onlineHelp()', self.ui.actionOnline_Help),
      ('window.about()', self.ui.actionAbout_Mochi_MPlayer),
      ('playlist.next()', self.ui.actionPlay_Next_File),
      ('playlist.prev()', self.ui.actionPlay_Previous_File),
      ('playlist.repeat = Repeat.Off', self.ui.action_Off),
      ('playlist.repeat = Repeat.Playlist', self.ui.action_Playlist),
      ('playlist.repeat = Repeat.This', self.ui.action_This_File),
      ('playlist.shuffle()', self.ui.actionSh_uffle),
      ('playlist.show = not playlist.show', self.ui.action_Show_Playlist),
      ('playlist.full = not playlist.full', self.ui.action_Hide_Album_Art),
      ('update.check()', self.ui.action_Check_for_Updates),
      ('update.youtube_dl()', self.ui.actionUpdate_Streaming_Support),
      ('overlay.media_info = not overlay.media_info', self.ui.actionMedia_Info),
      ('engine.new()', self.ui.action_New_Player),
      ('qt.aboutQt()', self.ui.actionAbout_Qt),
      ('qt.quit()', self.ui.actionE_xit),
    ]:
      # compile the function into python byte-code
      f = compile(cmd, '<string>', 'single')
      # attach the function-call to the action
      act.triggered.connect(lambda v, f = f: self.eval(f))

  def dragEnterEvent(self, event):
    '''
    Feedback when something is dragged into window.
    '''
    if event.mimeData().hasUrls() or event.mimeData().hasText():
      event.acceptProposedAction()
    return QMainWindow.dragEnterEvent(self, event)

  def dropEvent(self, event):
    '''
    Process dropping something onto window, play it.
    '''
    mimeData = event.mimeData()
    if mimeData.hasUrls():
      for url in mimeData.urls():
        if url.isLocalFile():
          self.player.play(url.toLocalFile())
        else:
          self.player.play(url.url())
      event.accept()
    elif mimeData.hasText():
      self.player.play(mimeData.text())
      event.accept()
    return QMainWindow.dropEvent(self, event)

  def mousePressEvent(self, event):
    return QMainWindow.mousePressEvent(self, event)

  def mouseReleaseEvent(self, event):
    return QMainWindow.mouseReleaseEvent(self, event)

  def mouseMoveEvent(self, event):
    return QMainWindow.mouseMoveEvent(self, event)

  def eventFilter(self, obj, event):
    return QMainWindow.eventFilter(self, obj, event)

  def wheelEvent(self, event):
    return QMainWindow.wheelEvent(self, event)

  def keyPressEvent(self, event):
    '''
    Process window key events.
    '''
    # make sure we're not interfering with textboxes
    if self.focusWidget() == self.ui.inputLineEdit and event.key() == Qt.Key_Return:
      return
    # get the actual input binding
    key = self.input.get(QKeySequence(event.modifiers() | event.key()).toString())
    if key:
      # execute the attached function
      exec(key[0], self.exec_scope)
      event.accept()
    return QMainWindow.keyPressEvent(self, event)

  def resizeEvent(self, event):
    '''
    Process when window is resized.
    '''
    if self.overlay and self.overlay.media_info:
      self.overlay.refresh()
    return QMainWindow.resizeEvent(self, event)

  def mouseDoubleClickEvent(self, event):
    '''
    Processed when window is double clicked.
    '''
    if event.button() == Qt.LeftButton and ui.mpvFrame.geometry().contains(event.pos()):
      self.fullscreen = not self.fullscreen
      event.accept()
    QMainWindow.mouseDoubleClickEvent(self, event)

  def fit(self, percent=0):
    '''
    Fit window to a specific percentage of the video.
    '''
    pass

  def jump(self):
    '''
    Jump-to-time dialog.
    '''
    pass

  def open(self):
    '''
    Open file dialog.
    '''
    self.player.play(
      QFileDialog.getOpenFileName(
        self,
        self.tr('Open File'),
        self.player.path,
        ';;'.join((
          '%s (%s)' % (self.tr('Media Files'), ' '.join(self.config.media_filetypes)),
          '%s (%s)' % (self.tr('Video Files'), ' '.join(self.config.video_filetypes)),
          '%s (%s)' % (self.tr('Audio Files'), ' '.join(self.config.audio_filetypes)),
          '%s (*.*)' % (self.tr('All Files')),
        )), str(), QFileDialog.DontUseSheet)[0])

  def openUrl(self):
    '''
    Open location dialog.
    '''
    self.player.play(LocationDialog.getUrl(self.player.path, self))

  def dim(self):
    '''
    Dim the screen.
    '''
    pass

  def showInFolder(self):
    '''
    Show the current file in the system explorer.
    '''
    pass

  def preferences(self):
    '''
    Show preferences dialog.
    '''
    pass

  def onlineHelp(self):
    '''
    Load online help.
    '''
    pass

  def about(self):
    '''
    Show our about dialog.
    '''
    AboutDialog.about(self.config.version, self)
