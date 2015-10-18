from PyQt5.QtNetwork import QTcpServer
from data import Data

class Remote(QTcpServer):
  listen = True
  port = 8474

  def __init__(self):
    super(QTcpServer, self).__init__()

    self.data = Data({
        'listen': True,
        'port': 8474,
    })
