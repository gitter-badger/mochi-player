'''
LocationDialog - Open Location (accepts URLs)
'''

from PyQt5.Qt import QApplication, QPixmap, QDir
from PyQt5.QtWidgets import QDialog
from moc.locationdialog import Ui_LocationDialog

from engine.util import Util


class LocationDialog(QDialog):
    ui = Ui_LocationDialog()

    def __init__(self, path, parent):
        QDialog.__init__(self, parent)
        self.ui.setupUi(self)

        self.ui.okButton.clicked.connect(self.accept)
        self.ui.cancelButton.clicked.connect(self.reject)
        self.ui.urlEdit.textChanged.connect(self.validate)
        self.ui.clearButton.clicked.connect(
            lambda: self.ui.urlEdit.setText(''))
        self.ui.pasteButton.clicked.connect(
            lambda: self.ui.urlEdit.setText(
                QApplication.clipboard().text()))
        self.ui.copyButton.clicked.connect(
            lambda: QApplication.clipboard().setText(
                self.ui.urlEdit.text()))

        if Util.isValidFile(path):
            self.ui.urlEdit.setText(QDir.toNativeSeparators(path))
        else:
            self.ui.urlEdit.setText(path)

    def getUrl(path, parent):
        dialog = LocationDialog(path, parent)
        if dialog.exec_() == QDialog.Accepted:
            return dialog.ui.urlEdit.text()

    def validate(self, s):
        if Util.isValidLocation(s):
            self.ui.validEntryLabel.setPixmap(QPixmap(':/img/exists.svg'))
            self.ui.okButton.setEnabled(True)
        else:
            self.ui.validEntryLabel.setPixmap(QPixmap(':/img/not_exists.svg'))
            self.ui.okButton.setEnabled(False)
