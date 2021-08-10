from gym_40k.engine.terrain_type import TerrainType

class Terrain():
  """Class defining a piece of terrain. In V0, all terrain is square"""

  def __init__(self):
      self.length = 6
      self.width  = 6
      self.terrain_type = TerrainType.Ruins