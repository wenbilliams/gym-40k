class Board():
  """Class defining a gaming board"""

  def __init__(self, length = 60, width = 44):
      self.length = length
      self.width  = width
      self.terrain = []