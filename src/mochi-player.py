#!/bin/python3

'''
mochi-player - a mpv based media player
'''

import sys
from engine import Engine
engine = Engine(sys.argv)
sys.exit(engine.exec_())
