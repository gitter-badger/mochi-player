import sys
from enum import Enum

from PyQt5.Qt import QTextCursor
from PyQt5.QtWidgets import QMainWindow
from .moc.mainwindow import Ui_MainWindow

from .aboutdialog import AboutDialog

class OnTop(Enum):
  Never=0
  Always=1
  Playing=2

class MainWindow(QMainWindow):
  ui = Ui_MainWindow()

  def retranslate(self):
    self.ui.retranslateUi(self)

  def __init__(self):
    super().__init__()
    self.ui.setupUi(self)

    if sys.platform == 'linux' or sys.platform == 'unix': # todo: do this through Config
      self.ui.actionUpdate_Streaming_Support.setEnabled(False)
    self.addActions(self.ui.menubar.actions())
    self.ui.mpvFrame.installEventFilter(self)
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
    self.MapCommandActions()
    self.show()

  def MapCommandActions(self):
    """
    Map the interface actions to engine commands
    """
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
      ('player.mute = True', self.ui.action_Mute),
      ('player.screenshot(includes="subtitles")', self.ui.actionWith_Subtitles),
      ('player.screenshot(includes="window")', self.ui.actionWithout_Subtitles),
      ('player.pause = not player.pause', self.ui.action_Play),
      ('player.stop()', self.ui.action_Stop),
      ('player.volume += 5', self.ui.action_Increase_Volume),
      ('player.volume -= 5', self.ui.action_Decrease_Volume),
      ('player.speed += 0.1', self.ui.action_Increase),
      ('player.speed -= 0.1', self.ui.action_Decrease),
      ('player.speed = 1.0', self.ui.action_Reset),
      ('player.play(qt.clipboard.text())', self.ui.actionOpen_Path_from_Clipboard),
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
      ('window.output = True', self.ui.actionShow_D_ebug_Output),
      ('window.preferences()', self.ui.action_Preferences),
      ('window.onlineHelp()', self.ui.actionOnline_Help),
      ('window.about()', self.ui.actionAbout_Mochi_MPlayer),
      ('playlist.next()', self.ui.actionPlay_Next_File),
      ('playlist.prev()', self.ui.actionPlay_Previous_File),
      ('playlist.repeat = Repeat.Off', self.ui.action_Off),
      ('playlist.repeat = Repeat.Playlist', self.ui.action_Playlist),
      ('playlist.repeat = Repeat.This', self.ui.action_This_File),
      ('playlist.shuffle()', self.ui.actionSh_uffle),
      ('playlist.show = True', self.ui.action_Show_Playlist),
      ('playlist.full = True', self.ui.action_Hide_Album_Art),
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
      act.triggered.connect(lambda v, f=f: exec(f, self.exec_scope))

  def fit(self, percent=0):
    """
    Fit window to a specific percentage of the video.
    """
    pass

  def jump(self):
    """
    Jump-to-time dialog.
    """
    pass

  def open(self):
    """
    Open file dialog.
    """
    pass

  def openUrl(self):
    """
    Open location dialog.
    """
    pass

  def dim(self):
    """
    Dim the screen.
    """
    pass

  def showInFolder(self):
    """
    Show the current file in the system explorer.
    """
    pass

  def preferences(self):
    """
    Show preferences dialog.
    """
    pass

  def onlineHelp(self):
    """
    Load online help.
    """
    pass

  def about(self):
    """
    Show our about dialog.
    """
    AboutDialog(self, self.config.version).show()
