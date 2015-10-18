from data import Data

class Recent:
  def __init__(self):
      self.data = Data({
        'max_recent': 10,
        'recent': [],
      })
