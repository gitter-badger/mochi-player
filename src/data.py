"""
Data provides a way to store data in core classes, this allows us
  to save/load class data unintrusively.
"""

class Data(dict):
  def __init__(self):
    # load all runtime variables into dictionary
    super().__init__(self.__dict__)

# todo add a way to bind variables to functions
