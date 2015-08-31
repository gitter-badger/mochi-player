from PyQt5.QtWidgets import QDialog
from .moc.aboutdialog import Ui_AboutDialog
from config import Config

class AboutDialog(QDialog):
  ui = Ui_AboutDialog()
  def __init__(self, parent):
    super(AboutDialog, self).__init__(parent)
    self.ui.setupUi(self)
    self.ui.versionLabel.setText('Mochi-Player %s' % (Config.Version))
    self.ui.closeButton.clicked(self.close)
