import sys, copy

from PyQt5.Qt import QTextCursor
from PyQt5.QtWidgets import QMainWindow
from .moc.mainwindow import Ui_MainWindow

from .aboutdialog import AboutDialog

from engine import Engine

class MainWindow(QMainWindow):
  ui = Ui_MainWindow()

  def retranslate(self):
    self.ui.retranslateUi(self)
    # todo: repopulate necessary strings

  def __init__(self):
    super().__init__()
    self.ui.setupUi(self)

    if sys.platform == 'linux' or sys.platform == 'unix':
      self.ui.actionUpdate_Streaming_Support.setEnabled(False)
    self.addActions(self.ui.menubar.actions())
    self.ui.mpvFrame.installEventFilter(self)
    # todo autohide

    self.data = Data({
      'autoFit': 100,
      'debug': False,
      'gestures': True,
      'hidePopup': False,
      'lang': 'auto',
      'onTop': 'never',
      'remaining': True,
      'resume': True,
      'screenshotDialog': True,
      'showAll': True,
      'splitter': 254,
      'trayIcon': False,
      'version': Config.Version,
      'mpv': self.mpv.data,
      'recent': self.recent.data,
      'remote': self.remote.data,
      'input': self.input.data,
      'update': self.update.data,
    })

    self.data.bind({
      'lang': self.ChangeLanguage,
      'onTop': lambda t: \
        Util.SetAlwaysOnTop(self.winId(), \
          (t == "never" and False) or \
          (t == "always" and True) or \
          (t == "playing" and self.mpv.state == PlayState.Playing) or
          False),
      'remaining': lambda: self.data.update(self.mpv.data.time),
    })
    self.mpv.data.bind({
      'state': self.ChangeState,
    })
    self.MapCommandActions()

  def Load(self, file=None):
    self.data.load(Config.SettingsFile)
    self.data['mpv']['file'] = file

  def Save(self):
      self.data.save(Config.SettingsFile)

  def ChangeState(self, state):
    ''' Change the mpv state, update interface accordingly '''


  def ChangeLanguage(self, lang):
    if lang == 'auto':
      lang = QLocale.system().name()
    if lang != 'en':
      self.translators = (QTranslator(), QTranslator())
      self.translators[0].load('qt_%s' % (lang), QLibraryInfo.location(QLibraryInfo.TranslationsPath))
      self.translators[1].load('mochi-mplayer_%s' % (lang), Config.LanguagePath)
      qApp.installTranslator(self.translators[0])
      qApp.installTranslator(self.translators[1])
    else:
      qApp.removeTranslator(self.translators[0])
      qApp.removeTranslator(self.translators[1])
    ui.retranslateUi(self)
    self.data.Refresh()

  def MapCommandActions(self):
    commandAction = {
      'mpv add chapter +1': self.ui.action_Next_Chapter,
      'mpv add chapter -1': self.ui.action_Previous_Chapter,
      'mpv set sub-scale 1': self.ui.action_Reset_Size,
      'mpv add sub-scale +0.1': self.ui.action_Size,
      'mpv add sub-scale -0.1': self.ui.actionS_ize,
      'mpv set video-aspect -1': self.ui.action_Auto_Detect,
      'mpv set video-aspect 16:9': self.ui.actionForce_16_9,
      'mpv set video-aspect 2.35:1': self.ui.actionForce_2_35_1,
      'mpv set video-aspect 4:3': self.ui.actionForce_4_3,
      'mpv cycle sub-visibility': self.ui.actionShow_Subtitles,
      'mpv set time-pos 0': self.ui.action_Restart,
      'mpv frame_step': self.ui.action_Frame_Step,
      'mpv frame_back_step': self.ui.actionFrame_Back_Step,
      'deinterlace': self.ui.action_Deinterlace,
      'interpolate': self.ui.action_Motion_Interpolation,
      'mute': self.ui.action_Mute,
      'screenshot subtitles': self.ui.actionWith_Subtitles,
      'screenshot': self.ui.actionWithout_Subtitles,
      'add_subtitles': self.ui.action_Add_Subtitle_File,
      'fitwindow': self.ui.action_To_Current_Size,
      'fitwindow 50': self.ui.action50,
      'fitwindow 75': self.ui.action75,
      'fitwindow 100': self.ui.action100,
      'fitwindow 150': self.ui.action150,
      'fitwindow 200': self.ui.action200,
      'fullscreen': self.ui.action_Full_Screen,
      'jump': self.ui.action_Jump_to_Time,
      'media_info': self.ui.actionMedia_Info,
      'new': self.ui.action_New_Player,
      'open': self.ui.action_Open_File,
      'open_clipboard': self.ui.actionOpen_Path_from_Clipboard,
      'open_location': self.ui.actionOpen_URL,
      'playlist play +1': self.ui.actionPlay_Next_File,
      'playlist play -1': self.ui.actionPlay_Previous_File,
      'playlist repeat off': self.ui.action_Off,
      'playlist repeat playlist': self.ui.action_Playlist,
      'playlist repeat this': self.ui.action_This_File,
      'playlist shuffle': self.ui.actionSh_uffle,
      'playlist toggle': self.ui.action_Show_Playlist,
      'playlist full': self.ui.action_Hide_Album_Art,
      'dim': self.ui.action_Dim_Lights,
      'play_pause': self.ui.action_Play,
      'quit': self.ui.actionE_xit,
      'show_in_folder': self.ui.actionShow_in_Folder,
      'stop': self.ui.action_Stop,
      'volume +5': self.ui.action_Increase_Volume,
      'volume -5': self.ui.action_Decrease_Volume,
      'speed +0.1': self.ui.action_Increase,
      'speed -0.1': self.ui.action_Decrease,
      'speed 1.0': self.ui.action_Reset,
      'output': self.ui.actionShow_D_ebug_Output,
      'preferences': self.ui.action_Preferences,
      'online_help': self.ui.actionOnline_Help,
      'update': self.ui.action_Check_for_Updates,
      'update youtube-dl': self.ui.actionUpdate_Streaming_Support,
      'about qt': self.ui.actionAbout_Qt,
      'about': self.ui.actionAbout_Mochi_MPlayer,
    }
    for cmd, act in commandAction.items():
      act.triggered.connect(lambda: self.command(copy.copy(cmd)))

  def command(self, cmd):
    self.ui.outputTextEdit.moveCursor(QTextCursor.End)
    self.ui.outputTextEdit.insertPlainText('[mochi]: %d\n' % (mochi.command(cmd)))
