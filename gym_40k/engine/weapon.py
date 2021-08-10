from gym_40k.engine.weapon_type import WeaponType
from gym_40k.engine.weapon_ability import WeaponAbility
from gym_40k.engine.random_quantity import RandomQuantity

class Weapon():
  """Base Warhammer 40K Weapon"""

  def __init__(self):
    self.name = "Bolter"
    self.range = 24
    self.type = WeaponType.RapidFire
    self.attacks = 1
    self.weapon_abilities = []
    self.random_attacks = RandomQuantity.Fixed
    self.random_damage  = RandomQuantity.Fixed
    self.damage         = 1
    self.ap             = 0