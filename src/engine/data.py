'''
Data: Base-type for easy configuration by recursively walking through objects.
'''


import json
import copy


class Data:
    data = []
    data_init = {}

    def save_init(self):
        ''' Save the initial state of our class to remove when we save '''
        self.data_init = copy.deepcopy(self.vars())

    def vars(self):
        ''' Walk through Data object tree returning object variables '''
        def want(k):
            ''' Figure out which variables we want '''
            return (type(self.data) == list and k in self.data) or \
                   (type(self.data) == tuple and k not in self.data) or \
                   (callable(self.data) and self.data(k))
        def varsIfData(kv):
            ''' Return key-value tuple if we want it '''
            k,v = kv
            return (k, v.vars() if isinstance(v, Data) else v) if want(k) \
                    else (k, None)
        return {k: v
                for k, v in map(varsIfData, vars(self).items())
                if v and v != self.data_init.get(k)}

    def setVars(self, data):
        ''' Walk through Data object tree inserting values defined in data '''
        for k, v in vars(self).items():
            print(self)
            d = data.get(k)
            if d:
                if isinstance(v, Data):
                    v.setVars(d)
                else:
                    setattr(self, k, d)

    def load(self, file):
        ''' Load from settings. '''
        try:
            f = open(file, 'r')
            self.setVars(json.load(f))
            f.close()
        except Exception as e:
            print('Error in engine.load(%s): %s' % (file, e))

    def save(self, file):
        ''' Save from settings. '''
        try:
            f = open(file, 'w')
            # TODO: only save diffs
            json.dump(self.vars(), f, indent=2, sort_keys=True)
            f.close()
        except Exception as e:
            print('Error in engine.save(%s): %s' % (file, e))
