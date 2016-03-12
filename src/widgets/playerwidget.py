'''
PlayerWidget - handles displaying the player
'''

from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.Qt import Qt, QMetaObject, Q_UNUSED, QOpenGLContext, pyqtSignal


def get_proc_address(ctx, name):
    Q_UNUSED(ctx)
    glctx = QOpenGLContext.currentContext()
    if not glctx:
        return None
    return glctx.getProcAddress(QByteArray(name))


class PlayerWidget(QOpenGLWidget):
    player = Player()

    def __init__(self, parent, flags):
        QOpenGLWidget.__init__(self, parent, flags)
        self.handle_gl = _mpv_get_sub_api(MPV_SUB_API_OPENGL_CB)
        # self.player.set_option('vo', 'opengl-cb')
        self.player.OpenGLCbSetUpdateCallback(self.on_update, self)
        self.frameSwapped.connect(self.swapped)

    def __del__(self):
        self.player.OpenGLCbSetUpdateCallback(None, None)

    def initializeGL(self):
        self.player.OpenGLCbInitGL(None, get_proc_address, None)

    def paintGL(self):
        self.player.OpenGLCbDraw(
            self.defaultFramebufferObject(), widget(), -height())

    def swapped(self):
        self.player.OpenGLCbReportFlip(0)

    def on_update(ctx):
        QMetaObject.invokeMethod(ctx, 'update')
