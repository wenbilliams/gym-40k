from gym_40k.engine.position import Position
from gym_40k.engine.model_type import ModelType

class Model():
  """Base Warhammer 40K Model"""

  def __init__(self):
    # TODO - Buffs, Debuggs, healing
    self.wounds          = 1
    self.base_size       = 1
    self.move            = 6
    self.weapon_skill    = 4
    self.ballistic_skill = 4
    self.strength        = 3
    self.toughness       = 3
    self.attacks         = 1
    self.leadership      = 6
    self.armor_save      = 5
    self.invul_save      = 0
    self.feel_no_pain    = 6
    self.weapons         = []
    self.name            = "Base human"
    self.team            = 0

    self.type            = ModelType.Infantry

    self.flying          = False
    self.in_close_combat = False

    self.position = Position()
