from PyQt5.QtNetwork import QNetworkAccessManager
from data import Data

class Update(QNetworkAccessManager):
  url = 'http://baka-mplayer.u8sand.net'

  def __init__(self):
    super(QNetworkAccessManager, self).__init__()
    self.data = Data({
        'auto': False
    })
