import pprint
import re

class BaseColors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'

class TerminalLogger(BaseColors):
  info = 0
  ok = 1
  warning = 2
  error = 3
  unk = 4

  def __init__(self, level = 0):
    """Initialize the pretty printer."""
    self.level = level
    self.pp = pprint.PrettyPrinter(indent=2)

  def log(self, message, messageType):
    """Print a message to the terminal."""
    if self.level == 0:
      # Level 0 means silent.
      return
    elif self.level == 1:
      # Only print errors and ok messages in level 1
      if messageType == self.info or messageType == self.warning or messageType == self.unk:
        return
    if not isinstance(message, basestring):
      self.pp.pprint(message)
    else:
      print self.color_code(messageType) + message + self.ENDC
      

  def color_code(self, messageType):
    """Decide the color code to use based on the message type and the logger level."""
    if messageType == self.info:
      return self.OKBLUE
    elif messageType == self.ok:
      return self.OKGREEN
    elif messageType == self.warning:
      return self.WARNING
    elif messageType == self.error:
      return self.FAIL
    elif messageType == self.unk:
      return self.HEADER
