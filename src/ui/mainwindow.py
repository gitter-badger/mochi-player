'''
MainWindow - [window] handles the gui
'''

from enum import Enum

from PyQt5.Qt import QTextCursor, QDesktopServices, QUrl, qApp, QStyle, QSize
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from .moc.mainwindow import Ui_MainWindow

from util import Util
from .aboutdialog import AboutDialog
from .locationdialog import LocationDialog
from .jumpdialog import JumpDialog


class OnTop(Enum):
    Never = 0
    Always = 1
    Playing = 2


class MainWindow(QMainWindow):
    ui = Ui_MainWindow()
    overlay = None

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui.setupUi(self)
        self.ui.actionUpdate_Streaming_Support.setEnabled(
            Util.canUpdateStreamingSupport())
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

        # connect signals and slots
        # self.ui.inputLineEdit.submitted.connect(self.execute)

        self.show()

    def execute(self, command):
        '''
        Safely compile and evaluate a user python statement
        '''
        try:
            self.eval(compile(command, '<string>', 'single'))
        except Exception as e:
            print('Error in window.execute(%s): %s' % (command, e))

    def output(self, text):
        '''
        Output text to the console textbox.
        '''
        # self.ui.outputTextEdit.moveCursor(QTextCursor.End)
        # self.ui.outputTextEdit.insertPlainText(text)

    # Delegate input events to input class
    def mousePressEvent(self, event):
        self.input.mouse.press(event)
        return QMainWindow.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.input.mouse.move(event)
        return QMainWindow.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        self.input.mouse.release(event)
        return QMainWindow.mouseReleaseEvent(self, event)

    def mouseDoubleClickEvent(self, event):
        self.input.mouse.doubleClick(event)
        return QMainWindow.mouseDoubleClickEvent(self, event)

    def wheelEvent(self, event):
        self.input.mouse.wheel(event)
        return QMainWindow.wheelEvent(self, event)

    def keyPressEvent(self, event):
        if not (self.focusWidget() == self.ui.consoleWidget and
                event.key() == Qt.Key_Return):
            self.input.key.press(event)
        return QMainWindow.keyPressEvent(self, event)

    def eventFilter(self, obj, event):
        return QMainWindow.eventFilter(self, obj, event)

    # Handle other window events
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

    def resizeEvent(self, event):
        '''
        Process when window is resized.
        '''
        if self.overlay and self.overlay.media_info:
            self.overlay.refresh()
        return QMainWindow.resizeEvent(self, event)

    # Window Functions
    def clear(self):
        '''
        Clear the output window.
        '''
        # self.ui.outputTextEdit.clear()

    def fit(self, percent=0):
        '''
        Fit window to a specific percentage of the video.
        '''
        # if self.isFullScreen() or self.isMaximized() or not self.ui.menuFit_Window.isEnabled():
        #   return

        # create a video_params structure
        class video_params:

            def __init__(self, vp):
                self.width, self.height = vp['w'], vp['h']
                self.dwidth, self.dheight = vp['dw'], vp['dh']

        vG = video_params(self.player.video_params)  # video geometry
        mG = self.ui.mpvFrame.geometry()  # mpv geometry
        wfG = self.frameGeometry()  # frame geometry of window (window geometry + window frame)
        wG = self.geometry()  # window geometry
        # available geometry of the screen we're in--(geometry not including
        # the taskbar)
        aG = qApp.desktop().availableGeometry(wfG.center())

        # obtain natural video aspect ratio
        if vG.width == 0 or vG.height == 0:  # width/height are 0 when there is no output
            return

        if vG.dwidth == 0 or vG.dheight == 0:  # dwidth/height are 0 on load
            # use video width and height for aspect ratio
            a = float(vG.width) / vG.height
        else:
            # use display width and height for aspect ratio
            a = float(vG.dwidth) / vG.dheight

        # calculate resulting display:
        if percent == 0:  # fit to window
            # set our current mpv frame dimensions
            w = mG.width()
            h = mG.height()

            c = w / h - a  # comparison
            # epsilon (deal with rounding errors) we consider -eps < 0 < eps
            # ==> 0
            e = 0.01

            if c > e:  # too wide
                w = h * a  # calculate width based on the correct height
            elif c < -e:  # too long
                h = w / a  # calculate height based on the correct width
        else:  # fit into desired dimensions
            scale = percent / 100.0  # get scale

            w = vG.width * scale  # get scaled width
            h = vG.height * scale  # get scaled height

        # calculate display width of the window
        dW = w + (wfG.width() - mG.width())
        # calculate display height of the window
        dH = h + (wfG.height() - mG.height())

        if dW > aG.width():  # if the width is bigger than the available area
            dW = aG.width()  # set the width equal to the available area
            w = dW - (wfG.width() - mG.width())  # calculate the width
            h = w / a  # calculate height
            # calculate new display height
            dH = h + (wfG.height() - mG.height())
        if dH > aG.height():  # if the height is bigger than the available area
            dH = aG.height()  # set the height equal to the available area
            h = dH - (wfG.height() - mG.height())  # calculate the height
            w = h * a  # calculate the width accordingly
            dW = w + (wfG.width() - mG.width())  # calculate new display width

        # get the centered rectangle we want
        rect = QStyle.alignedRect(
            Qt.LeftToRight,
            Qt.AlignCenter,
            QSize(dW, dH),
            wfG if percent == 0 else aG)  # center in window (autofit) or on our screen

        # adjust the rect to compensate for the frame
        rect.setLeft(rect.left() + (wG.left() - wfG.left()))
        rect.setTop(rect.top() + (wG.top() - wfG.top()))
        rect.setRight(rect.right() - (wfG.right() - wG.right()))
        rect.setBottom(rect.bottom() - (wfG.bottom() - wG.bottom()))

        # finally set the geometry of the window
        self.setGeometry(rect)

        # note: the above block is required because there is no
        # setFrameGeometry function

        # self.overlay.showStatusText(self.tr('Fit Window: %s') % (self.tr('To Current Size') if percent == 0 else ('%d%%' % (percent))))

    def jump(self):
        '''
        Jump-to-time dialog.
        '''
        time = JumpDialog.getTime(self.player.length, self)
        if time:
            self.player.time = time

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
                    '%s (%s)' % (self.tr('Media Files'),
                                 ' '.join(self.config.mediaFiletypes)),
                    '%s (%s)' % (self.tr('Video Files'),
                                 ' '.join(self.config.videoFiletypes)),
                    '%s (%s)' % (self.tr('Audio Files'),
                                 ' '.join(self.config.audioFiletypes)),
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
        Util.showInFolder(self.player.path)

    def boss(self):
        '''
        Hide from the boss (Pause/Minimize).
        '''
        self.player.pause = True
        self.setWindowState(self.windowState() | Qt.WindowMinimized)

    def preferences(self):
        '''
        Show preferences dialog.
        '''
        pass

    def onlineHelp(self):
        '''
        Load online help.
        '''
        QDesktopServices.openUrl(QUrl(self.config.onlineHelpUrl))

    def about(self):
        '''
        Show our about dialog.
        '''
        AboutDialog.about(self.config.version, self)
