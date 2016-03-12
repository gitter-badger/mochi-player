'''
KeySequenceEdit widget - workaround for PyQt5.uic which doesn't recognize QKeySequenceEdit as an available widget.
'''
from PyQt5.QtWidgets import QKeySequenceEdit


class KeySequenceEdit(QKeySequenceEdit):
    pass
