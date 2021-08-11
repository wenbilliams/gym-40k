import random

class Die():
  """Base class to represent a Die"""

  def __init__(self, min = 1, max = 6):
    self.min = min
    self.max = max

  def roll():
      return random.randint(min, max)