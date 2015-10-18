import sys
from engine import Engine

if __name__ == '__main__':
  engine = Engine(sys.argv)
  sys.exit(engine.exec_())
