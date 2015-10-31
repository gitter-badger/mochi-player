from PyQt5.QtWidgets import QDialog
from .moc.aboutdialog import Ui_AboutDialog

class AboutDialog(QDialog):
  ui = Ui_AboutDialog()
  def __init__(self, version, parent):
    QDialog.__init__(self, parent)
    self.ui.setupUi(self)
    self.ui.versionLabel.setText('Mochi-Player %s' % (version))
    self.ui.closeButton.clicked.connect(self.close)

  def about(version, parent):
    AboutDialog(version, parent).show()
