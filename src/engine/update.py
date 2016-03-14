'''
Update provides a way to check for new updates and automatically
  download new ones replacing the existing installation.
'''

from .data import Data


class Update(Data):

    def check(self):
        ''' Check for new updates. '''
        pass

    def youtube_dl(self):
        ''' Handle youtube-dl updates. '''
        pass
