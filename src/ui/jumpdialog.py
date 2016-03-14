'''
JumpDialog - Jump to specific time
'''

# from PyQt5.Qt import QApplication, QPixmap, QDir
from PyQt5.QtWidgets import QDialog
from moc.jumpdialog import Ui_JumpDialog

from engine.util import Util


class JumpDialog(QDialog):
    ui = Ui_JumpDialog()

    def __init__(self, maxTime, parent):
        QDialog.__init__(self, parent)
        self.ui.setupUi(self)

        self.time = 0
        self.maxTime = maxTime

        self.ui.okButton.clicked.connect(self.accept)
        self.ui.hourBox.valueChanged.connect(self.validate)
        self.ui.minBox.valueChanged.connect(self.validate)
        self.ui.secBox.valueChanged.connect(self.validate)

        if maxTime > 3600:
            self.ui.hourBox.setFocus()
        elif maxTime > 60:
            self.ui.hourBox.setEnabled(False)
            self.ui.minBox.setFocus()
        else:
            self.ui.hourBox.setEnabled(False)
            self.ui.minBox.setEnabled(False)
            self.ui.secBox.setFocus()

    def getTime(maxTime, parent):
        dialog = JumpDialog(maxTime, parent)
        if dialog.exec_() == QDialog.Accepted:
            return dialog.time

    def validate(self, s):
        self.time = \
            self.ui.hourBox.value() * 3600 + \
            self.ui.minBox.value() * 60 + \
            self.ui.secBox.value()
        if self.time < self.maxTime:
            self.ui.validEntryLabel.setPixmap(QPixmap(':/img/exists.svg'))
            self.ui.okButton.setEnabled(True)
        else:
            self.ui.validEntryLabel.setPixmap(QPixmap(':/img/not_exists.svg'))
            self.ui.okButton.setEnabled(False)
