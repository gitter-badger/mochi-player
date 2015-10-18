class Data(dict):
  __bound__ = {}

  def __init__(self, data):
    super(Data, self).__init__()
    super(Data, self).update(data)
    self.__default__ = data

  def __setitem__(self, key, val):
    bindings = self.__bound__.get(key)
    if bindings:
      for bind in bindings:
        if callable(bind) and callable(val):
          bind(val())
        elif callable(bind) and val:
          bind(val)
        elif bind and callable(val):
          bind = val()
        elif bind and val:
          bind = val
    super(Data, self).__setitem__(key, val)

  def load(self, file):
    import json
    try:
        f = open(file, 'r')
        super(Data, self).update(json.load(f))
        f.close()
    except:
        return False
    return True

  def save(self, file):
    import json, copy
    try:
        f = open(file, 'w')
        d = copy.deepcopy(dict(self))
        for k, v in self.__default__.items():
            if d[k] == v:
                d.pop(k)
        json.dump(d, f, indent=4, sort_keys=True)
        f.close()
    except:
        return False
    return True

  def bind(self, vars):
    for k, v in vars.items():
      V = self.__bound__.get(k)
      if V:
        V.append(v)
      else:
        self.__bound__[k] = [v]

  def refresh(self):
    '''
    Send events to all bound functions.
    '''
    for k, v in self.items():
      self[k] = v
